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

Los nombres de la leyenda de `/entradas/` están en `familias:` de `_data/i18n.yml`, en los
dos idiomas: si cambian las familias, hay que actualizarlos ahí.

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

## Estadísticas

Visitas y uso con GoatCounter, sin cookies: el panel está en
`https://dobleclickjg.goatcounter.com`. Todo vive en `_includes/analitica.html`, que
además de contar páginas vistas manda algunos eventos (llegar al final de una entrada,
play al audio, abrir una fuente, filtrar el archivo, enviar un formulario). La lista de
eventos y sus nombres está en el comentario de ese archivo. `/confirmar/` y `/baja/` no
cargan el contador porque llevan el token del suscriptor en la URL.

Para compartir un enlace y saber cuánto tráfico trajo, agrégale
`?utm_source=linkedin&utm_campaign=<nombre>`: el panel lo muestra como origen y campaña.
Para no contar tus propias visitas, abre `/#toggle-goatcounter` una vez en cada navegador.

## Versión en inglés

El sitio es bilingüe. El español es el original y vive donde siempre; el inglés es una
traducción fiel que cuelga de `/en/` (`/en/`, `/en/posts/`, `/en/doble-lectura/`,
`/en/about/`, `/en/sources/`, y sus feeds `/en/feed.xml` y `/en/feed-lecturas.xml`).

- **Contenido.** Cada entrada de `_posts/` tiene su traducción en `_en_posts/` y cada lectura
  de `_lecturas/` en `_en_lecturas/`, **con el mismo nombre de archivo**: eso es lo que las
  empareja. Son colecciones aparte, no un `_posts` más, para que el inglés nunca entre en
  `site.posts` ni en `/feed.xml`, que es el que lee el newsletter.
- **Textos de la interfaz.** Los layouts e includes no escriben texto: lo leen de
  `_data/i18n.yml` (ramas `es:` y `en:`) a través de `_includes/idioma.html`, que cada
  layout incluye al principio. Las páginas de archivo, lecturas y fuentes comparten el
  cuerpo (`_includes/pagina_*.html`) y solo cambia su front matter. Método no: `about.md` y
  `en/about.md` son dos textos, y un cambio en uno hay que llevarlo al otro a mano.
- **Temas.** Las `tags` quedan en español en las dos versiones (deciden color y filtro); el
  sitio las muestra traducidas con `temas:` de `_data/i18n.yml`.
- **Fuentes.** `_data/fuentes.yml` trae los textos en inglés en los campos `_en`. Una
  categoría nueva sin ellos se ve en español en `/en/sources/` hasta que alguien los agregue.
- **Selector e idioma del navegador.** El botón ES/EN del header lleva a la misma página en
  el otro idioma (`_includes/alterno.html` busca la pareja). Al entrar al sitio, si quien lee
  no eligió idioma, se le muestra el que prefiere su navegador; la elección del botón se
  guarda y manda desde ahí. Los buscadores no se redirigen: tienen las etiquetas `hreflang`.
  El detalle está en el comentario de `_layouts/default.html`.
- **Audio.** El inglés es el doblaje del guion en español: `_audio/en/<slug>.txt` y su
  `.voice` hacen el mp3, y quién narra queda en `_data/voces_en.yml`. Se doblan todas las
  Doble Lectura y las entradas desde el 2026-09-27 (`DOBLAJE_DESDE` en
  `_tools/traducciones.py`), alternando Matilda y Eric, voces de fábrica de ElevenLabs. El
  reproductor en inglés busca
  `assets/audio/en/<slug>.mp3` y, mientras no exista, no aparece.
- **Newsletter.** Una sola lista con una columna `idioma`. Quien se suscribe desde `/en/`
  (el formulario manda `lang=en`) recibe la edición en inglés, que sale de `/en/feed.xml` y
  `/en/feed-lecturas.xml` cuando la traducción está publicada; el resto, la española. Cada
  correo trae un enlace para cambiar de idioma. Todo eso vive en el Apps Script del
  newsletter, no en este repo.

### Mantener las traducciones al día

Cada traducción guarda en `hash_original` el hash del español con que se hizo. Así se sabe
qué falta y qué quedó viejo cuando el original cambia (una fe de erratas, una revisión):

```bash
python _tools/traducciones.py            # informe: por traducir, desactualizadas
python _tools/traducciones.py --diff     # qué cambió en el español desde que se tradujo
python _tools/traducciones.py --sellar _en_posts/AAAA-MM-DD-slug.md   # después de traducir
python _tools/traducciones.py --voces    # voz alternada para cada guion en inglés nuevo
python _tools/traducciones.py --sellar _audio/en/slug.txt             # después de doblar
```

El informe trae también el estado del audio en inglés: guiones por doblar, desactualizados
(el guion en español cambió) y doblajes sellados que todavía no tienen mp3. El hash del
guion en español con que se dobló cada uno queda en `_audio/en/sellos.yml`. Al pushear, el
Action de audio regenera el mp3 en inglés cada vez que su guion o su voz cambian.

La guía de estilo de la traducción (glosario, números, monedas, enlaces internos) está en
`_tools/traduccion_en.md`. Una entrada de hoy que todavía no se tradujo simplemente no tiene
versión en inglés: el selector lleva a la portada en inglés y nadie es redirigido a una
página que no existe.

## Correr local (opcional)

```bash
bundle install
bundle exec jekyll serve
# abrir http://localhost:4000/
```
