#!/usr/bin/env python3
"""Genera el mp3 del resumen hablado de cada entrada con ElevenLabs.

Reemplaza a edge-tts. Lee _audio/<slug>.txt y la voz de _audio/<slug>.voice
(nombre estilo edge-tts), la mapea a una voz de ElevenLabs (eleven_multilingual_v2)
y deja assets/audio/<slug>.mp3.

El doblaje al inglés sigue el mismo camino desde _audio/en/: <slug>.txt y <slug>.voice
(en-US-female o en-US-male) dejan assets/audio/en/<slug>.mp3. A diferencia del español,
el inglés se regenera solo cuando cambia el guion o la voz: _data/voces_en.yml guarda,
junto a quién narra, el hash del guion con que se hizo cada mp3.

Uso:
  python _tools/tts_elevenlabs.py                       # solo lo que falta, en los dos idiomas (modo CI)
  python _tools/tts_elevenlabs.py --lang en             # solo un idioma (es o en)
  python _tools/tts_elevenlabs.py --force               # regenera TODOS
  python _tools/tts_elevenlabs.py --only slugA slugB    # regenera esos (aunque existan)

La API key se lee de la variable de entorno ELEVENLABS_API_KEY (secret en CI) o,
si no existe, de un archivo local secretElevenlabs.txt (en este repo o en el padre).
"""
import os, sys, json, glob, hashlib, re, urllib.request, urllib.error

MODEL = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"
DEFAULT_VOICE = "es-CL-LorenzoNeural"

# Mapeo voz edge-tts -> voice_id ElevenLabs. Cuarteto: hombre y mujer de CO y CL.
VOICE_MAP = {
    "es-CO-SalomeNeural":   "Tzf8K1T8bC5nay312fzF",  # Virginia          (CO femenina)
    "es-CL-LorenzoNeural":  "ClNifCEVq1smkl4M3aTk",  # Cristian Cornejo  (CL masculino)
    "es-CO-GonzaloNeural":  "aLA88pewYI8sJzecjzX0",  # Andres Jaramillo  (CO masculino)
    "es-CL-CatalinaNeural": "6Gr4AVmTax1pMJO0lHRK",  # Catalina          (CL femenina)
}
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.0, "use_speaker_boost": True}

# Doblaje al inglés: una mujer y un hombre de Estados Unidos, voces de fábrica de ElevenLabs
# (no ocupan cupo de voces). Las claves describen el papel y no la voz, para que cambiar de
# voz no obligue a renombrar los .voice: el nombre que muestra el sitio se anota en
# _data/voces_en.yml al generar cada mp3.
VOICE_MAP_EN = {
    "en-US-female": ("XrExE9yKIg1WjnnlVkGX", "Matilda (United States)"),
    "en-US-male":   ("cjVigY5qzO86Huf0OWal", "Eric (United States)"),
}
VOCES_EN = os.path.join("_data", "voces_en.yml")


def get_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if k:
        return k.strip()
    for p in ("secretElevenlabs.txt", os.path.join("..", "secretElevenlabs.txt")):
        if os.path.exists(p):
            return open(p, encoding="utf-8").read().strip()
    sys.exit("ERROR: falta ELEVENLABS_API_KEY (variable de entorno o secretElevenlabs.txt)")


def read_voice(slug):
    vf = os.path.join("_audio", slug + ".voice")
    if os.path.exists(vf):
        v = open(vf, encoding="utf-8").read().strip()
        if v:
            return v
    return DEFAULT_VOICE


