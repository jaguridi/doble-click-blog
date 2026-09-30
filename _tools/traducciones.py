#!/usr/bin/env python3
"""Estado de la edición en inglés: qué falta traducir y qué quedó desactualizado.

Cada traducción guarda en su front matter `hash_original`: el hash del archivo en español
con que se tradujo. Si el español cambia después (una fe de erratas, una corrección de la
revisión), el hash deja de calzar y la traducción aparece como desactualizada.

Pares:  _posts/X.md     <->  _en_posts/X.md
        _lecturas/X.md  <->  _en_lecturas/X.md

Uso:
  python _tools/traducciones.py                  # informe: faltantes, desactualizadas, huérfanas
  python _tools/traducciones.py --check          # igual, pero sale con código 1 si hay pendientes
  python _tools/traducciones.py --lista          # solo las rutas en español pendientes, una por línea
  python _tools/traducciones.py --diff [RUTA…]   # qué cambió en el español desde que se tradujo
  python _tools/traducciones.py --sellar RUTA…   # guarda el hash actual del original en esas traducciones
  python _tools/traducciones.py --verificar [RUTA…]  # compara la estructura de cada par (ver abajo)

--verificar no juzga la traducción, solo lo que se puede perder sin darse cuenta: que el
front matter sea YAML válido y traiga las mismas claves, que los campos que no se traducen
(fecha, tags, DOI, fuentes…) sean idénticos, que estén los mismos enlaces externos en el
mismo orden, que los internos apunten a /en/, que haya los mismos encabezados y que no
queden números con formato español ("12,5%", "3.000 millones"). Sin rutas, revisa todos los pares. Sale con
código 1 si encuentra algo.

--diff busca en el historial de git la versión del español cuyo hash calza con el de la
traducción y muestra la diferencia con la versión actual. Sin rutas, lo hace para todas
las desactualizadas. Las rutas pueden ser del español o del inglés.

--sellar se usa DESPUÉS de dejar la traducción al día: sellar una traducción que no
refleja el original la esconde del informe. Ver _tools/traduccion_en.md.
"""
import argparse, difflib, glob, hashlib, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARES = [("_posts", "_en_posts"), ("_lecturas", "_en_lecturas")]
CAMPO = "hash_original"
RE_CAMPO = re.compile(r"^%s:.*$" % CAMPO, re.M)


def normalizar(texto):
    """El hash no debe cambiar por finales de línea de Windows ni por espacios al final."""
    return texto.replace("\r\n", "\n").rstrip() + "\n"


def hash_de(texto):
    return hashlib.sha256(normalizar(texto).encode("utf-8")).hexdigest()[:12]


def leer(ruta):
    with open(os.path.join(RAIZ, ruta), encoding="utf-8") as fh:
        return fh.read()


def hash_guardado(ruta_en):
    """El hash_original del front matter de una traducción, o None."""
    texto = leer(ruta_en)
    m = re.match(r"^---\n(.*?)\n---", texto.replace("\r\n", "\n"), re.S)
    if not m:
        return None
    campo = RE_CAMPO.search(m.group(1))
    if not campo:
        return None
    return campo.group(0).split(":", 1)[1].strip().strip("\"'") or None


def par_de(ruta):
    """(ruta_es, ruta_en) a partir de cualquiera de las dos."""
    ruta = ruta.replace("\\", "/")
    if ruta.startswith("./"):
        ruta = ruta[2:]
    for es, en in PARES:
        if ruta.startswith(en + "/"):
            return es + ruta[len(en):], ruta
        if ruta.startswith(es + "/"):
            return ruta, en + ruta[len(es):]
    sys.exit("No reconozco la ruta %s: tiene que estar en %s" % (ruta, ", ".join(d for p in PARES for d in p)))


def estado():
    faltantes, desactualizadas, al_dia, huerfanas = [], [], [], []
    for es, en in PARES:
        originales = {os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, es, "*.md"))}
        traducidas = {os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, en, "*.md"))}
        for nombre in sorted(originales):
            ruta_es, ruta_en = "%s/%s" % (es, nombre), "%s/%s" % (en, nombre)
            if nombre not in traducidas:
                faltantes.append(ruta_es)
            elif hash_guardado(ruta_en) != hash_de(leer(ruta_es)):
                desactualizadas.append(ruta_es)
            else:
                al_dia.append(ruta_es)
        huerfanas += ["%s/%s" % (en, n) for n in sorted(traducidas - originales)]
    return faltantes, desactualizadas, al_dia, huerfanas


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")


