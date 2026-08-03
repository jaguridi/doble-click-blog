"""Genera _data/voces.yml a partir de los .voice de _audio/.

El sitio muestra quién narra cada audio (`_includes/audio.html`), pero el dato vive
en _audio/<slug>.voice, y Jekyll no lee directorios que empiezan con "_" salvo que
sean colecciones. Este script traduce esos archivos a un _data/voces.yml que Liquid
sí puede consultar como site.data.voces[slug].

OJO con los nombres. Los .voice guardan identificadores estilo edge-tts
("es-CO-SalomeNeural") desde que el audio se hacía con edge-tts. El 2026-08-03 la
generación migró a ElevenLabs (_tools/tts_elevenlabs.py), que mapea cada uno de esos
identificadores a una voz DISTINTA, del mismo género y país pero con otro nombre:

    es-CO-SalomeNeural   -> Virginia          (antes: Salomé)
    es-CL-LorenzoNeural  -> Cristian Cornejo  (antes: Lorenzo)
    es-CO-GonzaloNeural  -> Andrés Jaramillo  (antes: Gonzalo)
    es-CL-CatalinaNeural -> Catalina          (igual)

Así que el nombre a mostrar depende de CUÁNDO se generó el audio, no sólo del .voice.
El corte es la fecha de la entrada: antes de MIGRACION el mp3 se hizo con edge-tts;
desde esa fecha en adelante, con ElevenLabs.

Algunos .voice traen varias voces concatenadas (regeneraciones sucesivas del audio,
escritas una tras otra sin salto de línea). La buena es la última.

Uso:  python _tools/voces_yml.py      (desde la raíz del repo)
"""

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AUDIO = RAIZ / "_audio"
POSTS = RAIZ / "_posts"
LECTURAS = RAIZ / "_lecturas"
SALIDA = RAIZ / "_data" / "voces.yml"

# Primera entrada cuyo audio generó ElevenLabs (workflow .github/workflows/audio.yml).
MIGRACION = "2026-08-03"

EDGE = {
    "es-CO-SalomeNeural": "Salomé (Colombia)",
    "es-CL-LorenzoNeural": "Lorenzo (Chile)",
    "es-CO-GonzaloNeural": "Gonzalo (Colombia)",
    "es-CL-CatalinaNeural": "Catalina (Chile)",
}

ELEVENLABS = {
    "es-CO-SalomeNeural": "Virginia (Colombia)",
    "es-CL-LorenzoNeural": "Cristian (Chile)",
    "es-CO-GonzaloNeural": "Andrés (Colombia)",
    "es-CL-CatalinaNeural": "Catalina (Chile)",
}

PATRON_VOZ = re.compile(r"es-[A-Z]{2}-[A-Za-z]+Neural")
PATRON_FECHA_POST = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
PATRON_FECHA_YAML = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})", re.M)


def fechas_por_slug():
    """slug -> fecha (AAAA-MM-DD), sacada del nombre en _posts o del front matter en _lecturas."""
    fechas = {}
    for archivo in POSTS.glob("*.md"):
        m = PATRON_FECHA_POST.match(archivo.name)
        if m:
            fechas[m.group(2)] = m.group(1)
    for archivo in LECTURAS.glob("*.md"):
        m = PATRON_FECHA_YAML.search(archivo.read_text(encoding="utf-8")[:600])
        if m:
            fechas[archivo.stem] = m.group(1)
    return fechas


def main():
    fechas = fechas_por_slug()
    filas = []
    sin_mapear = set()
    sin_fecha = []

    for archivo in sorted(AUDIO.glob("*.voice")):
        slug = archivo.stem
        encontradas = PATRON_VOZ.findall(archivo.read_text(encoding="utf-8"))
        if not encontradas:
            continue
        voz = encontradas[-1]

        # Sin fecha conocida asumimos el presente, que es ElevenLabs.
        fecha = fechas.get(slug)
        if fecha is None:
            sin_fecha.append(slug)
        tabla = EDGE if (fecha is not None and fecha < MIGRACION) else ELEVENLABS

        nombre = tabla.get(voz)
        if not nombre:
            sin_mapear.add(voz)
            continue
        filas.append((slug, nombre))

    lineas = [
        "# Quién narra el audio de cada entrada — lo muestra _includes/audio.html.",
        "# GENERADO: no editar a mano. Se regenera con `python _tools/voces_yml.py`,",
        "# que lee los .voice de _audio/. Un slug ausente simplemente no muestra la voz.",
        "",
    ]
    lineas += ['%s: "%s"' % (slug, nombre) for slug, nombre in filas]
    SALIDA.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print("%d voces escritas en %s" % (len(filas), SALIDA.relative_to(RAIZ)))
    reparto = {}
    for _, nombre in filas:
        reparto[nombre] = reparto.get(nombre, 0) + 1
    for nombre, n in sorted(reparto.items(), key=lambda x: -x[1]):
        print("   %-22s %d" % (nombre, n))
    if sin_fecha:
        print("Sin fecha (se asumió ElevenLabs): %s" % ", ".join(sin_fecha))
    if sin_mapear:
        print("Voces sin mapear:", ", ".join(sorted(sin_mapear)))


if __name__ == "__main__":
    main()
