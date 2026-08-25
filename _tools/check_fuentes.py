#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Control periódico de la página /fuentes/.

Lee `_data/fuentes.yml`, golpea cada URL y reporta:

  - Caídas reales (4xx/5xx que no sean bloqueo de bots).
  - Redirecciones permanentes (301/308) cuyo destino ya no es la URL listada.
  - Bloqueos de bots (403/429): la fuente probablemente sigue viva, pero no se
    puede confirmar desde un runner. No es una caída.
  - Errores de red/DNS/TLS.

Y cierra con un recordatorio de vigencia institucional: los enlaces pueden
responder 200 y aun así apuntar a un organismo que ya no existe o que perdió
las competencias por las que lo seguíamos (caso INAI México, extinguido en
2025). Eso ninguna herramienta lo detecta sola; hay que mirarlo a mano.

Es informativo: SIEMPRE termina con exit code 0. No modifica nada.

Uso:
    python _tools/check_fuentes.py
    python _tools/check_fuentes.py --file _data/fuentes.yml --timeout 25 --workers 8

Sin dependencias: usa PyYAML si está instalado y, si no, cae a un parser por
regex del formato inline controlado que usa el archivo
(`- { nombre: "...", url: "..." }`).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin, urlsplit, urlunsplit

# Un runner de Actions con el User-Agent de urllib se come 403 de medio mundo.
# Con un UA de navegador el ruido baja bastante.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,pt;q=0.8,en;q=0.7",
}

# Estados
OK = "ok"
REDIR = "redir"
BLOQUEO = "bloqueo"
CAIDA = "caida"
ERROR = "error"


# --------------------------------------------------------------------------
# Lectura del YAML
# --------------------------------------------------------------------------

def cargar_fuentes(ruta: str) -> list[dict]:
    """Devuelve [{categoria, nombre, url}, ...] desde _data/fuentes.yml."""
    with open(ruta, "r", encoding="utf-8") as fh:
        texto = fh.read()

    try:
        import yaml  # type: ignore
    except ImportError:
        return _parsear_regex(texto)

    datos = yaml.safe_load(texto) or {}
    salida = []
    for cat in datos.get("categorias", []) or []:
        nombre_cat = (cat or {}).get("nombre", "(sin categoría)")
        for f in (cat or {}).get("fuentes", []) or []:
            if not f or not f.get("url"):
                continue
            salida.append(
                {
                    "categoria": nombre_cat,
                    "nombre": f.get("nombre", f["url"]),
                    "url": f["url"],
                }
            )
    return salida


_RE_CAT = re.compile(r'^\s*-\s+nombre:\s*"(?P<nombre>[^"]+)"\s*$')
_RE_FUENTE = re.compile(
    r'^\s*-\s*\{\s*nombre:\s*"(?P<nombre>[^"]*)"\s*,\s*url:\s*"(?P<url>[^"]+)"\s*\}\s*$'
)


def _parsear_regex(texto: str) -> list[dict]:
    """Fallback sin PyYAML. Sirve porque el formato del archivo es controlado:
    categorías con `- nombre: "..."` y fuentes con `- { nombre: "...", url: "..." }`.
    """
    salida = []
    categoria = "(sin categoría)"
    for linea in texto.splitlines():
        m = _RE_FUENTE.match(linea)
        if m:
            salida.append(
                {
                    "categoria": categoria,
                    "nombre": m.group("nombre") or m.group("url"),
                    "url": m.group("url"),
                }
            )
            continue
        m = _RE_CAT.match(linea)
        if m:
            categoria = m.group("nombre")
    return salida


# --------------------------------------------------------------------------
# Chequeo HTTP
# --------------------------------------------------------------------------