def version_traducida(ruta_es, objetivo):
    """El contenido del español en el commit donde su hash era `objetivo`, o None."""
    if not objetivo:
        return None
    log = git("log", "--format=%H", "--follow", "--", ruta_es)
    for sha in log.stdout.split():
        show = git("show", "%s:%s" % (sha, ruta_es))
        if show.returncode == 0 and hash_de(show.stdout) == objetivo:
            return show.stdout
    return None


def mostrar_diff(ruta_es, ruta_en):
    antes = version_traducida(ruta_es, hash_guardado(ruta_en))
    print("=" * 78)
    print("%s  ->  %s" % (ruta_es, ruta_en))
    if antes is None:
        print("  (no encontré en git la versión con que se tradujo: retraduce el archivo completo)")
        return
    actual = leer(ruta_es)
    lineas = difflib.unified_diff(normalizar(antes).splitlines(), normalizar(actual).splitlines(),
                                  "traducido", "actual", lineterm="")
    salida = "\n".join(lineas)
    print(salida if salida else "  (sin cambios de contenido: basta con sellar)")


def sellar(ruta_en):
    ruta_es, ruta_en = par_de(ruta_en)
    if not os.path.exists(os.path.join(RAIZ, ruta_en)):
        sys.exit("No existe la traducción %s" % ruta_en)
    valor = hash_de(leer(ruta_es))
    texto = leer(ruta_en)
    crlf = "\r\n" in texto
    texto = texto.replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    if not m:
        sys.exit("%s no tiene front matter" % ruta_en)
    fm = m.group(1)
    linea = '%s: "%s"' % (CAMPO, valor)
    fm = RE_CAMPO.sub(linea, fm) if RE_CAMPO.search(fm) else fm + "\n" + linea
    texto = "---\n" + fm + "\n---" + texto[m.end():]
    if crlf:
        texto = texto.replace("\n", "\r\n")
    with open(os.path.join(RAIZ, ruta_en), "w", encoding="utf-8", newline="") as fh:
        fh.write(texto)
    print("sellada %s (%s)" % (ruta_en, valor))


# Campos que la traducción copia tal cual (ver _tools/traduccion_en.md).
FIJOS = ["layout", "date", "tags", "audio", "numero", "paper_titulo", "paper_doi", "paper_archivo"]
FIJOS_FUENTE = ["url", "tipo", "nivel", "fecha"]
RE_ENLACE = re.compile(r"\]\((https?://[^)\s]+|/[^)\s]*)\)|href=\"([^\"]+)\"")
DOMINIO = "https://dobleclick.jaguridi.cl"


def partes(texto):
    """(front matter como texto, cuerpo)."""
    texto = texto.replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?", texto, re.S)
    return (m.group(1), texto[m.end():]) if m else ("", texto)


def enlaces(cuerpo):
    return [a or b for a, b in RE_ENLACE.findall(cuerpo)]


def es_interno(url):
    return url.startswith("/") or url.startswith(DOMINIO)


