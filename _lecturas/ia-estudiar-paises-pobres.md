---
layout: lectura
numero: 6
tags: [educación, datos, latam]
title: "Mientras más pobre el país, más se usa la IA para aprender"
description: "Un análisis de 686 mil conversaciones en 227 países encuentra que el uso educativo de la IA sube donde baja el ingreso, al revés de lo que pasó con internet. Y que el inglés se impone como lengua franca de la IA justo donde los idiomas locales funcionan peor en los modelos."
date: 2026-06-16
paper_titulo: "How Early Adopters Used Generative AI Worldwide: Variation by Country Income and Language"
paper_autores: "Daepp y Slaughter"
paper_publicado: "Preprint arXiv, 2026"
paper_doi: "https://doi.org/10.48550/arXiv.2605.30685"
paper_archivo: "daepp-2026-early-adopters-generative-ai-worldwide.pdf"
paper_keywords: ""
audio: true
---

## La ficha

- **Qué es:** *How Early Adopters Used Generative AI Worldwide: Variation by Country Income and Language*
- **Quiénes:** [Madeleine I. G. Daepp](https://www.microsoft.com/en-us/research/people/mdaepp/) (Microsoft Research) e [Isaac Slaughter](https://scholar.google.com/citations?user=lg1C8i8AAAAJ) (University of Washington).
- **Dónde:** preprint en arXiv (cs.CY), mayo de 2026, en formato de conferencia. Aún no pasa por revisión por pares. [doi.org/10.48550/arXiv.2605.30685](https://doi.org/10.48550/arXiv.2605.30685)
- **Tipo:** estudio cuantitativo y descriptivo, sobre 686.722 conversaciones de 54.841 usuarios en 227 países.

## Primera lectura: qué hace y qué encuentra

Conviene partir por el tipo de estudio, porque ordena lo demás. Es un trabajo descriptivo a gran escala. Las autoras y autores tomaron una base de conversaciones anonimizadas y limpias de datos personales de un chatbot gratuito y disponible en casi todo el mundo, Bing Copilot, durante seis meses de 2024 (de abril a septiembre). Para poder comparar países, armaron una muestra estratificada: hasta 250 usuarios por país, hasta 20 conversaciones por usuario, y solo personas con al menos cinco conversaciones, para quedarse con quienes de verdad le encontraron uso a la herramienta y no con quien la probó una vez. No miden si la IA sirve ni evalúan ningún modelo. Describen para qué la usa la gente, según dónde vive y en qué idioma escribe.

Para clasificar el "para qué", construyeron un clasificador apoyado en una taxonomía de la economía laboral que reparte el tiempo de las personas en cinco usos: estudio, trabajo remunerado, producción doméstica, cuidado personal y ocio. Lo validaron contra dos codificadores humanos y reportan un acuerdo moderado, comparable al de trabajos similares. Vale anotar el detalle: el clasificador es un modelo de lenguaje, y lo aplican sobre conversaciones en muchos idiomas. Es el método que tienen para mirar cientos de miles de chats, pero conviene tenerlo presente al leer las cifras.

El primer hallazgo es el que da el título, y va a contramano de lo que pasó con internet. El estudio es el uso más frecuente: en dos tercios de los países (66,7%) es el destino principal de la mayoría de los usuarios. Y mientras más bajo el ingreso del país, más pesa el estudio (una correlación inversa y fuerte, Spearman de -0,64). El trabajo remunerado también sube cuando baja el ingreso. El ocio, en cambio, es lo contrario: crece con la riqueza del país (correlación de 0,69). Dicho simple, en los países más ricos la IA se usa más para entretenerse; en los más pobres, más para aprender y para ganarse la vida. Además, quien usa el chatbot para estudiar tiende a concentrar ahí gran parte de sus conversaciones, más que en cualquier otro uso.

El segundo hallazgo es sobre el idioma. El inglés aparece sobrerrepresentado como lengua de la IA, pero de forma despareja. En Europa y las Américas, la proporción de gente que sabe inglés es mayor que la proporción que efectivamente le escribe en inglés al chatbot; es decir, la gente prefiere su propia lengua cuando puede. En Asia, Oceanía y África pasa al revés: el inglés funciona como lengua franca de la IA mucho más allá de cuánta gente realmente lo domina. ¿Por qué? El estudio lo cruza con qué tan bien rinden los modelos en cada idioma (el benchmark MMLU-ProX). El uso de lenguas distintas del inglés se mantiene plano y muy bajo hasta que un idioma alcanza cierto umbral de rendimiento; recién ahí la gente empieza a usarlo. Las lenguas africanas, que son las que peor puntúan en esa prueba, están prácticamente ausentes del uso. La gente, sugieren los datos, termina escribiendo en inglés cuando su idioma funciona mal en el modelo.

La conclusión que las autoras y autores sacan de juntar las dos cosas es la que da sentido al paper: que esta tecnología termine ampliando la brecha digital o, al revés, permita "saltar etapas" (leapfrogging) podría depender, en buena parte, de qué tan bien rindan los modelos en cada idioma.

## Segunda lectura: desde América Latina

El estudio es global y no separa a América Latina como bloque, así que lo que sigue es lectura mía sobre dónde cae la región en sus mapas, no un hallazgo sobre la región.

La primera noticia es relativamente buena. La parte más dura de la brecha lingüística golpea a las lenguas africanas y a varias asiáticas, no al español ni al portugués, que están entre los idiomas mejor servidos por los modelos. En la dimensión del idioma, entonces, la región parte de una posición cómoda comparada con buena parte del sur global. La segunda noticia es más interesante para pensar política pública. Por su nivel de ingreso, la región se ubica en la franja media, donde según el patrón del estudio el uso educativo y laboral pesa más que el ocio. Si eso se cumpliera acá (y es una extrapolación: el paper no lo midió para estos países), querría decir que mucha gente ya está usando estas herramientas para estudiar y para mejorar su empleabilidad, no solo para entretenerse.

Ahí está la oportunidad de la que hablan las propias autoras y autores, y conviene citarla con cuidado, porque ellas mismas la dejan como posibilidad y no como certeza: si la IA de verdad ayuda a aprender, podría haber un efecto de saltar etapas en los lugares que más lo necesitan. Pero en el mismo respiro advierten el reverso, y es suyo, no mío: para que eso ocurra los modelos tienen que estar diseñados para que la gente aprenda de verdad y no para copiar. El estudio no resuelve cuál de las dos cosas está pasando.

Hay una tercera advertencia que el paper deja anotada y que pega fuerte en la región. Si los modelos rinden peor en seguridad y alineamiento en algunos idiomas, podría abrirse una brecha de "tercer nivel": no ya en quién accede o quién sabe usar la herramienta, sino en quién se lleva los daños. El español está bien cubierto, pero conviene no leer eso como que la región queda fuera del problema: muchas lenguas indígenas no están en ninguna de estas pruebas.

La pregunta que deja sirve para cualquier ministerio de educación de la región. Si lo que más hace la gente con la IA en países como los nuestros es estudiar, ¿estamos tratando estas herramientas como un problema de disciplina (la copia) o como la infraestructura de aprendizaje que, a juzgar por cómo se usan, ya son?

## La letra chica

- Es un estudio descriptivo: muestra correlaciones, no causas. Las autoras y autores son explícitos en que no pueden afirmar por qué aparecen estos patrones, y ofrecen tres explicaciones posibles para el uso educativo (que en los países pobres los primeros en adoptar la IA sean estudiantes, que los usuarios con plata se vayan a otros chatbots de pago, o que de verdad existan necesidades distintas).
- La muestra es estratificada por país, pensada para comparar países, no para retratar el volumen total de uso del mundo. Y mira solo a "early adopters", gente que usó el chatbot al menos cinco veces, no a quien lo probó de pasada.
- Es un solo producto (Bing Copilot) en un momento concreto, 2024. Los modelos han mejorado desde entonces, sobre todo en idiomas, así que los propios autores piden leer estos patrones como una foto de esa época y no como algo fijo.