class _SinRedirecciones(urllib.request.HTTPRedirectHandler):
    """Queremos VER el 301, no seguirlo en silencio."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _normalizar(url: str) -> str:
    """Para comparar destinos de redirección sin marcar ruido cosmético
    (slash final, http->https, www, puerto por defecto, mayúsculas del host)."""
    p = urlsplit(url)
    host = p.netloc.lower()
    for puerto in (":443", ":80"):
        if host.endswith(puerto):
            host = host[: -len(puerto)]
    if host.startswith("www."):
        host = host[4:]
    camino = p.path.rstrip("/")
    return urlunsplit(("https", host, camino, p.query, ""))


def _abrir(url: str, metodo: str, timeout: int, ctx):
    req = urllib.request.Request(url, headers=HEADERS, method=metodo)
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ctx), _SinRedirecciones
    )
    return opener.open(req, timeout=timeout)


def _contexto_permisivo():
    """Algunos servidores (varias universidades y organismos públicos) siguen
    con configuraciones TLS viejas y le tiran un handshake failure al contexto
    por defecto de Python. Bajar el nivel de seguridad solo para volver a
    preguntar 'estás vivo' es aceptable: no leemos ni enviamos nada sensible."""
    ctx = ssl.create_default_context()
    try:
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
    except ssl.SSLError:
        pass
    return ctx


def revisar(fuente: dict, timeout: int) -> dict:
    url = fuente["url"]
    ctx = ssl.create_default_context()
    resultado = dict(fuente)
    ultimo = None

    for metodo in ("HEAD", "GET", "GET-TLS-LEGACY"):
        try:
            if metodo == "GET-TLS-LEGACY":
                resp = _abrir(url, "GET", timeout, _contexto_permisivo())
            else:
                resp = _abrir(url, metodo, timeout, ctx)
            resultado.update(estado=OK, codigo=resp.getcode(), detalle="")
            resp.close()
            return resultado

        except urllib.error.HTTPError as e:
            codigo = e.code
            destino = e.headers.get("Location", "") if e.headers else ""

            if codigo in (301, 308):
                # Location puede venir relativo ("/the-batch"): resolverlo contra
                # la URL original, si no todo redirect relativo parece un cambio.
                if destino:
                    destino = urljoin(url, destino)
                if destino and _normalizar(destino) != _normalizar(url):
                    resultado.update(
                        estado=REDIR, codigo=codigo, detalle=f"-> {destino}"
                    )
                else:
                    resultado.update(estado=OK, codigo=codigo, detalle="")
                return resultado

            if codigo in (302, 303, 307):
                # Redirección temporal: normal en sitios que rebotan por idioma
                # o sesión. No es hallazgo.
                resultado.update(estado=OK, codigo=codigo, detalle="")
                return resultado

            if codigo in (403, 405, 429, 418, 501, 999) and metodo == "HEAD":
                # Puede ser que el servidor no acepte HEAD. Reintenta con GET.
                continue

            if codigo in (401, 403, 429, 418, 999):
                resultado.update(
                    estado=BLOQUEO,
                    codigo=codigo,
                    detalle="bloqueo de bots o muro; revisar a mano en el navegador",
                )
                return resultado

            resultado.update(estado=CAIDA, codigo=codigo, detalle=e.reason or "")
            return resultado

        except Exception as e:  # timeout, DNS, TLS, etc.
            es_tls = isinstance(e, ssl.SSLError) or "SSL" in str(e)
            if metodo == "HEAD" or (metodo == "GET" and es_tls):
                # HEAD puede no estar soportado; un fallo de TLS merece un
                # segundo intento con un contexto más tolerante.
                ultimo = e
                continue
            resultado.update(
                estado=ERROR, codigo=None, detalle=f"{type(e).__name__}: {e}"
            )
            return resultado

    resultado.update(
        estado=ERROR,
        codigo=None,
        detalle=f"{type(ultimo).__name__}: {ultimo}" if ultimo else "sin respuesta",
    )
    return resultado


# --------------------------------------------------------------------------
# Reporte
# --------------------------------------------------------------------------

# Dominios de organismos públicos: son los que hay que mirar por vigencia,
# no solo por enlace roto.
_RE_PUBLICO = re.compile(
    r"(^|\.)((gob|gov)\.[a-z]{2,3}|gov\.br|gouv\.fr|gob\.mx|europa\.eu|"
    r"jus\.br|un\.org|unesco\.org|oecd\.[a-z]+|cepal\.org|iadb\.org|"
    r"nist\.gov|aisi\.gov\.uk|iea\.org)$"
)


def _es_publico(url: str) -> bool:
    host = urlsplit(url).netloc.lower().split(":")[0]
    return bool(_RE_PUBLICO.search(host)) or ".gob." in host or ".gov." in host


def _linea(r: dict) -> str:
    cod = r["codigo"] if r["codigo"] is not None else "—"
    extra = f"  {r['detalle']}" if r["detalle"] else ""
    return f"    [{cod}] {r['nombre']}\n          {r['url']}{extra}\n          categoría: {r['categoria']}"


def imprimir_reporte(resultados: list[dict]) -> int:
    por_estado: dict[str, list[dict]] = {}
    for r in resultados:
        por_estado.setdefault(r["estado"], []).append(r)

    total = len(resultados)
    caidas = por_estado.get(CAIDA, [])
    errores = por_estado.get(ERROR, [])
    redirs = por_estado.get(REDIR, [])
    bloqueos = por_estado.get(BLOQUEO, [])
    ok = por_estado.get(OK, [])

    print("=" * 78)
    print("  Control de enlaces de la página /fuentes/")
    print("=" * 78)
    print(f"  Revisadas: {total}   OK: {len(ok)}   "
          f"Caídas: {len(caidas)}   Redirecciones: {len(redirs)}   "
          f"Bloqueos: {len(bloqueos)}   Errores de red: {len(errores)}")
    print()

    if caidas:
        print("-- CAÍDAS (4xx/5xx) — hay que corregir o dar de baja la fuente")
        print("   Ojo: algunos sitios devuelven 404 a clientes que no son un")
        print("   navegador en vez de 403. gob.mx lo hace incluso en su portada.")
        print("   Confirmar en el navegador antes de sacar una fuente de la lista.")
        for r in sorted(caidas, key=lambda x: x["categoria"]):
            print(_linea(r))
        print()

    if errores:
        print("-- ERRORES DE RED (timeout, DNS, TLS) — reintentar antes de tocar nada")
        for r in sorted(errores, key=lambda x: x["categoria"]):
            print(_linea(r))
        print()

    if redirs:
        print("-- REDIRECCIONES PERMANENTES — conviene actualizar la URL listada")
        for r in sorted(redirs, key=lambda x: x["categoria"]):
            print(_linea(r))
        print()

    if bloqueos:
        print("-- BLOQUEOS DE BOTS (403/429) — la fuente sigue viva; no es una caída")
        for r in sorted(bloqueos, key=lambda x: x["categoria"]):
            print(_linea(r))
        print()

    publicos = sorted(
        {(r["nombre"], r["url"]) for r in resultados if _es_publico(r["url"])}
    )
    print("-" * 78)
    print("  RECORDATORIO DE VIGENCIA INSTITUCIONAL")
    print("-" * 78)
    print("  Un enlace puede responder 200 y aun así apuntar a un organismo que")
    print("  ya no existe, se fusionó o perdió las competencias por las que lo")
    print("  seguíamos. El INAI mexicano fue extinguido en 2025 y sus funciones")
    print("  de protección de datos pasaron a la Secretaría Anticorrupción y")
    print("  Buen Gobierno: el dominio siguió respondiendo un buen rato.")
    print()
    print("  Antes de citar a cualquiera de estos organismos, confirmar que")
    print("  sigue existiendo con las mismas competencias:")
    for nombre, url in publicos:
        print(f"    · {nombre} — {url}")
    print()
    print("  (Este chequeo es informativo: no abre issues ni edita contenido.)")
    print("=" * 78)

    return len(caidas) + len(errores) + len(redirs)


# --------------------------------------------------------------------------

def main() -> int:
    aquí = os.path.dirname(os.path.abspath(__file__))
    predeterminado = os.path.join(os.path.dirname(aquí), "_data", "fuentes.yml")

    ap = argparse.ArgumentParser(
        description="Revisa los enlaces de _data/fuentes.yml. Informativo, "
                    "siempre sale con código 0."
    )
    ap.add_argument("--file", default=predeterminado, help="ruta a fuentes.yml")
    ap.add_argument("--timeout", type=int, default=20, help="timeout por URL (s)")
    ap.add_argument("--workers", type=int, default=8, help="chequeos en paralelo")
    args = ap.parse_args()

    if not os.path.exists(args.file):
        print(f"No encuentro {args.file}. Nada que revisar.")
        return 0

    fuentes = cargar_fuentes(args.file)
    if not fuentes:
        print(f"{args.file} no tiene fuentes legibles. Revisar el formato.")
        return 0

    print(f"Revisando {len(fuentes)} fuentes de {args.file} ...\n")

    resultados = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futuros = {pool.submit(revisar, f, args.timeout): f for f in fuentes}
        for fut in concurrent.futures.as_completed(futuros):
            try:
                resultados.append(fut.result())
            except Exception as e:  # que un fallo raro no tumbe el reporte
                f = futuros[fut]
                resultados.append(
                    dict(f, estado=ERROR, codigo=None,
                         detalle=f"{type(e).__name__}: {e}")
                )

    hallazgos = imprimir_reporte(resultados)
    if hallazgos:
        print(f"\nHallazgos que requieren mirada humana: {hallazgos}")
    else:
        print("\nSin hallazgos: todos los enlaces respondieron bien.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
