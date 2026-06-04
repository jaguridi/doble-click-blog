---
layout: lectura
numero: 1
title: "Políticos y funcionarios no quieren lo mismo de la IA"
description: "Qué encontró un estudio que entró a ministerios de Chile y Uruguay."
date: 2026-06-04
paper_titulo: "Thoughtful Adoption of NLP for Civic Participation: Understanding Differences Among Policymakers"
paper_autores: "Guridi, Cheyre y Yang"
paper_publicado: "Proc. ACM HCI (CSCW), 2025"
paper_doi: "https://doi.org/10.1145/3711091"
---

## La ficha

- **Qué es:** *Thoughtful Adoption of NLP for Civic Participation: Understanding Differences Among Policymakers*
- **Quiénes:** [Jose A. Guridi](https://jaguridi.github.io/), [Cristóbal Cheyre](https://infosci.cornell.edu/people/cristobal-cheyre) y [Qian Yang](https://qianyang.co/) (Cornell University)
- **Dónde:** *Proceedings of the ACM on Human-Computer Interaction* (CSCW), abril 2025. [doi.org/10.1145/3711091](https://doi.org/10.1145/3711091)
- **Tipo:** estudio cualitativo, 20 entrevistas.

## Primera lectura: qué hace y qué encuentra

Conviene partir por qué tipo de estudio es, porque eso ordena todo lo demás. Es un trabajo cualitativo. Los autores entrevistaron a 20 personas (7 autoridades designadas y 13 funcionarios de carrera) en cinco ministerios de Chile y en la agencia de gobierno digital de Uruguay, AGESIC, y analizaron esas conversaciones. No miden si el NLP mejora la participación ni evalúan ningún modelo. Explican cómo piensan y cómo dicen actuar dos grupos distintos frente a estas herramientas.

El punto de partida viene de la literatura previa, no de este estudio: el NLP puede ayudar a ordenar grandes volúmenes de comentarios ciudadanos, y aun así los gobiernos casi no lo usan. La pregunta propia del paper es por qué. Y su aporte arranca en una distinción que la literatura suele aplanar: en lugar de tratar a "los que deciden" como un solo bloque, separa a los políticos (las autoridades designadas que encabezan las instituciones) de los funcionarios (la carrera que diseña y ejecuta). Ambos miran la misma herramienta y ven cosas distintas, porque construyen su legitimidad en lugares opuestos.

Los políticos la construyen hacia afuera, en la confianza de la ciudadanía y la buena prensa. Por eso les atrae un NLP que se vea objetivo y moderno, y que despeje la sospecha de manipulación humana al momento de contar opiniones. "La máquina no interpreta, solo procesa datos", dice uno. El estudio le pone nombre al riesgo que esto esconde: la ilusión de objetividad, creer que algo es confiable solo porque no lo tocó una persona.

Los funcionarios la construyen hacia adentro, frente a sus jefaturas, y trabajan ahogados en volumen. Todos hablaron de reducir su carga de trabajo. Pero como son ellos los que operan el sistema, ven los riesgos concretos que los políticos casi no mencionan: errores de clasificación, datos sensibles, vigilancia. No quieren que la IA los reemplace. Quieren, en palabras de una funcionaria, un miembro del equipo que sistematice y que después puedan interrogar.

El tercer hallazgo es el que da el título. Ninguno de los dos grupos asume quién debería impulsar la adopción ni hacerse cargo si sale mal. Se culpan entre ellos: los políticos dicen que los funcionarios se resisten y no saben de tecnología; los funcionarios, que los políticos no lideran ni les dan tiempo ni infraestructura para aprender. A eso se suma una traba que ambos reconocen: las compras públicas no están hechas para esto. Un entrevistado pasó más de un año tratando de contratar un servicio de correo masivo. Para los autores, lo que frena la adopción no es la calidad del algoritmo, sino esa falta de claridad sobre quién es responsable.

## La letra chica

- Es un estudio cualitativo: su valor está en explicar el porqué y el cómo de estas decisiones, no en medir cuántos ni en probar que el NLP funcione. Los números de las tablas dicen cuántos entrevistados mencionaron cada cosa, no qué tan extendido está.
- Habla de NLP en un momento previo a la masificación de los LLM. Los propios autores advierten que ese avance puede cambiar algunos detalles. Lo organizacional, en cambio, envejece lento, porque trata de personas e instituciones.

## Segunda lectura: desde América Latina

Algo que reivindican los propios autores: esta es evidencia desde adentro de la región, con entrevistas en español y en ministerios reales, no extrapolada desde el norte global. La literatura de su campo casi no estudia estos países, así que el valor está en mirar de cerca algo poco mirado.

Importa desde dónde se mira. Chile y Uruguay son dos de los países de la región con más recorrido en gobierno digital: la agencia uruguaya AGESIC es una referencia, y Chile cuenta con una Política Nacional de IA. Si la falta de claridad sobre quién es responsable y la fricción de las compras públicas aparecen incluso ahí, es razonable pensar que pesan más donde la carrera funcionaria es más débil y la rotación política más alta. Esto último ya es lectura mía: el paper no estudió esos otros países, y lo dejo como hipótesis, no como hallazgo.

Donde el estudio se conecta con el presente es en el cambio de época. Las entrevistas retratan un mundo donde el NLP se le contrataba a un proveedor. Hoy un equipo puede pegar comentarios ciudadanos en un chatbot sin licitación ni auditoría. Eso no deja obsoleto al paper, lo vuelve más pertinente. Sus hallazgos sobre barreras técnicas son los que los LLM están borrando. Sus hallazgos sobre quién construye legitimidad y hacia dónde, y sobre la falta de claridad sobre quién responde, quedan en pie. Cuando usar la herramienta es así de fácil, lo que sigue trabando no es la capacidad del modelo, sino quién decide y quién se hace cargo. Los mismos autores apuntan a esto cuando advierten que los LLM pueden bajar las barreras técnicas y traer riesgos nuevos.

De ahí salen tres ideas que el paper sugiere y que se traducen directo a la región, sin olvidar que vienen de entrevistas y no de un experimento. La primera: no ofrecer la IA para participación solo como una ganancia de eficiencia, porque a los políticos los mueve la legitimidad. La segunda: lo que pedían los funcionarios, pilotos, validación humana y poder rastrear los resultados hasta el dato crudo, debería ser piso y no lujo. La tercera: que alguien tenga, de forma explícita, la responsabilidad de decidir si se adopta y también de frenar.

La pregunta que deja sirve para cualquier ministerio de la región. Ahora que usar IA es tan simple como pegar los comentarios en un chatbot, ¿quién responde cuando eso se usa para escuchar a la ciudadanía? Si la respuesta es nadie, el estudio sugiere que el problema está ahí, y no en el algoritmo.
