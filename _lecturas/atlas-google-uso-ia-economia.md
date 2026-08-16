---
layout: lectura
numero: 17
tags: [trabajo, mercados, latam]
title: "La IA ya llegó a casi todos los oficios, pero apenas cubre una quinta parte de sus tareas"
description: "Google mapeó 15 millones de conversaciones con Gemini contra las taxonomías oficiales de ocupaciones y tareas de Estados Unidos. La adopción alcanza al 68% de las ocupaciones, pero en la ocupación mediana llega al 21% de sus tareas, y menos del 10% del uso en trabajo cognitivo no rutinario busca que la IA haga la tarea completa."
date: 2026-08-10
paper_titulo: "Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy"
paper_autores: "Iscenko, Strand y otros"
paper_publicado: "Google, julio 2026"
paper_doi: "https://doi.org/10.48550/arXiv.2608.00038"
paper_archivo: "google-2026-atlas-gemini-usage-economy.pdf"
paper_keywords: "artificial intelligence, technological change, technology adoption, labor demand, productivity, household production, time use, global diffusion"
audio: true
---

## La ficha

- **Qué es:** *Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy*, primera entrega de una iniciativa de investigación económica de Google sobre sus propios registros de uso.
- **Quiénes:** dieciocho personas de Google y Google DeepMind. La correspondencia queda a nombre de [Zanna Iscenko](https://scholar.google.com/scholar?q=%22Zanna+Iscenko%22) y [Scott Strand](https://scholar.google.com/scholar?q=%22Scott+Strand%22+Google). Los agradecimientos consignan contribuciones, orientación y revisión de Diane Coyle (Universidad de Cambridge) y David Autor (MIT).
- **Dónde:** publicado por Google el 23 de julio de 2026 y depositado como preprint en arXiv. Sin revisión por pares: es un reporte de la propia empresa sobre su propio producto. [doi.org/10.48550/arXiv.2608.00038](https://doi.org/10.48550/arXiv.2608.00038)
- **Tipo:** estudio observacional. 14.653.926 interacciones desidentificadas entre el 6 y el 19 de abril de 2026, en la app de Gemini, el Modo IA de Google y la API de Gemini, clasificadas y mapeadas de forma automática a taxonomías estadísticas oficiales de Estados Unidos.

## Primera lectura: qué hace y qué encuentra

Conviene partir por qué tipo de trabajo es esto. No es un experimento ni una estimación causal: es un ejercicio de medición. Los autores resumen conversaciones reales con Gemini, las agrupan en clusters y mapean cada grupo contra tres marcos que ya existían: la clasificación de ocupaciones de la Oficina de Estadísticas Laborales de Estados Unidos, el catálogo de tareas O*NET y la encuesta de uso del tiempo ATUS. La gracia del diseño está ahí, en pegar el uso de IA a las mismas categorías con que se mide la economía.

Los dos primeros hallazgos hay que leerlos juntos, porque el segundo corrige al primero. La IA aparece en el 68% de las ocupaciones, que concentran algo más del 88% del empleo estadounidense, y no solo en las de siempre: junto a desarrolladores y analistas de mercado aparecen agricultores, ingenieros industriales e ingenieros forestales. Pero la penetración es ancha y delgada. En la ocupación mediana con algo de uso, la IA cubre el 21% de las tareas que componen ese oficio, y solo un 3% de las ocupaciones supera los tres cuartos.

El tercero es sobre qué se le pide a la herramienta. Las tareas cognitivas no rutinarias, esas que la literatura clásica consideraba complementarias a la tecnología y no sustituibles, son cerca del 35% de las tareas de la economía y casi el 65% de las interacciones de trabajo en estos datos. Pero un clasificador de intención muestra que ese uso se concentra en generar borradores parciales, revisar y afinar, discutir ideas y buscar información. Que la IA ejecute la tarea completa de punta a punta aparece en menos del 10% de esas conversaciones; en el trabajo cognitivo rutinario, en cambio, más de un cuarto apunta a automatizar. Los autores marcan que este clasificador es preliminar.

Dos hallazgos más, en direcciones opuestas. La IA también aparece en el trabajo manual: en varios oficios técnicos funciona como acompañante de diagnóstico, y ahí el uso con imágenes y video más que duplica la línea base del resto del trabajo. Al mismo tiempo, el uso escala con el sueldo: un 1% más de ingreso mediano en una ocupación se asocia a más de un 2,5% más de intensidad de uso, y la relación sobrevive al controlar por nivel educativo.

Fuera del trabajo pasa lo que casi nadie mide: más del 86% del uso conversacional, el que no pasa por la API, ocurre ahí, y se concentran en trámites de alta fricción. Las consultas sobre servicios de gobierno y obligaciones cívicas están sobrerrepresentadas por un factor cercano a veinte respecto del tiempo que la gente les dedica, y casi la mitad de las consultas médicas, legales, financieras y de gobierno ocurren fuera del horario hábil. La imagen que proponen es la de una oficina pública abierta de noche y los fines de semana. Sobre eso estiman el valor que el PIB no captura: entre 15 y 149 mil millones de dólares anuales solo en Estados Unidos, según supuestos de ahorro de tiempo entre 0,5% y 5%. Es una cuenta hipotética y lo dicen con todas sus letras.

## Segunda lectura: desde América Latina

Lo primero es que la región aparece, y aparece bien. La adopción por habitante sigue de cerca la riqueza nacional, con una elasticidad cercana a 0,9, pero Chile, Perú, Brasil, Argentina y Colombia se ubican en los quintiles alto y muy alto de uso conversacional, junto a países bastante más ricos. Los autores lo atribuyen en parte al uso extendido de dispositivos digitales y dejan abierta la pregunta de por qué algunos países de ingreso medio se salen de la línea.

Lo segundo es más incómodo. Cuando el uso laboral se mide como porcentaje de las conversaciones totales de cada país, y no en volumen por habitante, el ranking se da vuelta: Estados Unidos y la Unión Europea caen a los quintiles bajos, África salta al más alto y Sudamérica se mantiene arriba. Los autores ofrecen la lectura entusiasta, profesionales de economías en desarrollo usando la IA para sortear restricciones que en otros lados no existen, pero la contrapesan de inmediato. Donde los datos móviles se pagan por megabyte el uso digital tiende a ser más dirigido a un fin, así que hay menos conversación casual diluyendo el denominador. Y el conjunto de datos no incluye las cuentas empresariales de Gemini: si esas suscripciones corporativas son más habituales en Norteamérica y Europa, como plantean los autores, el uso profesional de esos países queda subestimado.

Lo tercero es una buena noticia bien fundada, y tiene que ver con el idioma. El español es la segunda lengua del conjunto de datos, con 12% de las conversaciones, detrás de un inglés que solo llega a un tercio; el portugués ronda el 6%. Y la hipótesis de que la gente se cambia al inglés para lo importante no se sostiene: el uso de una lengua no primaria es del 26% en actividades de trabajo y de casi 24% fuera del trabajo. Eso sí, esas conversaciones salen más caras, entre 9% y 12% más turnos y entre 18% y 20% más tokens, así que los autores concluyen que invertir en calidad multilingüe rinde también en eficiencia.

Lo cuarto es la advertencia: usar IA no es lo mismo que construir con IA. El mapa de la API está todavía más concentrado en países de ingreso alto, porque integrar una API exige ingeniería, infraestructura y capital, se paga por token, y los idiomas fuera del alfabeto occidental consumen más tokens por palabra. Ahí conviene ser fiel a lo que el reporte declara: los países del quintil más bajo de uso conversacional concentran el 17% de la población mundial y generan el 2% de las conversaciones, y los autores aclaran de forma explícita que ATLAS v1.0 no permite pronunciarse sobre si la IA profundiza esa brecha.

La pregunta que queda para la región es cuál de las dos historias es la verdadera: si el alto uso laboral que muestran estos datos es un multiplicador de productividad, o el efecto óptico de un uso más escaso y más obligado. Esa distinción vale mucho para cualquier política pública, y con estos datos no se puede hacer.

## La letra chica

- Es un reporte de Google sobre el uso de Gemini, publicado por Google y sin revisión por pares: evidencia interna con acceso a datos que nadie más tiene, no una auditoría independiente. La revisión externa de Coyle y Autor ayuda, pero no cambia la naturaleza del documento.
- Mide comportamiento, no resultados. Que una conversación termine no significa que la persona haya logrado su objetivo ni ahorrado tiempo. Es la segunda limitación que declaran, después de la falta de datos empresariales.
- Falta buena parte del uso profesional: no incluye la API pagada ni el uso empresarial vía Google Cloud, ni Workspace, Translate, AI Overviews o programación agéntica.
- Las clasificaciones son probabilísticas y los clasificadores de intención y experticia son preliminares. La cifra de valor doméstico depende de un ahorro de tiempo supuesto, no medido. Todo es una foto de dos semanas de abril de 2026.
