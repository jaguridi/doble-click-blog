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

## Diseño: franjas y color por tema

Dos mecanismos distintos que conviene no confundir:

- **Las franjas alternadas** (`--banda`) son las que separan una publicación de la
  siguiente en la portada, el archivo y el índice de lecturas, como en una tabla.
- **El color** (`--tono`) no marca la posición sino el **tema**: capitular, enlaces del
  cuerpo, líneas de los `h2`, caja de audio, fecha y cuadradito del feed.

Encima de todo eso está la marca (`--accent` / `--accent-text`): header, footer, cursor
parpadeante y botón de suscripción, que no cambian nunca.

### Las cuatro familias temáticas

| Color | Familia | Temas |
|---|---|---|
| teja | Gobernanza y política | gobernanza, participación, ética |
| ocre | Mercados e industria | mercados, lanzamientos |
| ciruela | Riesgo y seguridad | seguridad, datos |
| oliva | Sociedad | trabajo, educación, salud, diseño |

El mapa vive en `_data/familias.yml` y lo resuelve `_includes/tono.html`, que toma el
**primer tag de la entrada que esté en ese archivo**. `latam` queda fuera a propósito:
lo llevan todas las entradas, así que no distingue nada y el include sigue de largo al
tag siguiente. Si ningún tag está mapeado, la entrada cae en teja. La routine no tiene
que hacer nada: sale de los `tags` que ya escribe.

Al agregar un tema nuevo a `_data/temas.yml`, conviene agregarlo también a
`_data/familias.yml` (con y sin tilde) para que no caiga en teja por descarte.

La leyenda de `/entradas/` está escrita a mano en ese archivo: si cambian las familias,
hay que actualizarla ahí.

**Doble Lectura** usa el mismo papel y las mismas familias que el diario: es la misma
publicación, y lo que la distingue es el kicker ("Doble Lectura #N"), no el color. Una
lectura de gobernanza y una entrada de gobernanza se ven del mismo color.

Para volver al diseño original (acento único teja, sin franjas):

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
