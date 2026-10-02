#!/usr/bin/env python3
"""Estado de la edición en inglés: qué falta traducir y qué quedó desactualizado.

Cada traducción guarda en su front matter `hash_original`: el hash del archivo en español
con que se tradujo. Si el español cambia después (una fe de erratas, una corrección de la
revisión), el hash deja de calzar y la traducción aparece como desactualizada.

Pares:  _posts/X.md     <->  _en_posts/X.md
        _lecturas/X.md  <->  _en_lecturas/X.md
        _audio/X.txt    <->  _audio/en/X.txt     (el doblaje del audio; ver abajo)

Uso:
  python _tools/traducciones.py                  # informe: faltantes, desactualizadas, huérfanas
  python _tools/traducciones.py --check          # igual, pero sale con código 1 si hay pendientes
  python _tools/traducciones.py --lista          # solo las rutas en español pendientes, una por línea
  python _tools/traducciones.py --diff [RUTA…]   # qué cambió en el español desde que se tradujo
  python _tools/traducciones.py --sellar RUTA…   # guarda el hash actual del original en esas traducciones
  python _tools/traducciones.py --verificar [RUTA…]  # compara la estructura de cada par (ver abajo)
  python _tools/traducciones.py --voces          # asigna voz a los guiones en inglés que no la tienen

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

El audio en inglés es el doblaje del guion en español. Los .txt no tienen front matter, así
que el hash del guion con que se dobló cada uno vive en _audio/en/sellos.yml. --diff,
--sellar y --verificar aceptan las rutas de los guiones (_audio/X.txt o _audio/en/X.txt), y
--verificar revisa además que sea texto plano para TTS, con los mismos párrafos, un largo
parecido y voz asignada. --voces alterna mujer y hombre por orden de fecha.
"""
import argparse, difflib, glob, hashlib, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARES = [("_posts", "_en_posts"), ("_lecturas", "_en_lecturas")]
CAMPO = "hash_original"
RE_CAMPO = re.compile(r"^%s:.*$" % CAMPO, re.M)

# Doblaje. Se doblan todas las lecturas y las entradas desde DOBLAJE_DESDE: las anteriores
# quedan con audio solo en español (decisión de José, 2026-10-01).
AUDIO_ES, AUDIO_EN = "_audio", "_audio/en"
SELLOS_AUDIO = "_audio/en/sellos.yml"
DOBLAJE_DESDE = "2026-09-27"
VOCES_EN = ("en-US-female", "en-US-male")  # se alternan, en este orden
CIERRE_ES = "Esto fue una entrada automática de Doble Click; conviene verificar cada noticia en sus fuentes."
CIERRE_EN = "This was an automated Doble Click entry; please verify each story against its sources."


def normalizar(texto):
    """El hash no debe cambiar por finales de línea de Windows ni por espacios al final."""
    return texto.replace("\r\n", "\n").rstrip() + "\n"


def hash_de(texto):
    return hashlib.sha256(normalizar(texto).encode("utf-8")).hexdigest()[:12]


def leer(ruta):
    with open(os.path.join(RAIZ, ruta), encoding="utf-8") as fh:
        return fh.read()


def hash_guardado(ruta_en):
    """El hash_original del front matter de una traducción (o el sello de un guion), o None."""
    if es_audio(ruta_en):
        return leer_sellos().get(slug_de(ruta_en))
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
    if ruta.startswith(AUDIO_EN + "/") and ruta.endswith(".txt"):
        return AUDIO_ES + ruta[len(AUDIO_EN):], ruta
    if ruta.startswith(AUDIO_ES + "/") and ruta.count("/") == 1 and ruta.endswith(".txt"):
        return ruta, AUDIO_EN + ruta[len(AUDIO_ES):]
    sys.exit("No reconozco la ruta %s: tiene que estar en %s" % (
        ruta, ", ".join([d for p in PARES for d in p] + [AUDIO_ES, AUDIO_EN])))


def es_audio(ruta):
    return ruta.replace("\\", "/").startswith(AUDIO_ES + "/")


