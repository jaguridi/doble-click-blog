---
layout: lectura
numero: 7
tags: [trabajo, mercados, latam]
title: "La IA escribe el código, pero el resultado depende de cuánto sabes del problema"
description: "Anthropic analizó unas 400 mil sesiones de Claude Code y encontró un patrón parejo: el que dirige bien a la IA no es necesariamente quien sabe programar, sino quien conoce el dominio del problema. La experiencia en el área pesa más que la profesión, y la brecha entre novatos y el resto sigue ahí."
date: 2026-06-16
paper_titulo: "Agentic coding and persistent returns to expertise"
paper_autores: "Hitzig, Massenkoff, Lyubich, Heller y McCrory"
paper_publicado: "Anthropic, junio 2026"
paper_doi: "https://www.anthropic.com/research/claude-code-expertise"
paper_keywords: "agentic coding, returns to expertise, division of labor, task composition, occupations, AI and work"
audio: true
---

## La ficha

- **Qué es:** *Agentic coding and persistent returns to expertise*, un informe del equipo de investigación económica de Anthropic.
- **Quiénes:** Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Ryan Heller y Peter McCrory.
- **Dónde:** publicado en el sitio de Anthropic el 16 de junio de 2026. No es un paper con revisión de pares ni tiene DOI: es un reporte de la propia empresa. [anthropic.com/research/claude-code-expertise](https://www.anthropic.com/research/claude-code-expertise)
- **Tipo:** estudio observacional a gran escala. Analizan alrededor de 400 mil sesiones interactivas de Claude Code, de unos 235 mil usuarios, entre octubre de 2025 y abril de 2026, con un método que preserva la privacidad: los investigadores no leen transcripciones individuales, sino que clasificadores automáticos etiquetan cada sesión y trabajan sobre los agregados.

## Primera lectura: qué hace y qué encuentra

Conviene partir por lo que el estudio mide y lo que no. Claude Code es la herramienta de Anthropic para programar conversando con el modelo, donde la persona pide y el modelo ejecuta acciones sobre el código. El estudio no observa si ese código termina usándose ni si el proyecto sale bien en el mundo real. Lo que observa es la sesión: cómo se reparte el trabajo entre la persona y el modelo, en qué consiste, y una medida interna de si la sesión llegó a algo. Toda la evidencia viene de clasificadores que etiquetan automáticamente cada conversación, y los propios autores avisan que esos clasificadores son difíciles de validar a esa escala. Vale tenerlo presente al leer cualquier cifra.

El primer hallazgo es sobre la división del trabajo. En una sesión típica, la persona toma cerca del 70% de las decisiones de planificación pero solo un 20% de las decisiones de ejecución. El modelo corre alrededor de diez acciones por cada instrucción de la persona, y en casos extremos pasa de cien. El patrón que dibujan es nítido: la persona define qué hacer y el modelo resuelve cómo hacerlo.

En qué consiste el trabajo también cambió en el período. Cerca del 56% de las sesiones son escribir código (25%), corregirlo (26%) o probarlo (5%); un 17% es operar software ya hecho; un 14% es planificar o explorar; y un 13% es analizar datos o documentos en prosa. Entre octubre y abril, la corrección de código cayó de 33% a 19% y la operación de software subió de 14% a 21%. Los autores lo leen como un desplazamiento desde apagar incendios hacia tareas más de construcción y operación, aunque, otra vez, es una foto corta de un terreno que se mueve rápido.

El centro del informe, y de donde sale el título, es la experiencia. Acá hay que ser preciso con qué se mide: no es la profesión de la persona ni su currículum, sino un nivel de experiencia en el dominio específico de la tarea, inferido por un clasificador en una escala de cinco puntos, de novato a experto. Con esa medida, las sesiones de expertos se ven distintas: el modelo corre unas doce acciones por instrucción y produce del orden de 3.200 palabras de resultado, contra unas cinco acciones y 600 palabras en las de novatos. La diferencia es estadísticamente significativa en todos los niveles.

El salto importante está en el éxito. El estudio usa dos varas. Una estricta, el éxito verificado, donde hay alguna señal concreta de que la tarea se cumplió: ahí los novatos llegan al 15% y de intermedio en adelante el rango sube a 28-33%. Una laxa, el éxito al menos parcial: los novatos llegan al 77% y de intermedio en adelante a 91-92%. Cuando la sesión se complica, la brecha se ensancha: entre las sesiones con dificultades detectadas, los novatos terminan con éxito verificado un 4% de las veces y los expertos un 15%. Y los novatos abandonan la sesión con una frecuencia del 19%, contra 5-7% en los demás grupos.

Acá aparece el hallazgo que los autores destacan como más llamativo: la profesión importa menos que la experiencia. En las sesiones que producen código, las ocupaciones de software tienen un 34% de éxito verificado y el resto un 29%, una diferencia de apenas cinco puntos. Cada una de las diez ocupaciones más grandes del conjunto queda dentro de siete puntos de los ingenieros de software. Aparecen gestión, ventas y derecho entre los grupos no técnicos que más rápido crecen. Dicho de otro modo: lo que permite dirigir bien al modelo se parece más a saber del problema que a saber escribir código.

De ahí el nombre, "retornos persistentes a la experiencia". Es un término prestado de la economía laboral, donde "retorno" es lo que rinde una habilidad. La tesis es que la IA que programa vuelve menos central la formación formal en código, pero no borra el valor de la pericia: lo corre de lugar. Lo que rinde ahora es el conocimiento del dominio. Un matiz que los propios autores subrayan y conviene no perder: la mayor parte de la ganancia aparece al pasar de novato a intermedio; de intermedio a experto, la mejora es modesta. No hace falta ser el mejor del área para sacarle provecho, pero partir de cero sí cuesta caro.

El estudio cierra con una estimación de valor que conviene leer con pinzas. Comparando las tareas de las sesiones con avisos de mercados de trabajo freelance, calculan que el valor mediano de una sesión subió 27% entre octubre y abril, con la construcción liderando (+43%). Es una aproximación indirecta, basada en lo que se paga por encargos sueltos, no en trabajo asalariado, y los propios autores la describen como un emparejamiento difuso.

## Segunda lectura: desde América Latina

El estudio es global y no separa a América Latina, así que casi todo lo que sigue es extrapolación mía, no del informe. Con esa advertencia por delante, hay una señal que vale para la región.

El dato de que la profesión pesa poco y lo que manda es el conocimiento del dominio cambia quién puede usar estas herramientas. En buena parte de América Latina escasean los ingenieros de software formados, pero no escasean los expertos de dominio: investigadoras, funcionarios públicos, contadoras, abogados, gente de pymes que conoce su problema al detalle aunque nunca haya programado. Si lo que rinde es saber del problema, la puerta se abre para ese perfil, que es justamente el que antes quedaba afuera por no saber código. Para alguien como José, que se mueve entre la investigación y la política pública sin ser ingeniero, el hallazgo es de los que dan ganas de probar.

Pero el mismo estudio pone el freno, y es la parte que no conviene saltarse. La brecha del novato es real: 15% de éxito verificado contra 28-33%, y casi uno de cada cinco abandona cuando la cosa se complica. La democratización es parcial, no automática. Y donde se concentra la ganancia es en el tramo de novato a intermedio, es decir, en aprender lo justo para dejar de ser novato. Eso, leído desde la región, dice algo concreto: el acceso a la herramienta no alcanza si no viene con un mínimo de práctica y acompañamiento para cruzar ese primer tramo. Repartir licencias sin eso deja a mucha gente en el 15% y en el 19% que abandona.

Hay además una razón para la prudencia que es propia de mirar desde acá. Es un estudio de la empresa que vende la herramienta, sobre datos que no podemos auditar, con métricas inferidas. Antes de que un ministerio o una universidad de la región lo cite para justificar una compra o una política, conviene pedir lo que el propio informe no tiene: evidencia de resultados en el mundo real y, ojalá, en contextos parecidos a los nuestros. La señal es interesante y vale explorarla; usarla como prueba terminada sería ir más lejos de lo que el estudio aguanta.

La pregunta que deja, y que los autores también se hacen, es si estos retornos a la experiencia se sostienen o se achican con el tiempo. Si se achican, querría decir que los modelos empiezan a aportar el criterio que hoy pone la persona. Si se sostienen, el mensaje para la región es más bien al revés: la herramienta baja la barrera del código, pero el conocimiento del propio campo sigue siendo lo que marca la diferencia, y eso no se descarga.

## La letra chica

- Es un estudio de Anthropic sobre su propio producto. Eso no invalida los datos, pero sí pide cautela: la empresa tiene interés en que la historia salga favorable, y la elección de qué medir y cómo encuadrarlo no es neutral. Conviene leerlo como lo que es, evidencia interna y no auditoría independiente.
- Todo cuelga de clasificadores automáticos que etiquetan sesiones, y los autores admiten que validarlos a esta escala es difícil. El "nivel de experiencia" y el "éxito" no se observan directamente: se infieren. Agrego algo que es lectura mía y no del paper: si la misma señal que hace ver "experta" a una sesión es parte de lo que la hace ver "exitosa", una porción de la relación entre experiencia y éxito podría venir de cómo se mide y no solo del mundo. Los autores no afirman esto; lo dejo como cautela al interpretar.
- No hay resultados del mundo real. El estudio no ve si el código se usó, si el proyecto funcionó ni si alguien quedó conforme. "Éxito" es una señal dentro de la sesión, no fuera de ella.
- La cobertura es parcial. Queda afuera el uso no interactivo, el modo automático sin supervisión y las integraciones con editores de terceros, además de un 7,7% de sesiones descartadas por no tener un objetivo claro. Es un retrato de cómo se usa Claude Code conversando, no de todo el uso de IA para programar.
