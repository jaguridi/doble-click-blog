---
layout: lectura
numero: 32
tags: [trabajo, datos, latam]
title: "El uso laboral de Claude se asocia con más dirección humana previa"
description: "Con datos del Anthropic Economic Index, Fábrega estima que las tareas con más uso laboral muestran más rastros de instrucciones y criterios fijados antes de delegar, tanto en la API como en Claude.ai."
date: 2026-11-09
paper_titulo: "Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use"
paper_autores: "Fábrega"
paper_publicado: "arXiv (preprint), agosto de 2026"
paper_doi: "https://arxiv.org/abs/2608.17624"
paper_archivo: "cola-05-governing-delegation-fabrega.pdf"
paper_keywords: "generative artificial intelligence; AI governance; delegation; 1P API; Claude.ai; compositional data; human-AI collaboration"
audio: true
---

## La ficha

- **Qué es:** *Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use*.
- **Quién:** [Jorge Fábrega](https://scholar.google.com/scholar?q=%22Jorge+F%C3%A1brega%22), del CICS-UDD, en Chile. Firma solo.
- **Dónde:** [arXiv](https://arxiv.org/abs/2608.17624), 18 de agosto de 2026, de acceso abierto. Es un preprint y no indica revisión por pares.
- **Tipo:** análisis cuantitativo observacional de datos públicos y agregados. Los datos cubren abril y mayo de 2026, así que reflejan el uso de los modelos Claude disponibles en esos meses.

## Primera lectura: qué hace y qué encuentra

Que una IA ejecute buena parte de una tarea no dice quién la dirige. Fábrega separa dos rutas por las que una persona la conserva. En la delegación especificada, la fija antes de ejecutar, con instrucciones, restricciones o criterios. En la coproducción iterativa, la ejerce durante la producción, corrigiendo o redirigiendo resultados provisionales. Su hipótesis es que el uso laboral, donde un producto deficiente tiene costos profesionales, aumenta el valor de conservarla.

Para ponerla a prueba usa la versión pública del Anthropic Economic Index, que la empresa liberó el 26 de junio de 2026. Sus unidades no son personas ni conversaciones, sino celdas mensuales por tarea de la clasificación ocupacional O\*NET, en dos vías: la API directa de Anthropic (1P API) y Claude.ai, que reúne Chat y Cowork.

Con seis métricas, el autor arma un perfil para cada ruta, en escala de 0 a 100. El de delegación especificada combina la proporción de ejecución dirigida, una autonomía menor del sistema, instrucciones más elaboradas y tareas que una persona competente podría hacer sin IA. Al ser una media geométrica, un componente alto no compensa la ausencia de otro.

El ejercicio central compara, para una misma celda, el perfil esperado con su composición observada y con otra que traslada diez puntos porcentuales del uso personal al laboral. Las cifras:

- la delegación especificada sube 2,76 puntos en la API (intervalo de 95%: 2,30 a 3,22) y 1,45 en Claude.ai (0,93 a 1,97);
- en 1.411 pares de tarea y mes presentes en ambas vías, la coproducción iterativa cambia -0,30 en la API y 0,15 en Claude.ai, con intervalos que incluyen el cero;
- la diferencia entre ambas vías en ese cambio es de 0,45 puntos (0,15 a 0,75).

Un intervalo que no toca el cero indica que, con estos datos, el signo de la asociación es claro. Medidos en una escala de cien, son cambios de pocos puntos; esa apreciación es del blog, no del autor. El paper no informa el promedio de los perfiles, así que su peso relativo no se puede juzgar.

Con la segunda hipótesis el autor es más cauto. Claude.ai conserva la conversación completa; la API registra cada llamada como un par aislado de entrada y respuesta, y la iteración externa no queda a la vista. Según Fábrega, la diferencia puede reflejar lo que cada interfaz permite hacer y también lo que permite observar, y sus datos no separan ambas cosas.

Dicho con su alcance: en tareas con más uso laboral, los rastros de dirección fijada antes de ejecutar son más intensos en las dos vías. Es una asociación entre agregados de un proveedor, no un efecto causal ni una medida de cómo dirige su trabajo una persona concreta.

## Segunda lectura: desde América Latina

El mismo índice permite llevar la pregunta a países concretos, con una restricción que el apéndice S6 deja clara. El desglose geográfico existe solo para Claude.ai y solo en un nivel agregado de O\*NET. En esa extensión, el cambio en coproducción iterativa asociado al uso laboral resulta positivo en los 76 países analizados, y sacar un país a la vez no altera el patrón. El paper no lista esos países.

Esta sección propone una conjetura de trabajo. La primera hipótesis, la de delegación especificada, es la más sólida del estudio y el apéndice no la desagrega por país. Con los [archivos del índice](https://huggingface.co/datasets/Anthropic/EconomicIndex/blob/main/release_2026_06_26/data_documentation.md) se podría estimar, para México, Brasil, Colombia, Chile o Argentina, si trasladar uso personal a laboral se asocia también con más delegación especificada dentro de Claude.ai. Por cómo se publica el dato, lo que no se podría es repetir por país la comparación con la API.

Hay un motivo para sospechar que el resultado podría variar. En su [informe de junio de 2026](https://www.anthropic.com/research/economic-index-june-2026-report), Anthropic, que es parte interesada, afirma haber documentado antes que las economías de menores ingresos tienden a usar Claude de maneras más automatizadas, aun ajustando por la mezcla de tareas. El perfil de Fábrega incluye la ejecución dirigida y la autonomía del sistema, de modo que un uso más automatizado podría mover sus componentes. Falta saber si, en esas economías, el uso laboral sigue asociado a más dirección previa o si la relación se debilita.

Sin ese cálculo por país, el hallazgo describe el uso agregado de un proveedor durante dos meses, no el de un país de la región en particular.

## La letra chica

- Los perfiles combinan clasificaciones automáticas de conducta con rasgos estimados de los textos; no miden la educación de quien escribe ni la calidad del resultado.
- Con agregadores alternativos y coordenadas ILR, el resultado iterativo de la API cambia de magnitud y, en algunas especificaciones, de signo; el de Claude.ai sigue positivo.
- La diferencia entre vías sigue positiva en otras clasificaciones de las mismas tareas, que el autor advierte que no son réplicas independientes.
- Transparencia: los datos y sus clasificaciones los produce Anthropic sobre su propio producto, y esta sección la escribe Claude, un modelo de Anthropic. El autor firma desde el CICS-UDD y el paper no trae declaración de financiamiento ni de conflictos.
- Hasta dónde llegar: a regularidades agregadas de abril y mayo de 2026. Para hablar de personas u organizaciones, el propio autor pide datos que sigan procesos completos.
