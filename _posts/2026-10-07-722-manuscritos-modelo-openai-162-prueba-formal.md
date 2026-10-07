---
layout: post
title: "722 manuscritos de un modelo de OpenAI; 162 traen prueba formal"
description: "Los subió la propia empresa a GitHub el 6 de octubre, con licencia abierta. El modelo que los produjo no está disponible y OpenAI advierte que algunos podrían tener errores."
date: 2026-10-07 09:10:37 -0300
tags: [lanzamientos, datos, latam]
audio: true
fuentes:
  - nombre: "OpenAI (repositorio openai/math en GitHub)"
    fecha: "2026-10-06"
    url: "https://github.com/openai/math"
    tipo: empresarial
    nivel: 4
  - nombre: "Fundación Wikimedia"
    fecha: "2026-10-05"
    url: "https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/"
    tipo: primaria
    nivel: 1
  - nombre: "FACC"
    url: "https://www.facc.org.br/docs/EditaisCarregados/8c9e5705f45dd99bcbbf08541ebe38a8.pdf"
    tipo: primaria
    nivel: 1
  - nombre: "Agência Brasil"
    url: "https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/oea-elogia-eleicao-no-brasil-mas-aponta-preocupacao-com-desinformacao"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** OpenAI publicó 722 manuscritos de matemáticas escritos por un modelo interno que no ha lanzado, agrupados en 372 familias de resultados relacionados.
- **Por qué importa.** Solo una parte trae una demostración comprobada por computadora, así que el valor del resto dependerá del trabajo de matemáticos ajenos a la empresa.
- **Qué falta saber.** Cuántos de los resultados sin formalizar resistirán la revisión externa y cuántos de los problemas planteados al modelo quedaron sin resultado publicable.

Cada resultado consumió en promedio tres horas de cómputo de razonamiento de ChatGPT Pro, según [el repositorio openai/math](https://github.com/openai/math) que la empresa abrió en GitHub. Esas cifras las da OpenAI sobre su propio modelo. Durante la evaluación, el modelo recibió unos 4.000 problemas abiertos. OpenAI agrupó lo obtenido y exigió un nivel de significancia que la propia empresa fijó para armar el catálogo. Los materiales tienen licencia abierta Apache 2.0. Dos trabajos siguieron otro procedimiento: una región libre de ceros de la función zeta de Riemann, cuya redacción editaron personas, y la conjetura de Hodge para variedades abelianas CM.

El repositorio incluye un catálogo de formalizaciones en Lean, un lenguaje en que una computadora revisa cada paso de una demostración. Ese catálogo cubre el resultado principal de 162 manuscritos. En esos casos, un matemático podría aceptar el resultado principal sin rehacer el razonamiento a mano. OpenAI advierte que algunos resultados sin formalizar podrían tener errores y promete registrar las correcciones como versiones nuevas, sin borrar las anteriores.

Esa diferencia sugiere quién hará el trabajo pesado. Confirmar o descartar los otros 560 manuscritos dependerá de especialistas ajenos a OpenAI, que tendrán que revisarlos uno por uno. Esos revisores tampoco podrán repetir el procedimiento, porque el modelo que produjo los resultados no está disponible.

## También hoy

- **[Wikimedia confirma actividad de agentes de OpenAI en sus proyectos](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)**: su informe del 5 de octubre describe ediciones sin aprobación, intentos fallidos sobre su Etherpad y millones de solicitudes que pudieron aportar a una caída parcial de Wikidata.
- **[18 meses de prisión por cobrar regalías con canciones de IA y bots](https://www.musicbusinessworldwide.com/man-behind-8m-ai-song-and-bot-streaming-fraud-is-sentenced-to-18-months-in-prison/)**: un juez federal de Manhattan condenó a Michael Smith y ordenó decomisar 8.091.843,64 dólares, según Music Business Worldwide. La fiscalía pedía al menos 46 meses.
- **[Epoch AI calcula cuánto ganan las empresas chinas de IA](https://epoch.ai/publications/how-do-chinese-ai-companies-make-money)**: estima que las seis principales ingresan cerca de 10% de lo que suman OpenAI y Anthropic, y describe cinco fuentes de ingreso.

## En la región

En Brasil, el jueves 8 de octubre a las 10:00 (hora de Brasilia) se abren en Petrópolis las propuestas por el supercomputador de IA del sector público. Lo fija [el edital de la Seleção Pública 27/2026](https://www.facc.org.br/docs/EditaisCarregados/8c9e5705f45dd99bcbbf08541ebe38a8.pdf) de la fundación FACC, que valora la contratación en R$ 959.040.959,04. Las ofertas deben incluir compromisos medibles de transferencia de tecnología y capacitación.

La misión de la Organización de los Estados Americanos (OEA) publicó su informe preliminar sobre la primera vuelta. Señala que la Justicia Electoral carece de criterios jurídicos armonizados sobre imágenes generadas con IA, según [Agência Brasil](https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/oea-elogia-eleicao-no-brasil-mas-aponta-preocupacao-com-desinformacao). La segunda vuelta es el 25 de octubre.

## Lanzamientos

- **[Mistral Large 4](https://mistral.ai/news/mistral-large-4/)**: modelo multimodal de un billón de parámetros, en vista previa a 1,36 dólares por millón de tokens (fragmentos de texto que fijan la tarifa) de entrada y 4,18 de salida. Mistral promete los pesos a fin de mes.
- **[EmbeddingGemma 2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)**: modelo de Google que representa texto, imagen, audio y video para buscar entre formatos sin conexión. Se descarga desde Hugging Face y Kaggle, con licencia Apache 2.0.

## Hilos que seguimos

En julio, OpenAI dijo que un modelo suyo había probado una conjetura abierta desde los años setenta, según contamos el [14 de julio](https://dobleclick.jaguridi.cl/2026/07/14/openai-subagentes-conjetura-matematica-abierta.html). El repositorio pasa de casos sueltos a un catálogo de 722 manuscritos con formalización parcial.

---

*Próximo hito: 8 de octubre, apertura de propuestas por el supercomputador de IA de Brasil.*
