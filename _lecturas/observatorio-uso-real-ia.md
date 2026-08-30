---
layout: lectura
numero: 19
tags: [datos, gobernanza, seguridad]
title: "Casi la mitad del uso real de IA desaparece cuando se lo mide solo como trabajo"
description: "Un consorcio académico juntó siete fuentes de conversaciones reales con asistentes de IA y las anotó con una misma taxonomía. Al aplicarles el filtro ocupacional del Índice Económico de Anthropic, el 48% de las conversaciones queda descartado, y lo descartado no es ruido: ahí se concentran la salud, los vínculos y buena parte del contenido sensible."
date: 2026-08-24
paper_titulo: "The AI Observatory: A Public Measure of Real-World AI Use"
paper_autores: "Longpre, Reuel, Ki y otros"
paper_publicado: "Preprint, agosto de 2026"
paper_doi: "https://ai-observatory.org"
paper_archivo: "ai_observatory.pdf"
paper_keywords: "real-world AI use, conversation taxonomy, annotation pipeline, occupational filter, measurement sensitivity"
audio: true
---

## La ficha

- **Qué es:** *The AI Observatory: A Public Measure of Real-World AI Use*
- **Quiénes:** diecinueve investigadores de MIT, Stanford, Northeastern, Johns Hopkins, Berkeley, Carnegie Mellon, Brown, NYU, Maryland, Waterloo, EleutherAI, Cohere, Code Metal y Adaption Labs. La primera autoría es compartida entre [Shayne Longpre](https://scholar.google.com/scholar?q=%22Shayne+Longpre%22) (MIT), [Anka Reuel](https://scholar.google.com/scholar?q=%22Anka+Reuel%22) (Stanford) y [Dayeon Ki](https://scholar.google.com/scholar?q=%22Dayeon+Ki%22+Maryland) (Maryland). Entre quienes orientaron el trabajo están [Sandy Pentland](https://scholar.google.com/scholar?q=%22Alex+Pentland%22) (MIT), [Sara Hooker](https://scholar.google.com/scholar?q=%22Sara+Hooker%22) (Adaption Labs) y [Sanmi Koyejo](https://scholar.google.com/scholar?q=%22Sanmi+Koyejo%22) (Stanford).
- **Dónde:** preprint, agosto de 2026. Sin revisión por pares al momento de esta lectura. Taxonomía, anotaciones y herramientas de anotación en [ai-observatory.org](https://ai-observatory.org)
- **Tipo:** estudio de medición. 23.158 conversaciones y 85.633 turnos anotados, provenientes de siete fuentes de uso real recogidas entre abril de 2023 y julio de 2025, clasificados con una taxonomía común de 145 rasgos.

## Primera lectura: qué hace y qué encuentra

Lo primero es entender qué tipo de trabajo es. No mide si la IA sirve ni estima efectos: construye una infraestructura de medición y después la usa para probar qué tan frágiles son las afirmaciones que circulan sobre "para qué se usa la IA". Los autores juntaron siete colecciones de conversaciones reales (WildChat, ShareGPT, AI Archive, un raspado de conversaciones públicas de Grok, LMSYS-Chat-1M, Chatbot Arena y el National Internet Observatory) y las pasaron por una misma taxonomía de 145 rasgos, que etiqueta cada conversación en cuatro niveles: el prompt, la respuesta, el turno y la conversación completa. Esa taxonomía cubre función, tema, usos sensibles, estilo de interacción, dinámica multi-turno y estructura. La anotación la hace un modelo, GPT-4.1, calibrado contra un set de validación humano.

El primer hallazgo es que las fuentes no son intercambiables, y por bastante. En Grok, el 67,1% de las conversaciones incluye búsqueda de información, contra 26,2% en WildChat. ShareGPT se inclina a generación de contenido (63,6%) y AI Archive a análisis de información (53,9%). Los temas se separan igual: Grok concentra noticias y actualidad (38,5%) y negocios y sociedad (64,5%), muy por encima del resto. Y la estructura tampoco coincide: los prompts de WildChat promedian 569,5 tokens frente a un rango de 51,8 a 181,0 en las demás, y las respuestas de Grok promedian 1.322,9 tokens.

Eso importa sobre todo para los riesgos. Los problemas de integridad académica, por ejemplo tareas probablemente copiadas, van de 23,1% en WildChat a 40,4% en AI Archive. La desinformación se concentra en Grok (15,3%, frente a un rango de 4,2% a 10,2% en el resto). Los autores son cuidadosos con la interpretación: como todas las fuentes son de participación voluntaria, no pueden atribuir ninguna diferencia a una causa concreta, sea la plataforma, el modelo o el período. Lo que sí queda establecido es la magnitud. De qué fuente se saquen los datos cambia sustantivamente el retrato del uso.

El segundo hallazgo es el que da el título, y es el más incómodo. El Índice Económico de Anthropic, en su versión de marzo de 2025, primero filtra las conversaciones relevantes para alguna ocupación y recién después mapea las tareas. Los autores reimplementaron ese filtro a partir de los prompts y la taxonomía que Anthropic publicó, y lo corrieron sobre seis de sus siete fuentes: el National Internet Observatory queda afuera porque su acuerdo de datos solo permite sacar anotaciones agregadas acordadas de antemano, así que el pipeline no puede correrse ahí. El 47,9% de las conversaciones queda clasificado como no ocupacional, con un piso de 34,2% en AI Archive y un techo de 61,9% en LMSYS. Después miraron qué es lo que el filtro descarta, manteniendo fija la fuente y la anotación. Lo descartado no es residuo aleatorio: es mucho más probable que involucre salud y relaciones (44,2% contra 31,2%), temas adultos o ilícitos (7,9% contra 2,1%), acoso u odio (27,5% contra 5,6%) y contenido sexual (15,7% contra 2,4%). La conclusión que sacan es de método, no de acusación: el filtro no es un paso neutro de preprocesamiento, y un marco puede parecer completo mientras deja fuera de forma sistemática usos socialmente importantes. Ellos mismos aclaran dos cosas que conviene no saltarse. Ese 47,9% no es una estimación del tráfico de Claude.ai, y las versiones posteriores del Índice ya no aplican el filtro ocupacional y encuentran distribuciones parecidas.

El tercero es que el uso se mueve. Entre abril de 2023 y julio de 2025, dentro de WildChat, los prompts crecieron 1.049,5% en tokens promedio, las respuestas 100,6% y los turnos 17,1%. Y las variantes de un mismo desarrollador sostienen regímenes de uso distintos: intercambios cortos y de plantilla con GPT-3.5, asistencia más larga e iterativa con GPT-4o, y resolución técnica larga de una sola pasada con modelos de razonamiento como o1.

El cuarto mira a las personas y no a los promedios. Entre los usuarios que vuelven a WildChat, la variedad de usos se angosta con el tiempo: las etiquetas de función distintas bajan de 4 a 3 y las de uso sensible de 2 a 1. O sea, la expansión agregada de las conversaciones no viene de que cada usuario escriba más, sino de que cambia quién está usando la herramienta.

## Segunda lectura: desde América Latina

La región no aparece en este trabajo, y los autores lo dicen: entre las limitaciones declaran que las regiones donde predomina el Sur Global siguen mayormente fuera de alcance, aunque estén algo representadas, y proponen como remedio integrar estudios de donación consentida, muestreo regional y agregados del lado de los proveedores. La taxonomía detecta 72 idiomas, pero el paper no reporta ningún corte por lengua en su cuerpo principal.

Aun así, el resultado central se traduce directo. Cuando en la región se discute qué hacer con la IA, las cifras que se citan casi siempre vienen de dos o tres reportes de las propias empresas. Lo que este paper agrega es una advertencia sobre cómo se leen: la elección de la fuente y la elección del filtro no son detalles técnicos, son decisiones que cambian el resultado antes de que empiece el análisis. Una política de IA para el trabajo apoyada en un marco ocupacional no está midiendo mal, está midiendo una parte, y esa parte deja afuera justo lo que le tocaría a salud, educación o protección de datos.

Hay una diferencia de posición que vale marcar, y es mía, no del paper. Estados Unidos y Europa pueden compensar la opacidad de los reportes corporativos con mediciones propias: encuestas, observatorios instrumentados, acceso negociado a datos. Un país mediano de la región casi nunca tiene ninguna de esas tres cosas, así que depende más del reporte ajeno y tiene menos con qué contrastarlo. Lo que este trabajo muestra es que ese contraste no requiere acceso privilegiado a los servidores de nadie: requiere conversaciones donadas con consentimiento, una taxonomía explícita y plata para anotar. El costo total de anotación que reportan es de 5.680 dólares. Para una agencia pública o un centro universitario de la región, ese número no es la barrera.

Queda entonces una pregunta práctica. La taxonomía y las herramientas de anotación están publicadas y son extensibles, y el propio paper reconoce que su cobertura del Sur Global es débil. ¿Quién en la región va a poner las conversaciones en español y en portugués que hoy no están en ningún observatorio?

## La letra chica

- Ninguna de las siete fuentes es representativa del uso de IA. Todas son de participación voluntaria, y los propios autores sospechan que los usos sensibles están subrepresentados, porque la gente no comparte públicamente ese tipo de conversación.
- Las etiquetas las pone un modelo. El acuerdo con el consenso humano tiene una mediana de F1 de 0,856 por categoría madre, y por eso todas las comparaciones del cuerpo se hacen a ese nivel. Los autores señalan que "usos sensibles" es la familia menos estable, y piden leer esas prevalencias como aproximadas.
- El set de validación lo produjeron los mismos autores que diseñaron la taxonomía y eligieron el pipeline. Ellos lo dicen: eso evidencia la fidelidad del pipeline a su propio esquema, no la validez del esquema.
- El análisis temporal y el de perfiles de usuario se apoyan solo en WildChat, la única fuente con marcas de tiempo multianuales e identificadores estables.
- Es un preprint sin revisión por pares. Varios autores tienen afiliación en laboratorios de IA, y el trabajo compara su medición contra un reporte propietario de otro laboratorio; ellos mismos advierten que las diferencias pueden deberse a una mezcla de cambios de producto, de período y de fuente.