def slug_de(ruta):
    """El slug de un guion (_audio/X.txt, _audio/en/X.txt) o de una entrada (_posts/AAAA-MM-DD-X.md)."""
    nombre = os.path.splitext(os.path.basename(ruta))[0]
    return nombre[11:] if re.match(r"\d{4}-\d{2}-\d{2}-", nombre) else nombre


def leer_sellos():
    sellos, ruta = {}, os.path.join(RAIZ, SELLOS_AUDIO)
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            for linea in fh:
                m = re.match(r'^([^#\s][^:]*):\s*"?([0-9a-f]+)"?\s*$', linea)
                if m:
                    sellos[m.group(1)] = m.group(2)
    return sellos


def escribir_sellos(sellos):
    lineas = ["# Hash del guion en español (_audio/<slug>.txt) con que se dobló cada guion en inglés.",
              "# Lo escribe `python _tools/traducciones.py --sellar _audio/en/<slug>.txt`: no editar a mano.",
              ""] + ['%s: "%s"' % (s, sellos[s]) for s in sorted(sellos)]
    with open(os.path.join(RAIZ, SELLOS_AUDIO), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lineas) + "\n")


def leer_voz(slug):
    ruta = os.path.join(RAIZ, AUDIO_EN, slug + ".voice")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return fh.read().strip()


def doblables():
    """Los guiones en español que llevan doblaje: todas las lecturas y las entradas desde
    DOBLAJE_DESDE, siempre que tengan `audio: true` y guion."""
    rutas = []
    for es, _ in PARES:
        for p in sorted(glob.glob(os.path.join(RAIZ, es, "*.md"))):
            nombre = os.path.basename(p)
            if es == "_posts" and nombre[:10] < DOBLAJE_DESDE:
                continue
            fm, _ = partes(leer("%s/%s" % (es, nombre)))
            guion = "%s/%s.txt" % (AUDIO_ES, slug_de(nombre))
            if re.search(r"^audio:\s*true\s*$", fm, re.M) and os.path.exists(os.path.join(RAIZ, guion)):
                rutas.append(guion)
    return rutas


def estado_audio():
    sellos = leer_sellos()
    faltantes, sin_sellar, desactualizados, al_dia = [], [], [], []
    for ruta_es in doblables():
        slug = slug_de(ruta_es)
        if not os.path.exists(os.path.join(RAIZ, AUDIO_EN, slug + ".txt")):
            faltantes.append(ruta_es)
        elif slug not in sellos:
            sin_sellar.append(ruta_es)
        elif sellos[slug] != hash_de(leer(ruta_es)):
            desactualizados.append(ruta_es)
        else:
            al_dia.append(ruta_es)
    return faltantes, sin_sellar, desactualizados, al_dia


def sin_mp3(rutas_es):
    """De los doblajes al día, los que no tienen mp3 o lo tienen de un guion anterior. El mp3 lo
    hace el Action de audio después del push, con el mismo hash que calcula esta función, y lo
    anota en _data/voces_en.yml (ver _tools/tts_elevenlabs.py)."""
    hechos, slug, ruta = {}, None, os.path.join(RAIZ, "_data", "voces_en.yml")
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            for linea in fh:
                m = re.match(r"^([^#\s][^:]*):\s*$", linea)
                if m:
                    slug = m.group(1)
                    continue
                m = re.match(r'^  guion:\s*"(.*)"', linea)
                if m and slug:
                    hechos[slug] = m.group(1)
    faltan = []
    for ruta_es in rutas_es:
        slug = slug_de(ruta_es)
        texto = normalizar(leer("%s/%s.txt" % (AUDIO_EN, slug))).strip()
        guion = hashlib.sha256(((leer_voz(slug) or "") + "\n" + texto).encode("utf-8")).hexdigest()[:12]
        mp3 = os.path.join(RAIZ, "assets", "audio", "en", slug + ".mp3")
        if not os.path.exists(mp3) or hechos.get(slug) != guion:
            faltan.append(ruta_es)
    return faltan


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
        # cat-file y no `git show sha:ruta`: en Windows, show intenta leer el argumento como
        # un archivo antes de resolverlo y falla con rutas largas ("Filename too long").
        show = git("cat-file", "blob", "%s:%s" % (sha, ruta_es))
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


