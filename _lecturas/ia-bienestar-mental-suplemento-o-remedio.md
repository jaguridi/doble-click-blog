---
layout: lectura
numero: 21
tags: [salud, diseño, ética]
title: "Un chatbot de bienestar mental: ¿suplemento, remedio o profesor de yoga?"
description: "Veinticuatro expertos en clínica, ética y política pública, más de cien documentos regulatorios, y una conclusión incómoda para la industria: lo que define si una IA de bienestar mental está bien diseñada no es qué tan buena es conversando, sino qué beneficio concreto promete y a quién. Una herramienta pensada para servirle a todos no le responde a nadie."
date: 2026-09-07
paper_titulo: "Framing Responsible Design of AI for Mental Well-Being: AI as Primary Care, Nutritional Supplement, or Yoga Instructor?"
paper_autores: "Cooper, Guridi, Hwang, Kolko, McGinty y Yang"
paper_publicado: "CHI 2026"
paper_doi: "https://doi.org/10.1145/3772318.3791556"
paper_archivo: "3772318.3791556.pdf"
paper_keywords: "Responsible Artificial Intelligence, Design, Mental Health, Large Language Models"
audio: true
---

## La ficha

- **Qué es:** *Framing Responsible Design of AI for Mental Well-Being: AI as Primary Care, Nutritional Supplement, or Yoga Instructor?*
- **Quiénes:** [Ned Cooper](https://scholar.google.com/scholar?q=%22Ned+Cooper%22+%22human-computer+interaction%22), [Jose A. Guridi](https://jaguridi.github.io/) y [Qian Yang](https://qianyang.co/) (Cornell University), [Angel Hsing-Chi Hwang](https://scholar.google.com/scholar?q=%22Angel+Hsing-Chi+Hwang%22) (University of Southern California), [Beth Kolko](https://scholar.google.com/scholar?q=%22Beth+Kolko%22+%22human+centered+design%22) (University of Washington) y [Emma Elizabeth McGinty](https://scholar.google.com/scholar?q=%22Emma+E.+McGinty%22+%22health+policy%22) (Weill Cornell Medicine)
- **Dónde:** *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*, Barcelona, abril 2026. [doi.org/10.1145/3772318.3791556](https://doi.org/10.1145/3772318.3791556)
- **Tipo:** estudio cualitativo en tres etapas: 24 entrevistados expertos y análisis de más de 100 documentos regulatorios.

## Primera lectura: qué hace y qué encuentra

El objeto del estudio son las herramientas **no clínicas**: ChatGPT, Replika y compañía, usadas para desahogarse o sentirse mejor, sin receta ni supervisión de un profesional. La ley estadounidense separa esto con nitidez. Lo clínico lo regula la FDA como dispositivo médico; lo no clínico lo mira la FTC con mano liviana, como tecnología de consumo. Millones de personas ya están del lado liviano.

De ahí sale la pregunta, que es de diseño y no de medición: qué significa, en concreto, diseñar una de estas herramientas con responsabilidad. Los autores no evalúan ningún chatbot ni miden ningún efecto. Preguntan, a expertos en ética médica, política de salud, regulación de IA y diseño de tecnología sanitaria, analizan más de cien documentos de política pública, y vuelven a los entrevistados a discutir lo encontrado. Las primeras entrevistas casi fracasan, y eso es parte del hallazgo: los expertos en política de salud no veían por qué los estaban entrevistando, y los de política tecnológica compartían la preocupación sin ofrecer nada accionable. Lo único que resonó en todos fue una analogía suelta: algunas de estas herramientas se parecen a un suplemento nutricional, y otras a un remedio de venta libre.

El paper convierte esa intuición en un mapa de dos ejes: si la herramienta es un producto o un servicio, y si garantiza o no un resultado de salud. Quedan cuatro casillas. El suplemento es un producto que no garantiza nada. El remedio de venta libre garantiza alivio para un síntoma definido. La atención primaria es un servicio que garantiza el resultado, y si no puede darlo queda obligado a derivar. El profesor de yoga es un servicio sin garantía: puede mejorar o arruinar los beneficios probados del yoga con su instrucción, y aun así no promete ninguno.

Lo interesante no es la ocurrencia, sino lo que ordena: cada casilla trae riesgos primarios distintos y por lo tanto responsabilidades distintas. En una herramienta tipo remedio lo urgente es seguridad, efectividad y acceso equitativo, y varios entrevistados fueron explícitos en que algo que no funciona igual para todos los grupos no puede llamarse seguro y efectivo. En una tipo suplemento es casi lo contrario: su efectividad clínica importa poco, y lo que importa es que no reemplace la atención clínica ni el autocuidado. Como resumió un entrevistado, no es problema que alguien hable con un chatbot terapéutico, sea efectivo o no; es problema cuando esa persona debería estar hablando con un psiquiatra.

El segundo hallazgo es el que más muerde. Todos los entrevistados, con palabras distintas, exigieron que una herramienta declare sus **ingredientes activos**: el mecanismo probado por el cual mejora el bienestar. Los clínicos lo llamaban así, los éticos hablaban de teoría del cambio, la industria de la esencia real del producto. Con eso los autores distinguen tres tipos: las validadas como un todo mediante ensayos controlados, rarísimas; las que entregan un ingrediente probado como la terapia cognitivo conductual sin estar validadas ellas mismas; y las que no articulan ningún ingrediente, como ChatGPT de fábrica usado para desestresarse. Ningún entrevistado describió a esta última categoría como diseño responsable, y el paralelo que aparece varias veces son las redes sociales, que tampoco entendían cómo estaban entreteniendo a la gente y descubrieron tarde que el motor era la polarización y la rabia.

El tercer hallazgo los autores no lo resuelven, lo dejan planteado: dónde está el límite entre riesgo y beneficio. Los entrevistados de medicina y política de salud aceptaban el razonamiento de los medicamentos innovadores, donde un fármaco que salva a muchos se aprueba aunque sea letal para unos pocos, siempre que el riesgo esté declarado. Los de ética y diseño se resistieron con fuerza a esa aritmética poblacional, y la división cayó casi exactamente por línea disciplinar. Donde no hubo matiz fue entre los clínicos: varios insistieron en que preguntar si alguien tiene pensamientos suicidas no basta, y describieron como no negociables una evaluación de riesgo real y una derivación garantizada.

## Segunda lectura: desde América Latina

La advertencia primero: el análisis regulatorio es de Estados Unidos y los autores lo declaran. La FDA, la FTC y la definición de atención primaria de Medicare y Medicaid son el material del que están hechas las cuatro analogías, y nada de eso se importa tal cual. Pero conviene separar dos capas. La legal no viaja. La de diseño sí, y es la que el paper propone de verdad: un vocabulario para que quien construye la herramienta declare qué promete y a quién, antes de que exista una ley que se lo exija. Donde la regulación está en pañales, ese vocabulario llega justo cuando sirve.

Donde el marco se tensiona es en la derivación. Lo que separa a la atención primaria del profesor de yoga es la obligación de derivar de forma efectiva cuando la herramienta no puede resolver, y eso supone que existe a quién derivar. En buena parte de América Latina el especialista no está, o está a meses de lista de espera, así que el criterio de los clínicos entrevistados se vuelve más exigente de lo que suena: una herramienta que deriva a un vacío no cumplió. Y pedir que no sustituya la atención clínica supone que esa atención es una alternativa disponible. Para mucha gente acá, el chatbot gratis y en español no compite con el psicólogo, compite con nada, y desalentar su uso deja de ser solo precaución. Esto ya es lectura mía: el paper no estudió la región y sería injusto pedirle una respuesta a esa versión del dilema.

Algo parecido pasa con los ingredientes activos. La terapia cognitivo conductual y compañía fueron validadas mayoritariamente en otras poblaciones y en otro idioma, y quien las entrega acá es un modelo entrenado sobre todo en inglés. Declarar el ingrediente es el piso, no el techo. Esta extrapolación también es mía, aunque apunta hacia donde los autores ya miran cuando proponen una base de datos de ingredientes activos que documente qué tan bien funciona cada mecanismo en distintas poblaciones.

La pregunta que deja sirve para cualquier equipo que esté construyendo algo así en la región. Si tuvieras que escribir en la portada de tu herramienta qué mejora, en quién y por qué mecanismo probado, ¿podrías? Si la respuesta es que sirve para todo y para todos, el paper sugiere que eso no es versatilidad. Es ausencia de un responsable.

## La letra chica

- Transparencia: el autor de este blog es coautor del paper.
- Es un estudio cualitativo: su valor está en ofrecer un marco y explicitar desacuerdos, no en medir cuántos expertos piensan qué. El análisis regulatorio cubre solo Estados Unidos, y los autores lo justifican como una decisión de profundidad antes que de alcance.
- No entrevistaron a usuarios ni pacientes, y explican por qué: querían mirar riesgos que todavía no son observables, para lo cual la experiencia subjetiva de uso no sirve. Varios entrevistados de industria vienen de startups, y los propios autores anotan que los expertos de grandes hospitales y aseguradoras fueron menos accesibles.
- El paper no propone un estándar validado ni lo pretende. Deja abiertas dos preguntas que sus entrevistados no lograron zanjar: si conviene evaluar estas herramientas por su efecto poblacional, y si un riesgo proporcional al beneficio es vara suficiente.
