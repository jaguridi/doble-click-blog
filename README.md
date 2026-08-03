# Doble Click — blog

Blog público diario sobre inteligencia artificial con perspectiva latinoamericana.
Sitio estático con [Jekyll](https://jekyllrb.com/) y diseño propio (sin tema externo; los layouts viven en `_layouts/`), servido por GitHub Pages.

Este repositorio contiene **solo contenido público**. El material interno de curación
(arcos, candidatos del podcast, metodología, métricas) vive en un repo privado aparte y
**no se publica acá**.

## Cómo se publica

1. La routine diaria de noticias (privada) genera el `resumen.md` del día.
2. La routine **`blog-diario`** lee ese resumen, lo reescribe en tono de blog público
   (sin la mecánica interna del podcast) y escribe un archivo en `_posts/`.
3. Al hacer merge a `main`, GitHub Pages reconstruye el sitio automáticamente y actualiza
   el RSS (`/feed.xml`).
4. Un Google Apps Script lee la entrada nueva y la envía como newsletter a los suscriptores.

No hay que tocar nada a mano en el día a día.

## Estructura

- `_config.yml` — configuración del sitio (título, plugins, URL, endpoint del newsletter).
- `_posts/AAAA-MM-DD-slug.md` — una entrada por día (las escribe la routine).
- `index.md` — portada (lista de entradas).
- `about.md` — qué es el blog + suscripción.

## Diseño: el tono de cada entrada

Cada entrada del blog diario tiene su propio color, para que dos publicaciones seguidas
no se vean idénticas en la portada. Hay dos capas de color y conviene no mezclarlas:

- **`--accent` / `--accent-text`** — la marca: header, footer, cursor parpadeante, botón
  de suscripción. No cambia nunca.
- **`--tono`** — la entrada: capitular, enlaces del cuerpo, líneas de los `h2`, caja de
  audio y el cuadradito del feed. Rota entre cuatro colores (teja, ocre, oliva, ciruela).

El tono sale de la **fecha**, no de la posición en la lista: `(día del año × 3) módulo 4`,
en `_includes/tono.html`. Como 3 y 4 son coprimos, dos entradas de días seguidos nunca
comparten tono, y el color de la portada es siempre el mismo que el de la entrada abierta
y el del archivo. La routine no tiene que hacer nada: el cálculo es automático.

**Doble Lectura** no rota: usa tinta fijo y un papel más frío (`.seccion-lectura`), para
que se distinga del diario de un vistazo.

Para volver al diseño anterior (acento único teja, sin modo oscuro):

```bash
git checkout diseno-v1
```

## Quién narra cada audio

`_includes/audio.html` muestra la voz debajo del reproductor, leyéndola de
`_data/voces.yml`. Ese archivo lo genera `_tools/voces_yml.py` a partir de los
`_audio/<slug>.voice` (Jekyll no entra a los directorios que empiezan con `_`), y el
workflow de audio lo regenera solo cada vez que produce un mp3. Para correrlo a mano:

```bash
python _tools/voces_yml.py
```

Si un slug no está en el mapa, simplemente no se muestra la voz.

**Cuidado con los nombres:** los `.voice` guardan identificadores estilo edge-tts
(`es-CO-SalomeNeural`), pero desde el 2026-08-03 el audio lo genera ElevenLabs, que usa
voces distintas —mismo género y país, otro nombre— para esos mismos identificadores
(Salomé → Virginia, Lorenzo → Cristian, Gonzalo → Andrés). El script decide qué nombre
mostrar según la fecha de la entrada; la constante `MIGRACION` marca el corte.

## Dominio y GitHub Pages

El sitio se sirve en el subdominio **`dobleclick.jaguridi.cl`** (definido en el archivo `CNAME`),
con GitHub Pages detrás. Requiere en el DNS de `jaguridi.cl` un registro:

```
CNAME   dobleclick   →   jaguridi.github.io
```

En GitHub: Settings → Pages → Source `Deploy from a branch`, branch `main`, carpeta `/ (root)`,
Custom domain `dobleclick.jaguridi.cl`, y "Enforce HTTPS" una vez emitido el certificado.

## Correr local (opcional)

```bash
bundle install
bundle exec jekyll serve
# abrir http://localhost:4000/
```
