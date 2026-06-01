# Doble Click — blog

Blog público diario sobre inteligencia artificial con perspectiva latinoamericana.
Sitio estático con [Jekyll](https://jekyllrb.com/) + tema `minima`, servido por GitHub Pages.

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

- `_config.yml` — configuración del sitio (título, tema, plugins, URL).
- `_posts/AAAA-MM-DD-slug.md` — una entrada por día (las escribe la routine).
- `index.md` — portada (lista de entradas).
- `about.md` — qué es el blog + suscripción.

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

## Nota sobre el post de ejemplo

`_posts/2026-05-25-ia-resuelve-conjetura-erdos.md` es una **muestra ilustrativa** generada a
mano a partir del resumen de ese día, para validar el diseño y el tono. Sus enlaces apuntan a
los dominios oficiales (no a las notas exactas). Las entradas reales las genera la routine con
los links precisos de la curación del día. Se puede borrar cuando empiecen las entradas reales.
