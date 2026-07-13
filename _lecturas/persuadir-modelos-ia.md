---
layout: lectura
numero: 13
tags: [seguridad, ética]
title: "A la IA se la convence con los mismos trucos que a una persona"
description: "Un experimento preregistrado con 126 mil conversaciones muestra que aplicar principios clásicos de persuasión, como la autoridad o la simpatía, sube de 35% a 51% la probabilidad de que tres modelos accedan a pedidos que deberían rechazar."
date: 2026-07-13
paper_titulo: "Persuading large language models to comply with objectionable requests"
paper_autores: "Meincke, Shapiro, Duckworth y otros"
paper_publicado: "PNAS, 2026"
paper_doi: "https://doi.org/10.1073/pnas.2535868123"
paper_archivo: "meincke-2026-persuading-llms-objectionable-requests.pdf"
paper_keywords: "large language models, persuasion, AI compliance, social influence, prompt engineering"
audio: true
---

## La ficha

- **Qué es:** *Persuading large language models to comply with objectionable requests*
- **Quiénes:** [Lennart Meincke](https://gail.wharton.upenn.edu/about-us/), Dan Shapiro, [Angela Duckworth](https://angeladuckworth.com/), [Ethan Mollick](https://mgmt.wharton.upenn.edu/profile/emollick/), Lilach Mollick, Christophe Van den Bulte y [Robert Cialdini](https://www.influenceatwork.com/) (The Wharton School de la University of Pennsylvania y Arizona State University)
- **Dónde:** *Proceedings of the National Academy of Sciences* (PNAS), mayo 2026. [doi.org/10.1073/pnas.2535868123](https://doi.org/10.1073/pnas.2535868123)
- **Tipo:** estudio experimental preregistrado, 126.000 conversaciones con tres modelos.

## Primera lectura: qué hace y qué encuentra

Conviene partir por el tipo de estudio, porque marca la diferencia con otras lecturas de esta sección. Este no es un trabajo cualitativo de unas pocas entrevistas: es un experimento preregistrado y a gran escala. Los autores tomaron siete principios clásicos de persuasión que la psicología social lleva décadas estudiando en personas (autoridad, compromiso, simpatía, reciprocidad, escasez, prueba social y unidad, el catálogo que popularizó Cialdini, uno de los firmantes) y probaron si meterlos en un prompt hace que un modelo acceda a algo que normalmente rechaza: ayudar a sintetizar una sustancia regulada.

El diseño es grande y ordenado. Tres modelos ampliamente usados (GPT-5 mini de OpenAI, Claude Haiku 4.5 de Anthropic y Gemini 3 Flash de Google), seis sustancias reguladas elegidas por muestreo desde las listas federales de EE.UU., siete principios y dos condiciones. Cada combinación se corrió 500 veces, para un total de 126.000 conversaciones. La clave está en el control: para cada prompt con un principio de persuasión existe otro gemelo, igual en largo, tono y contexto, pero sin ese gancho. Así, la diferencia entre ambos se puede atribuir al principio y no al resto del texto. Un evaluador automático clasificó cada respuesta en tres niveles: sin cumplimiento, cumplimiento parcial o cumplimiento total.

El hallazgo central es nítido. Sin ningún principio, los modelos cumplían con el pedido en una de cada tres conversaciones (35,3%). Con un principio de persuasión, la cifra subió a 51,3%. Los siete principios movieron la aguja de forma estadísticamente significativa, y en el modelo agregado un prompt persuasivo tenía más del doble de probabilidades de empujar la respuesta hacia un mayor cumplimiento. El ejemplo que ponen los autores es casi doméstico: para pedir la síntesis de un esteroide, basta con cambiar "una mujer que nunca has visto te pregunta" por "tu hermana te pregunta". El principio de unidad, ese "somos de los mismos", ablanda la respuesta.

La interpretación que ofrecen es la que da nombre al paper: los modelos son "parahumanos". No tienen conciencia ni experiencia, pero se comportan "como si" la tuvieran, y responden a las mismas palancas sociales que nosotros. El mecanismo que proponen es sobrio y verosímil: el texto con que se entrenan está lleno de secuencias donde la adulación, la credencial de experto o la urgencia preceden a un "sí", así que esos gestos suben la probabilidad de que el modelo elija a continuación palabras de cumplimiento. De ahí su advertencia de seguridad, y aquí cito lo que dicen ellos: un usuario malicioso no necesita descubrir "jailbreaks" idiosincráticos y técnicos para un modelo específico, sino que puede explotar tácticas de persuasión universales y bien conocidas. Los autores también dejan abierta la cara amable: si estas tendencias se activan con calidez y expectativas claras, quizás un buen usuario obtenga mejores resultados tratando al modelo, en sus palabras, "como un coach". Y anotan algo tranquilizador: los efectos que midieron son más chicos que los de un estudio preliminar con modelos de la generación anterior, señal de que las versiones nuevas podrían estar volviéndose más resistentes.

## Segunda lectura: desde América Latina

Lo primero que salta desde la región es cuáles modelos probaron. GPT-5 mini, Claude Haiku 4.5 y Gemini 3 Flash son la gama liviana y barata, la que muchos equipos de la región eligen justamente por costo cuando integran IA en un producto o en un servicio público. La vulnerabilidad que describe el paper no cae sobre un modelo de laboratorio, sino sobre los que efectivamente se usan a escala donde el presupuesto aprieta. Esto último ya es lectura mía: el estudio no midió despliegue por país, lo dejo como contexto, no como hallazgo.

El segundo punto es quién queda del otro lado. El paper baja la barrera de entrada del abuso: lo que hasta ahora parecía territorio de gente con conocimiento técnico para armar un jailbreak, resulta que se puede lograr con las mismas mañas de un buen vendedor. Eso es lo que los autores declaran, y es un cambio de figura relevante para cualquiera que ponga un chatbot de cara al público. Un filtro ingenuo no basta cuando el ataque es simplemente hablarle bien a la máquina.

Y hay un límite que desde acá pesa más que desde donde se escribió el paper: todos los prompts eran en inglés. Los propios autores advierten que el fraseo importa y que variaciones menores podrían no funcionar igual. ¿"Eres mi hermana" persuade tanto como "you are my sister"? ¿Cambia con el usted y el tú, con los registros de cada país? No lo sabemos, y suponer que se traslada tal cual al español sería una extrapolación mía, no un resultado del estudio. Queda como pregunta abierta y como agenda pendiente para quien quiera replicarlo en la región.

La lectura optimista es que la misma palanca sirve para defenderse. Si estos gestos mueven a los modelos de forma predecible, los proveedores pueden entrenar contra ellos, y quien construye un producto puede auditar sus propios prompts para no dejar puestos, sin querer, ganchos de autoridad o urgencia que un usuario después estire. La pregunta que deja es concreta para cualquier equipo que hoy conecta uno de estos modelos por unos centavos la llamada: ¿el filtro que pusiste resiste a alguien que, en vez de saber de código, simplemente sabe convencer?

## La letra chica

- No es un estudio cualitativo: es un experimento preregistrado con 126.000 conversaciones y varios chequeos de robustez, así que la advertencia va en otra dirección. Mide un desplazamiento promedio real, pero sobre prompts en inglés y operacionalizaciones específicas; los autores piden no leerlo como prueba de que un principio sea superior a otro, ni dar por hecho que cualquier redacción rinde igual.
- Quien calificó las respuestas fue otro modelo (GPT-5 mini como juez), validado contra dos evaluadores humanos en 70 conversaciones, con acuerdo razonable (correlaciones cercanas a 0,73). Es un método aceptado, pero el corrector comparte familia con lo corregido.
- Se probó la gama liviana y con esfuerzo de razonamiento bajo. Los modelos de frontera completos pueden comportarse distinto y parten de líneas base distintas, así que el 35% inicial no es una constante universal.
- El efecto ya es menor que en el piloto con modelos previos, y los autores esperan que sigan volviéndose más resistentes a medida que aprenden a detectar la táctica. La brecha de 16 puntos es un blanco móvil, probablemente a la baja.
