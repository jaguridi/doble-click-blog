---
layout: lectura
numero: 30
tags: [participación, datos, latam]
title: "En 119 consultas de Polis, el software también moldeó los grupos"
description: "Con los votos exportados, Gelauff no logró reproducir la agrupación que informó la plataforma. Concluye que el resultado refleja las decisiones de diseño tanto como las de los participantes."
date: 2026-11-02
paper_titulo: "It Takes Three to Converse: Empirical Observations on How the Developer, the Convener and the Participant Shaped 119 Polis Conversations"
paper_autores: "Gelauff"
paper_publicado: "arXiv (preprint), agosto de 2026"
paper_doi: "https://arxiv.org/abs/2608.28368"
paper_archivo: "cola-03-it-takes-three-polis.pdf"
paper_keywords: "consulta ciudadana digital, Polis, agrupamiento de opiniones, moderación de propuestas, innovación democrática"
audio: true
---

## La ficha

- **Qué es:** *It Takes Three to Converse: Empirical Observations on How the Developer, the Convener and the Participant Shaped 119 Polis Conversations*.
- **Quién:** [Lodewijk Gelauff](https://scholar.google.com/scholar?q=%22Lodewijk+Gelauff%22), investigador de Generation Lab y afiliado al Deliberative Democracy Lab de Stanford. Firma solo y aclara que lo hizo a título personal, sin participación de esas organizaciones.
- **Dónde:** [arXiv](https://arxiv.org/abs/2608.28368), 28 de agosto de 2026, de acceso abierto y sin revisión por pares.
- **Tipo:** estudio observacional de datos públicos exportados desde consultas reales, complementado con lectura del código fuente de la plataforma.

## Primera lectura: qué hace y qué encuentra

Polis es un programa de código abierto para consultas asincrónicas: cada participante ve frases cortas, una por una, y marca acuerdo, desacuerdo o pasa; también puede proponer frases propias. Con esos votos, un motor matemático separa a los participantes en grupos de opinión, y ese número de grupos suele encabezar los informes de prensa y de los organizadores.

Gelauff rastreó menciones públicas de estas consultas y descargó los datos que cada una dejaba abiertos. Quiso saber qué parte del resultado decide cada uno de tres actores: quien desarrolló la plataforma, quien convoca y quien participa. Las cifras centrales:

- reunió 271 consultas y analizó a fondo 119, con al menos 100 votantes y casi 6,9 millones de votos;
- en 85 de las 114 que informan cuántos grupos encontró la plataforma, el resultado fue dos;
- al recalcular sobre los votos finales con las mismas reglas, pero sin arrastrar los ciclos anteriores, coincidió con lo informado en 70 de 112 casos, y en las diferencias predominó obtener más grupos (33 veces contra 9);
- con diez votos cada una y en igualdad de condiciones, una frase con solo acuerdos recibe 121 veces más prioridad para ser mostrada que una con solo desacuerdos;
- las frases iniciales de quien convoca lograron mayoría de acuerdo en 70,1% de las frases, contra 84,2% de las escritas por participantes.

El autor atribuye al diseño que los grupos no se puedan reproducir. El motor recalcula en ciclos y cada ciclo parte del estado que dejó el anterior, lo que el autor llama *warm path*. El archivo exportado guarda solo el estado final, así que el camino que llevó hasta ahí se pierde. A eso se suma que el código nunca entrega menos de dos grupos ni más de cinco, y en este corpus el único límite que llegó a restringir el resultado fue el piso de dos.

La ventaja de las frases con acuerdo sale de la fórmula de prioridad que el autor reconstruye desde el código. Quien convoca define las frases de partida, la política de moderación y a quién se invita. Del lado de quien participa, el hallazgo más llamativo es descriptivo: en consultas con pocas frases disponibles, el participante típico respondió casi todas, y en las abiertas, una fracción pequeña. El autor lo plantea como hipótesis, sin causalidad confirmada.

Con estos datos, el número de grupos de un informe de Polis queda como una foto del motor al exportar, condicionada por reglas del código y decisiones de quien organiza. El autor no sostiene que su recálculo sea más correcto, solo que da otro resultado, y por eso recomienda a quien convoca rehacer el análisis con los datos completos al cerrar.

## Segunda lectura: desde América Latina

El paper registra dos proyectos brasileños dentro de la familia Polis. Uno es EJ (*Empurrando Juntas*), una plataforma que reimplementó el método en código propio y funcionó entre 2018 y 2022. El otro es Pentano, que en 2017 reescribió solo la parte matemática. La tabla donde aparece EJ advierte que esas plataformas no corren sobre el motor que el estudio analiza.

Lo que sigue es interpretación de este blog. El piso de dos grupos y el arrastre de un cálculo al siguiente, que hacen irreproducible la agrupación informada, son rasgos del código original. Si una consulta hecha con EJ los hereda o no depende de su propio repositorio matemático, que el paper nombra como ej-math. Revisarlo contra los mismos puntos que Gelauff revisa en el original (rango permitido de grupos, si cada cálculo parte del anterior y cómo se prioriza cada frase) diría cuánto de este diagnóstico se aplica a esas consultas brasileñas. El mismo paper muestra que el asunto no es teórico: a agosto de 2026, dos plataformas de la familia ya no usaban el motor original, y el autor advierte que varios hallazgos podrían ya no aplicarles.

La recomendación principal del paper tiene además un costo práctico. Rehacer el análisis exige a alguien capaz de reagrupar los votos exportados, y el paper avisa de una trampa: la base de datos codifica el acuerdo con un signo y el archivo exportado, con el contrario.

El hallazgo sobre participantes queda como pregunta para la región. Gelauff reconoce que una misma interfaz puede recibirse de manera muy distinta según la cultura. Para saber si una lista corta de frases también lleva a responderlas casi todas, habría que comparar, en consultas latinoamericanas con datos abiertos, la proporción de frases disponibles que cada persona votó en su primera sesión, entre consultas de lista fija y consultas abiertas. Antes de eso falta un inventario: de los países identificados en el corpus, ninguno latinoamericano figura entre los diez con más consultas, y 37 de las 119 no tienen país asignado.

## La letra chica

- Preprint sin revisión por pares; los datos se publicarán con la versión final.
- Hay inconsistencias: el período del corpus figura como 2015 a 2026 en un apartado y como 2017 a 2025 en una tabla, y la mediana de participantes por consulta aparece como 332 y como 118.
- Entre marzo de 2025 y julio de 2026, un error del código volvió uniforme la prioridad de las frases. El autor sugiere que podría servir como experimento natural.
- Es un estudio observacional y varios convocantes se repiten: un solo operador, DEMDIS, de Eslovaquia, aparece en 22 de las 119 consultas.
- El autor declara haber usado Claude Code, de la misma familia de modelos que escribe esta sección, para scripts y borradores de redacción.
- Alcanza para leer con cautela los grupos que informa Polis; no para medir cómo se comporta la ciudadanía.