def tts(key, voice_id, text, out_path):
    url = "https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s" % (voice_id, OUTPUT_FORMAT)
    body = json.dumps({"text": text, "model_id": MODEL, "voice_settings": SETTINGS}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
        headers={"xi-api-key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        data = r.read()
    with open(out_path, "wb") as f:
        f.write(data)
    return len(data)


def generar_es(key, force, only):
    os.makedirs(os.path.join("assets", "audio"), exist_ok=True)
    generated = 0
    for txt in sorted(glob.glob(os.path.join("_audio", "*.txt"))):
        slug = os.path.splitext(os.path.basename(txt))[0]
        if only is not None and slug not in only:
            continue
        out = os.path.join("assets", "audio", slug + ".mp3")
        if os.path.exists(out) and not force and only is None:
            continue
        voice = read_voice(slug)
        vid = VOICE_MAP.get(voice)
        if not vid:
            print("  [SKIP] %s: voz desconocida '%s'" % (slug, voice))
            continue
        text = open(txt, encoding="utf-8").read().strip()
        try:
            n = tts(key, vid, text, out)
            generated += 1
            print("  [OK] %-45s | %-22s -> %s | %d bytes" % (slug, voice, vid, n))
        except urllib.error.HTTPError as e:
            print("  [ERR] %s: HTTP %s %s" % (slug, e.code, e.read().decode()[:200]))
            sys.exit(1)
    print("Audios generados (es): %d" % generated)


def leer_voces_en():
    """slug -> {voz, motor, guion} desde _data/voces_en.yml (formato fijo, sin PyYAML)."""
    voces, slug = {}, None
    if not os.path.exists(VOCES_EN):
        return voces
    for linea in open(VOCES_EN, encoding="utf-8"):
        m = re.match(r"^([^#\s][^:]*):\s*$", linea)
        if m:
            slug = m.group(1)
            voces[slug] = {}
            continue
        m = re.match(r'^  (\w+):\s*"(.*)"\s*$', linea)
        if m and slug:
            voces[slug][m.group(1)] = m.group(2)
    return voces


def escribir_voces_en(voces):
    lineas = [
        "# Quién narra el audio en inglés de cada entrada — lo muestra _includes/audio.html.",
        "# GENERADO por _tools/tts_elevenlabs.py cada vez que produce un mp3: no editar a mano.",
        "# `guion` es el hash del guion y la voz con que se hizo el mp3; si cambian, se regenera.",
        "",
    ]
    for slug in sorted(voces):
        v = voces[slug]
        lineas.append("%s:" % slug)
        for campo in ("voz", "motor", "guion"):
            lineas.append('  %s: "%s"' % (campo, v.get(campo, "")))
    with open(VOCES_EN, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas) + "\n")


def generar_en(key, force, only):
    os.makedirs(os.path.join("assets", "audio", "en"), exist_ok=True)
    voces = leer_voces_en()
    generated = 0
    for txt in sorted(glob.glob(os.path.join("_audio", "en", "*.txt"))):
        slug = os.path.splitext(os.path.basename(txt))[0]
        if only is not None and slug not in only:
            continue
        vf = os.path.join("_audio", "en", slug + ".voice")
        voice = open(vf, encoding="utf-8").read().strip() if os.path.exists(vf) else ""
        if voice not in VOICE_MAP_EN:
            # Sin voz no hay default: la alternancia la decide `traducciones.py --voces`.
            print("  [SKIP] en/%s: voz desconocida o ausente '%s'" % (slug, voice))
            continue
        vid, nombre = VOICE_MAP_EN[voice]
        text = open(txt, encoding="utf-8").read().strip()
        guion = hashlib.sha256((voice + "\n" + text).encode("utf-8")).hexdigest()[:12]
        out = os.path.join("assets", "audio", "en", slug + ".mp3")
        al_dia = os.path.exists(out) and voces.get(slug, {}).get("guion") == guion
        if al_dia and not force and only is None:
            continue
        try:
            n = tts(key, vid, text, out)
        except urllib.error.HTTPError as e:
            print("  [ERR] en/%s: HTTP %s %s" % (slug, e.code, e.read().decode()[:200]))
            escribir_voces_en(voces)  # lo ya generado en esta corrida queda anotado
            sys.exit(1)
        voces[slug] = {"voz": nombre, "motor": "ElevenLabs", "guion": guion}
        generated += 1
        print("  [OK] en/%-42s | %-12s -> %s | %d bytes" % (slug, voice, vid, n))
    # El mapa solo nombra audios que existen.
    voces = {s: v for s, v in voces.items()
             if os.path.exists(os.path.join("assets", "audio", "en", s + ".mp3"))}
    escribir_voces_en(voces)
    print("Audios generados (en): %d" % generated)


def main():
    args = sys.argv[1:]
    force = "--force" in args
    lang = None
    if "--lang" in args:
        lang = args[args.index("--lang") + 1]
        if lang not in ("es", "en"):
            sys.exit("ERROR: --lang tiene que ser es o en")
    only = None
    if "--only" in args:
        only = set()
        for a in args[args.index("--only") + 1:]:
            if a.startswith("--"):
                break
            only.add(a)

    key = get_key()
    if lang in (None, "es"):
        generar_es(key, force, only)
    if lang in (None, "en"):
        generar_en(key, force, only)


if __name__ == "__main__":
    main()