def sellar_audio(ruta_es, ruta_en):
    if not os.path.exists(os.path.join(RAIZ, ruta_en)):
        sys.exit("No existe el guion en inglés %s" % ruta_en)
    slug = slug_de(ruta_en)
    if leer_voz(slug) not in VOCES_EN:
        sys.exit("%s no tiene voz: corre antes `python _tools/traducciones.py --voces`" % ruta_en)
    sellos = leer_sellos()
    sellos[slug] = hash_de(leer(ruta_es))
    escribir_sellos(sellos)
    print("sellado %s (%s)" % (ruta_en, sellos[slug]))


def sellar(ruta_en):
    ruta_es, ruta_en = par_de(ruta_en)
    if es_audio(ruta_en):
        return sellar_audio(ruta_es, ruta_en)
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


RE_NUMERO_ES = re.compile(r"(?<![\w.,/-])\d{1,3},\d+ ?%|\b\d[\d.,]* (?:millones|billones|mil millones)\b")
NO_VA_EN_AUDIO = [
    (re.compile(r"https?://|www\."), "URL"),
    (re.compile(r"[*_#\[\]`<>|]"), "marca de formato"),
    (re.compile("[\u2014\u2013]"), "raya"),
    (re.compile(r"[$%&/@€]"), "símbolo (en palabras: percent, dollars, and…)"),
    (re.compile(r"\bDouble (?:Click|Reading)\b", re.I), "marca traducida (es Doble Click / Doble Lectura)"),
]


def parrafos(texto):
    return [p for p in re.split(r"\n\s*\n", normalizar(texto).strip()) if p.strip()]


def verificar_audio(ruta_es, ruta_en):
    """Lo que se puede perder sin darse cuenta al doblar un guion. No juzga la traducción."""
    if not os.path.exists(os.path.join(RAIZ, ruta_en)):
        return ["no existe el guion en inglés"]
    es_txt, en_txt = normalizar(leer(ruta_es)).strip(), normalizar(leer(ruta_en)).strip()
    if not en_txt:
        return ["el guion en inglés está vacío"]
    problemas = []
    voz = leer_voz(slug_de(ruta_en))
    if voz not in VOCES_EN:
        problemas.append("sin voz válida en %s/%s.voice (%r): corre --voces" % (AUDIO_EN, slug_de(ruta_en), voz))
    n_es, n_en = len(parrafos(es_txt)), len(parrafos(en_txt))
    if n_es != n_en:
        problemas.append("párrafos: %d en el original, %d en el doblaje" % (n_es, n_en))
    w_es, w_en = len(es_txt.split()), len(en_txt.split())
    if not 0.7 <= w_en / max(w_es, 1) <= 1.25:
        problemas.append("largo: %d palabras para %d del original (¿falta o sobra algo?)" % (w_en, w_es))
    for patron, que in NO_VA_EN_AUDIO:
        vistos = sorted({m.group(0) for m in patron.finditer(en_txt)})
        if vistos:
            problemas.append("%s: %s" % (que, " ".join(repr(v) for v in vistos[:5])))
    for m in RE_NUMERO_ES.finditer(en_txt):
        problemas.append("número con formato español: %r" % m.group(0))
    if es_txt.endswith(CIERRE_ES) and not en_txt.endswith(CIERRE_EN):
        problemas.append("el cierre de las entradas es: %s" % CIERRE_EN)
    return problemas


def claves_de_orden():
    """slug -> clave para ordenar por fecha de publicación (y por número, entre lecturas del mismo día)."""
    claves = {}
    for es, _ in PARES:
        for p in glob.glob(os.path.join(RAIZ, es, "*.md")):
            nombre = os.path.basename(p)
            fm, _ = partes(leer("%s/%s" % (es, nombre)))
            fecha = re.search(r"^date:\s*[\"']?([^\"'\n]+)", fm, re.M)
            fecha = fecha.group(1).strip() if fecha else nombre[:10]
            numero = re.search(r"^numero:\s*(\d+)", fm, re.M)
            claves[slug_de(nombre)] = (fecha[:10], fecha[11:19], int(numero.group(1)) if numero else 0, nombre)
    return claves


