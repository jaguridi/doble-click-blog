# Guía de traducción al inglés — Doble Click y Doble Lectura

La versión en inglés del sitio es una **traducción fiel** del español, que es el original.
Esta guía la siguen quien traduce por primera vez una entrada o una lectura y quien actualiza
una traducción porque el original cambió (una fe de erratas, una corrección de la revisión).

## Dónde va cada archivo

| Original | Traducción |
|---|---|
| `_posts/AAAA-MM-DD-slug.md` | `_en_posts/AAAA-MM-DD-slug.md` |
| `_lecturas/slug.md` | `_en_lecturas/slug.md` |

**El nombre del archivo es idéntico**, slug en español incluido. Es lo que empareja las dos
versiones: el selector de idioma, las etiquetas `hreflang` y `_tools/traducciones.py`
dependen de eso. No inventes un slug en inglés.

## Front matter

Copia el front matter completo del original, en el mismo orden, y cambia solo esto:

- `title` y `description`: tradúcelos. Los títulos van en **mayúscula inicial solamente**
  (sentence case), igual que en español: "Uruguay begins discussing OECD membership at an AI
  summit", no "Uruguay Begins Discussing…".
- `fuentes[].nombre`: traduce solo lo descriptivo. "AI Security Institute (Reino Unido)" →
  "AI Security Institute (UK)"; "Ministerio de Economía y Finanzas de Uruguay" → "Uruguay's
  Ministry of Economy and Finance". Los nombres de medios no se tocan: "Ámbito", "La Crónica
  de Hoy", "Poder360".
- En las lecturas, `paper_autores` ("y" → "and") y `paper_publicado` (meses en inglés:
  "marzo 2026" → "March 2026"; "Nota Técnica" → "Technical Note"). `paper_titulo` se deja
  **tal cual**: es el título original del documento. `paper_keywords` también se deja tal
  cual, salvo que esté en español.

No toques `layout`, `date`, `tags`, `audio`, `numero`, `paper_doi`, `paper_archivo`, `url`,
`tipo`, `nivel` ni `fecha`. **Las `tags` quedan en español** (`gobernanza`, `seguridad`…):
son claves internas que deciden el color y el filtro, y el sitio las muestra traducidas.

No agregues `hash_original`: lo escribe `python _tools/traducciones.py --sellar` después.

Las cadenas del YAML van entre comillas dobles, como en el original. Si el texto lleva
comillas dobles adentro, usa comillas simples para la cita interior o escápalas con `\"`.

## Cuerpo

**Traduce todo, no resumas ni agregues.** Cada párrafo, viñeta, nota y fe de erratas del
original tiene su equivalente, en el mismo orden y con el mismo Markdown y HTML (`<small>`,
negritas, cursivas, listas, `---`). No hay notas del traductor.

**No corrijas el contenido.** Si una cifra o un dato te parece dudoso, tradúcelo igual: las
correcciones se hacen en el original y después se propagan. La traducción no puede decir
algo que el español no dice.

**Inglés estadounidense, claro y sobrio.** Mismo registro que el original: periodístico,
para un público general informado, sin jerga ni tono de venta. Frases directas; si una frase
en español es larga, en inglés puede partirse en dos, sin perder nada.

**Primera persona plural** donde el original la usa ("seguimos", "revisamos" → "we").

### Enlaces

- Las URLs externas **no se tocan**. Solo se traduce el texto del enlace.
- Los enlaces internos se pasan a su versión en inglés:
  - `https://dobleclick.jaguridi.cl/2026/08/08/slug.html` → `https://dobleclick.jaguridi.cl/en/2026/08/08/slug.html`
  - `/doble-lectura/slug/` → `/en/doble-lectura/slug/`
  - `/entradas/` → `/en/posts/` · `/about/` → `/en/about/` · `/fuentes/` → `/en/sources/`

### Nombres propios

