---
layout: lectura
numero: 8
tags: [trabajo, mercados, latam]
title: "Con IA de por medio, el código que entregas ya no basta para probar que sabes programar"
description: "Entrevistas de programación simuladas con IA permitida muestran que los evaluadores no cambian qué entienden por pericia, pero sí la evidencia que piden. El código entregado deja de alcanzar: lo que ahora delata al buen programador es qué herramienta elige, cómo le habla y cuándo desconfía de lo que el modelo escupe."
date: 2026-06-19
paper_titulo: "Evolving Enactions of Expertise: Software Engineers' Evaluation and Demonstration of Coding Expertise with AI Coding Assistants"
paper_autores: "Jang, Sakashita, Niinuma y Gupta"
paper_publicado: "CHI 2026"
paper_doi: "https://doi.org/10.1145/3772318.3791260"
paper_archivo: "jang-2026-coding-expertise-ai-assistants.pdf"
paper_keywords: "AI Coding assistant, Coding Expertise, Software Engineering"
audio: true
---

## La ficha

- **Qué es:** *Evolving Enactions of Expertise: Software Engineers' Evaluation and Demonstration of Coding Expertise with AI Coding Assistants*
- **Quiénes:** [Yeonju Jang](https://scholar.google.com/scholar?q=Yeonju+Jang+coding+expertise) (Cornell University, el trabajo se hizo durante una pasantía en Fujitsu), [Mose Sakashita](https://scholar.google.com/scholar?q=Mose+Sakashita), [Koichiro Niinuma](https://scholar.google.com/scholar?q=Koichiro+Niinuma) y [Aakar Gupta](https://scholar.google.com/scholar?q=Aakar+Gupta) (Fujitsu Research of America).
- **Dónde:** *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (CHI 2026), Barcelona. [doi.org/10.1145/3772318.3791260](https://doi.org/10.1145/3772318.3791260)
- **Tipo:** estudio cualitativo. Doce entrevistas de programación simuladas, con dieciséis ingenieros de software emparejados de a dos, uno como evaluador y otro como candidato, con IA permitida.

## Primera lectura: qué hace y qué encuentra

Conviene partir por qué tipo de estudio es, porque ordena todo lo demás. Es un trabajo cualitativo que usa una técnica llamada *user enactment*: en vez de preguntar en abstracto, los investigadores montan una escena plausible del futuro cercano y dejan que la gente actúe dentro de ella. La escena elegida es la entrevista de programación en vivo, donde alguien resuelve un problema compartiendo pantalla mientras otro evalúa. Reclutaron a dieciséis ingenieros por redes y comunidades técnicas, los emparejaron por especialidad y lenguaje, y armaron doce sesiones. En cada una el evaluador diseñaba su propia tarea y sus criterios; el candidato tenía treinta minutos y podía usar cualquier herramienta de IA o buscador. El estudio no mide si la IA mejora la productividad ni evalúa modelo alguno. Describe cómo se demuestra y cómo se juzga la pericia cuando el modelo está sobre la mesa.

El primer hallazgo es el que da el título. Los evaluadores casi no cambiaron sus criterios. Entender el problema, explicar el código, manejar errores, escribir código limpio: lo de siempre. Lo que cambió fue la evidencia que aceptan para darlos por cumplidos. El código terminado, que durante décadas fue la prueba reina de que alguien sabe, dejó de bastar por sí solo, porque ahora lo puede escribir el modelo. Un evaluador notó que los comentarios prolijos del candidato estaban, pero los había generado la IA, así que no contaban como pericia propia. Otro vio a alguien resolver la tarea y aun así concluyó que sin IA no habría podido. La consecuencia práctica es que los evaluadores se apoyan mucho más en repreguntar: pedir que modifiquen la solución, que expliquen línea por línea, que digan qué pasaría si se cambia tal cosa. La prueba se corre del producto al proceso.

El segundo hallazgo es que la pericia empezó a manifestarse de maneras nuevas y a ocultarse en otras. Aparecen tres señales nuevas: cuál herramienta elige el candidato y por qué, cómo le habla al modelo, y qué hace con lo que el modelo le devuelve. Elegir Perplexity cuando hacían falta fuentes confiables fue leído como una jugada inteligente; un prompt demasiado amplio, como falta de comprensión del problema. Al mismo tiempo, otras señales tradicionales se apagan: cuando el modelo descompone la tarea, escribe el código entero o detecta el error y lo arregla de un viaje, el candidato pierde la ocasión de mostrar cómo entiende, cómo arma su enfoque y cómo depura. Una evaluadora se anticipó y partió la tarea en tres pasos que entregó de a uno, para que fuera el candidato, y no la IA, quien expandiera el razonamiento.

El tercer hallazgo es que nada de esto pesa igual para todos. Los evaluadores se dividen entre los que valoran la planificación y los que valoran la implementación. Para los primeros, la IA es casi un alivio: si lo central es pensar bien el problema, que el modelo escriba el código importa poco. Una evaluadora daba por hecho que el código funcionaría por venir de un generativo, y miraba si el candidato pensaba del modo correcto. Para los que se fijan en la implementación, en cambio, las señales nuevas importan mucho más, porque desconfían de que el modelo produzca código extensible y vigilan cómo el candidato elige, pregunta y descarta.

El cuarto hallazgo es una tensión. Con la IA disponible apareció una expectativa de mayor productividad que nadie definió como criterio, pero que igual operaba por debajo, y sin acuerdo sobre qué parte de la pericia la produce hubo malentendidos en las dos direcciones. Una candidata evitó la IA al principio para lucir su comprensión y después temió que eso la hiciera ver inexperta usando herramientas. Otro la usó de inmediato para terminar rápido y dejó al evaluador sin convencer, porque no explicó nada de lo que el modelo le había dado. La herramienta que promete velocidad también vuelve más resbaloso saber qué se está midiendo.

## Segunda lectura: desde América Latina

El estudio no es sobre América Latina. Los participantes se reclutaron por redes y comunidades internacionales y el paper no informa de dónde son, así que casi todo lo que sigue es lectura mía, no del estudio. Con esa advertencia por delante, hay un punto que aterriza fuerte en la región.

Buena parte del trabajo de programación que la región le vende al mundo pasa por exactamente este filtro: la entrevista técnica remota. Para mucha gente talentosa de Santiago, Bogotá, São Paulo o Buenos Aires, esa media hora compartiendo pantalla es la puerta de entrada a un empleo bien pagado sin emigrar. Y esa puerta está cambiando de cerradura justo ahora, sin reglas nuevas escritas. Si entregar código correcto ya no alcanza, y lo que se juzga es cómo dirigís al modelo, quien practicó mil problemas tipo LeetCode pero nunca aprendió a interrogar una herramienta de IA puede quedar mal parado aunque sepa programar. Y al revés: alguien que domina el ida y vuelta con el modelo podría aprobar sin la base que la empresa cree estar comprando.

Hay un detalle del paper que conviene traer acá: varios participantes describieron una hesitación a usar IA en la entrevista, un estigma que los autores llaman *AI shaming*. Uno se sintió desalentado de usarla pese a que las instrucciones lo permitían. En un mercado regional donde mucha gente se juega el empleo en estas pruebas, si la regla tácita castiga tanto usar la IA como no usarla, la entrevista termina midiendo quién leyó mejor las señales del evaluador y no quién resuelve mejor el problema. Lo que el estudio sugiere, y yo extiendo a la región, es que la salida no es prohibir ni permitir sin más, sino explicitar qué se evalúa. Las empresas y bootcamps que viven de colocar talento tienen ahí una tarea concreta: decir en voz alta qué cuenta como pericia cuando la IA está permitida, antes de que cada evaluador improvise su propia vara.

La pregunta que deja sirve para cualquier proceso de selección. Si dos personas igual de capaces pueden ser juzgadas distinto solo por cómo se paran frente a la IA, ¿se está midiendo pericia o lectura de expectativas? El estudio no lo resuelve, pero deja claro que mientras la regla no esté escrita, la respuesta queda al criterio de quien evalúa.

## La letra chica

- Es un estudio cualitativo y de laboratorio: su valor está en mostrar cómo y por qué cambian estas dinámicas, no en medir cuán extendidas están. Que sean dieciséis personas y doce sesiones no es un defecto; es lo que permite mirar de cerca algo que recién emerge.
- Son entrevistas simuladas, no contrataciones reales. Los propios autores avisan que una entrevista en vivo no captura lo colaborativo ni lo de largo plazo del trabajo real, donde la pericia se nota con el tiempo y en equipo. Es un retrato de un momento, no del oficio entero.
- Cada evaluador diseñó su propia tarea, así que la variedad de tareas y dificultades es parte del cuadro y no una constante controlada. Coherente con un estudio que busca explicar fenómenos, pero conviene tenerlo presente antes de generalizar una escena puntual.