def asignar_voces():
    """Da voz a cada guion en inglés que no la tiene, alternando con el anterior por fecha."""
    claves = claves_de_orden()
    slugs = [slug_de(p) for p in glob.glob(os.path.join(RAIZ, AUDIO_EN, "*.txt"))]
    slugs.sort(key=lambda s: claves.get(s, ("9999",)))
    anterior, nuevas = None, 0
    for slug in slugs:
        voz = leer_voz(slug)
        if voz in VOCES_EN:
            anterior = voz
            continue
        voz = VOCES_EN[0] if anterior is None else VOCES_EN[1 - VOCES_EN.index(anterior)]
        with open(os.path.join(RAIZ, AUDIO_EN, slug + ".voice"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(voz + "\n")
        print("voz %-13s %s/%s.txt" % (voz, AUDIO_EN, slug))
        anterior, nuevas = voz, nuevas + 1
    print("%d guiones con voz nueva." % nuevas)


def main():
    ap = argparse.ArgumentParser(description="Estado de la edición en inglés.")
    ap.add_argument("--check", action="store_true", help="código de salida 1 si hay pendientes")
    ap.add_argument("--lista", action="store_true", help="solo las rutas pendientes")
    ap.add_argument("--diff", nargs="*", metavar="RUTA", help="cambios del español desde la traducción")
    ap.add_argument("--sellar", nargs="+", metavar="RUTA", help="guarda el hash del original")
    ap.add_argument("--verificar", nargs="*", metavar="RUTA", help="compara la estructura de cada par")
    ap.add_argument("--voces", action="store_true", help="asigna voz a los guiones en inglés que no la tienen")
    a = ap.parse_args()

    if a.voces:
        asignar_voces()
        return

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
            for p in sorted(glob.glob(os.path.join(RAIZ, AUDIO_EN, "*.txt"))):
                pares.append(par_de("%s/%s" % (AUDIO_EN, os.path.basename(p))))
        con_problemas = 0
        for es, en in pares:
            problemas = verificar_audio(es, en) if es_audio(en) else verificar_par(es, en)
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
    sin_doblar, sin_sellar, doblaje_viejo, doblaje_al_dia = estado_audio()

    if a.diff is not None:
        rutas = [par_de(r) for r in a.diff] or [par_de(r) for r in desactualizadas + doblaje_viejo]
        if not rutas:
            print("No hay traducciones desactualizadas.")
        for es, en in rutas:
            mostrar_diff(es, en)
        return

    if a.lista:
        for r in faltantes + desactualizadas + sin_doblar + sin_sellar + doblaje_viejo:
            print(r)
        return

    print("Edición en inglés: %d al día, %d por traducir, %d desactualizadas."
          % (len(al_dia), len(faltantes), len(desactualizadas)))
    falta_mp3 = sin_mp3(doblaje_al_dia)
    print("Audio en inglés: %d al día, %d por doblar, %d sin sellar, %d desactualizados; %d sin mp3."
          % (len(doblaje_al_dia), len(sin_doblar), len(sin_sellar), len(doblaje_viejo), len(falta_mp3)))
    for titulo, rutas in (("Por traducir", faltantes), ("Desactualizadas (el original cambió)", desactualizadas),
                          ("Huérfanas (sin original en español)", huerfanas),
                          ("Por doblar (guion en español sin versión en inglés)", sin_doblar),
                          ("Doblaje sin sellar (falta --voces, --verificar y --sellar)", sin_sellar),
                          ("Doblaje desactualizado (el guion en español cambió)", doblaje_viejo),
                          ("Sin mp3 al día (lo genera el Action de audio después del push)", falta_mp3)):
        if rutas:
            print("\n%s:" % titulo)
            for r in rutas:
                print("  " + r)
    if a.check and (faltantes or desactualizadas or sin_doblar or sin_sellar or doblaje_viejo):
        sys.exit(1)


if __name__ == "__main__":
    main()