- **Doble Click** y **Doble Lectura** son marcas: no se traducen ("Doble Lectura #19").
- Instituciones: usa el nombre oficial en inglés cuando existe y es de uso común (OCDE →
  OECD, ONU → UN, BID → IDB, CEPAL → ECLAC, Unión Europea → European Union). Si no existe,
  traduce de forma descriptiva y conserva la sigla original: "Tribunal Superior Electoral
  (TSE)" → "Superior Electoral Court (TSE)"; "Cámara de Diputados de Brasil" → "Brazil's
  Chamber of Deputies". Los nombres de proyectos de ley se conservan ("PL 2338").
- "América Latina" / "Latinoamérica" → "Latin America"; "la región" → "the region";
  "latinoamericano" → "Latin American"; "el Sur Global" → "the Global South".
- Citas textuales: tradúcelas y mantenlas entre comillas. Si el original atribuye la cita a
  un medio ("según Ámbito"), la atribución se conserva.

### Números, monedas y fechas

Aquí es donde más fácil se cuela un error. Revísalos uno por uno.

| Español | Inglés |
|---|---|
| `12,2%` | `12.2%` |
| `6.000` | `6,000` |
| `30.000 millones de dólares` | `$30 billion` |
| `900.000 millones` | `900 billion` |
| `1,4 billones de dólares` | `$1.4 trillion` (**billón = 10¹², trillion**) |
| `mil millones` | `billion` |
| `19 puntos porcentuales` | `19 percentage points` |
| `200 reales` · `50 millones de pesos chilenos` | `200 reais` · `50 million Chilean pesos` |
| `29 de septiembre` | `September 29` |
| `28 de septiembre de 2026` | `September 28, 2026` |
| `el lunes 4 de octubre` | `Monday, October 4` |

Los dólares sin más especificación son estadounidenses: `$`. Otras monedas se nombran.

### Glosario fijo

Los encabezados y rótulos que se repiten se traducen siempre igual:

| Español | Inglés |
|---|---|
| `## En 60 segundos` | `## In 60 seconds` |
| `**Qué pasó.**` | `**What happened.**` |
| `**Por qué importa.**` | `**Why it matters.**` |
| `**Qué falta saber.**` | `**What we don't know yet.**` |
| `## También hoy` | `## Also today` |
| `## En la región` | `## In the region` |
| `## Lanzamientos` | `## Launches` |
| `## Hilos que seguimos` | `## Threads we're following` |
| `*Próximo hito: …*` | `*Next milestone: …*` |
| `## La ficha` | `## At a glance` |
| `**Qué es:**` · `**Quiénes:**` · `**Dónde:**` · `**Tipo:**` | `**What it is:**` · `**Who:**` · `**Where:**` · `**Type:**` |
| `## Primera lectura: qué hace y qué encuentra` | `## First reading: what it does and what it finds` |
| `## Segunda lectura: desde América Latina` | `## Second reading: from Latin America` |
| `## La letra chica` | `## The fine print` |
| `**Fe de erratas (28 de septiembre de 2026).**` | `**Correction (September 28, 2026).**` |
| `**Sobre esta entrada.**` | `**About this entry.**` |
| gobernanza · seguridad (de IA) · pesos abiertos | governance · safety · open weights |
| modelo de frontera · laboratorio · despliegue | frontier model · lab · deployment |
| cómputo · centro de datos · licitación | compute · data center · procurement / tender |

El párrafo fijo de las entradas antiguas se traduce así:

> `<small>**About this entry.** It is generated automatically from public sources, without human review before publication. It may contain errors of interpretation or summary; please check each story against its original source (the links lead there) before citing it or making decisions based on it.</small>`

## Actualizar una traducción existente

Cuando el original cambió, `python _tools/traducciones.py --diff` muestra qué cambió en el
español desde la versión que se tradujo. Aplica **el mismo cambio** en el inglés y deja el
resto como está: no retradúzcas el archivo entero, porque cambiaría frases que nadie tocó.
Si no hay forma de saber qué cambió (el diff no está disponible), retraduce el archivo
completo.

## Al terminar

```bash
python _tools/traducciones.py --sellar _en_posts/AAAA-MM-DD-slug.md   # o varias rutas
python _tools/traducciones.py                                          # debe quedar al día
```

`--sellar` guarda en el front matter del inglés el hash del original con que se tradujo.
Solo se sella lo que de verdad quedó al día con el español.
