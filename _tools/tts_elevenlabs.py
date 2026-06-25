#!/usr/bin/env python3
"""Genera el mp3 del resumen hablado de cada entrada con ElevenLabs.

Reemplaza a edge-tts. Lee _audio/<slug>.txt y la voz de _audio/<slug>.voice
(nombre estilo edge-tts), la mapea a una voz de ElevenLabs (eleven_multilingual_v2)
y deja assets/audio/<slug>.mp3.

Uso:
  python _tools/tts_elevenlabs.py                       # solo los mp3 que faltan (modo CI)
  python _tools/tts_elevenlabs.py --force               # regenera TODOS
  python _tools/tts_elevenlabs.py --only slugA slugB    # regenera esos (aunque existan)

La API key se lee de la variable de entorno ELEVENLABS_API_KEY (secret en CI) o,
si no existe, de un archivo local secretElevenlabs.txt (en este repo o en el padre).
"""
import os, sys, json, glob, urllib.request, urllib.error

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


def main():
    args = sys.argv[1:]
    force = "--force" in args
    only = None
    if "--only" in args:
        only = set(args[args.index("--only") + 1:])

    key = get_key()
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
    print("Audios generados: %d" % generated)


if __name__ == "__main__":
    main()
