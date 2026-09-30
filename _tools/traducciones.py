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


def main():
    ap = argparse.ArgumentParser(description="Estado de la edición en inglés.")
    ap.add_argument("--check", action="store_true", help="código de salida 1 si hay pendientes")
    ap.add_argument("--lista", action="store_true", help="solo las rutas pendientes")
    ap.add_argument("--diff", nargs="*", metavar="RUTA", help="cambios del español desde la traducción")
    ap.add_argument("--sellar", nargs="+", metavar="RUTA", help="guarda el hash del original")
    a = ap.parse_args()

    if a.sellar:
        for r in a.sellar:
            sellar(r)
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