def verificar_par(ruta_es, ruta_en):
    problemas = []
    if not os.path.exists(os.path.join(RAIZ, ruta_en)):
        return ["no existe la traducción"]
    fm_es, cuerpo_es = partes(leer(ruta_es))
    fm_en, cuerpo_en = partes(leer(ruta_en))
    try:
        import yaml
        d_es = yaml.safe_load(fm_es) or {}
        d_en = yaml.safe_load(fm_en) or {}
    except ImportError:
        d_es = d_en = None
    except Exception as e:  # YAML inválido
        return ["front matter inválido: %s" % str(e).splitlines()[0]]
    if d_es is not None:
        faltan = set(d_es) - set(d_en)
        sobran = set(d_en) - set(d_es) - {CAMPO}
        if faltan:
            problemas.append("faltan claves: %s" % ", ".join(sorted(faltan)))
        if sobran:
            problemas.append("claves que el original no tiene: %s" % ", ".join(sorted(sobran)))
        for k in FIJOS:
            if k in d_es and d_es.get(k) != d_en.get(k):
                problemas.append("%s distinto: %r / %r" % (k, d_es.get(k), d_en.get(k)))
        f_es, f_en = d_es.get("fuentes") or [], d_en.get("fuentes") or []
        if len(f_es) != len(f_en):
            problemas.append("fuentes: %d en el original, %d en la traducción" % (len(f_es), len(f_en)))
        else:
            for i, (a, b) in enumerate(zip(f_es, f_en)):
                for k in FIJOS_FUENTE:
                    if (a or {}).get(k) != (b or {}).get(k):
                        problemas.append("fuentes[%d].%s distinto" % (i, k))
    ext_es = [u for u in enlaces(cuerpo_es) if not es_interno(u)]
    ext_en = [u for u in enlaces(cuerpo_en) if not es_interno(u)]
    if ext_es != ext_en:
        solo_es = [u for u in ext_es if u not in ext_en]
        solo_en = [u for u in ext_en if u not in ext_es]
        detalle = ("; solo en el original: %s" % ", ".join(solo_es[:3])) if solo_es else ""
        detalle += ("; solo en la traducción: %s" % ", ".join(solo_en[:3])) if solo_en else ""
        problemas.append("enlaces externos distintos (%d / %d)%s" % (len(ext_es), len(ext_en), detalle or "; mismo conjunto, otro orden"))
    for u in enlaces(cuerpo_en):
        ruta = u[len(DOMINIO):] if u.startswith(DOMINIO) else u
        if es_interno(u) and ruta.startswith("/") and not ruta.startswith("/en/") and not ruta.startswith("/assets/"):
            problemas.append("enlace interno sin /en/: %s" % u)
    for nivel in ("## ", "### "):
        n_es = len(re.findall(r"^%s" % nivel, cuerpo_es, re.M))
        n_en = len(re.findall(r"^%s" % nivel, cuerpo_en, re.M))
        if n_es != n_en:
            problemas.append("encabezados '%s': %d / %d" % (nivel.strip(), n_es, n_en))
    # "1.276 billion" es correcto en inglés; lo que delata un número sin convertir es la
    # coma decimal ("12,5%") o la palabra en español que quedó al lado.
    for m in re.finditer(r"(?<![\w.,/-])\d{1,3},\d+ ?%|\b\d[\d.,]* (?:millones|billones|mil millones)\b", cuerpo_en):
        problemas.append("número con formato español: %r" % m.group(0))
    return problemas


def main():
    ap = argparse.ArgumentParser(description="Estado de la edición en inglés.")
    ap.add_argument("--check", action="store_true", help="código de salida 1 si hay pendientes")
    ap.add_argument("--lista", action="store_true", help="solo las rutas pendientes")
    ap.add_argument("--diff", nargs="*", metavar="RUTA", help="cambios del español desde la traducción")
    ap.add_argument("--sellar", nargs="+", metavar="RUTA", help="guarda el hash del original")
    ap.add_argument("--verificar", nargs="*", metavar="RUTA", help="compara la estructura de cada par")
    a = ap.parse_args()

    if a.sellar:
        for r in a.sellar:
            sellar(r)
        return

    if a.verificar is not None:
        if a.verificar:
            pares = [par_de(r) for r in a.verificar]
        else:
            pares = []
            for es, en in PARES:
                for p in sorted(glob.glob(os.path.join(RAIZ, es, "*.md"))):
                    nombre = os.path.basename(p)
                    if os.path.exists(os.path.join(RAIZ, en, nombre)):
                        pares.append(("%s/%s" % (es, nombre), "%s/%s" % (en, nombre)))
        con_problemas = 0
        for es, en in pares:
            problemas = verificar_par(es, en)
            if problemas:
                con_problemas += 1
                print(en)
                for p in problemas:
                    print("  - " + p)
        print("%d de %d traducciones con algo que revisar." % (con_problemas, len(pares)))
        if con_problemas:
            sys.exit(1)
        return

    faltantes, desactualizadas, al_dia, huerfanas = estado()

    if a.diff is not None:
        rutas = [par_de(r) for r in a.diff] or [par_de(r) for r in desactualizadas]
        if not rutas:
            print("No hay traducciones desactualizadas.")
        for es, en in rutas:
            mostrar_diff(es, en)
        return

    if a.lista:
        for r in faltantes + desactualizadas:
            print(r)
        return

    print("Edición en inglés: %d al día, %d por traducir, %d desactualizadas."
          % (len(al_dia), len(faltantes), len(desactualizadas)))
    for titulo, rutas in (("Por traducir", faltantes), ("Desactualizadas (el original cambió)", desactualizadas),
                          ("Huérfanas (sin original en español)", huerfanas)):
        if rutas:
            print("\n%s:" % titulo)
            for r in rutas:
                print("  " + r)
    if a.check and (faltantes or desactualizadas):
        sys.exit(1)


if __name__ == "__main__":
    main()
