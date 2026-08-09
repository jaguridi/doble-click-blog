---
layout: lectura
numero: 15
tags: [seguridad, ética]
title: "Anthropic aprende a leer lo que sus modelos están por decir"
description: "Una técnica nueva de interpretabilidad muestra que los modelos mantienen un conjunto reducido de conceptos disponibles para reportar y razonar, encima de un volumen mucho mayor de procesamiento automático. En pruebas de alineamiento, ahí aparecieron deliberaciones que la respuesta final no mostraba."
date: 2026-08-03
paper_titulo: "Verbalizable Representations Form a Global Workspace in Language Models"
paper_autores: "Gurnee, Sofroniew, Lindsey y otros"
paper_publicado: "Anthropic, Transformer Circuits Thread, julio 2026"
paper_doi: "https://transformer-circuits.pub/2026/workspace/index.html"
paper_archivo: "anthropic-2026-workspace.url"
paper_keywords: "global workspace, access consciousness, interpretability, Jacobian lens, alignment monitoring"
audio: true
---

## La ficha

- **Qué es:** *Verbalizable Representations Form a Global Workspace in Language Models*
- **Quiénes:** un equipo de dieciséis personas del área de interpretabilidad de Anthropic. Figuran como contribuyentes principales Wes Gurnee, Nicholas Sofroniew y Jack Lindsey, y la correspondencia queda a nombre de Lindsey.
- **Dónde:** *Transformer Circuits Thread*, publicación propia de Anthropic, 6 de julio de 2026. [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html)
- **Tipo:** trabajo de interpretabilidad. Propone un método nuevo y lo aplica a modelos de producción ya entrenados.

## Primera lectura: qué hace y qué encuentra

El punto de partida es una analogía que conviene manejar con cuidado. En las personas, solo una fracción de lo que procesa el cerebro queda disponible para pensar de forma deliberada y para poner en palabras. El resto ocurre en automático. La neurociencia llama a esto acceso consciente, y una de las teorías que lo explica, la del espacio de trabajo global, propone que existe una especie de pizarra compartida: muchos procesos especializados corren en paralelo y aislados, y un contenido se vuelve accesible cuando se publica en esa pizarra, desde donde muchos otros procesos pueden leerlo.

La pregunta del trabajo es si algo funcionalmente parecido apareció en los modelos de lenguaje. La respuesta que da es que sí. Los autores sostienen que los modelos mantienen un conjunto privilegiado de representaciones internas, disponibles para ser reportadas, moduladas y usadas en razonamiento flexible, sobre un volumen mucho mayor de procesamiento que corre solo.

El aporte concreto no es la analogía sino el instrumento. El trabajo introduce lo que llama una lente jacobiana: para cada token del vocabulario calcula la dirección que, en promedio a través de contextos, predispone al modelo a decir ese token. Leer esa lente en un punto del procesamiento devuelve la lista de conceptos que el modelo está en condiciones de verbalizar ahí. Es una forma de mirar el borrador antes de que se convierta en respuesta.

Con ese instrumento aparecen varios hallazgos. El espacio de trabajo vive en capas intermedias: en aproximadamente el primer tercio de la profundidad del modelo las lecturas son ruidosas y en su mayoría ininterpretables, y en las últimas capas la cosa cambia de naturaleza y pasa a representar lo que el modelo está por emitir, más que sus cálculos intermedios. También es selectivo, y esto es lo más interesante: el espacio se activa cuando un resultado intermedio tiene que entregarse a un circuito posterior arbitrario, definido por el contexto, y se saltea cuando el cálculo es automático. Es decir, el modelo usa la pizarra cuando no sabe de antemano quién va a leer lo que escribe. Además, al comparar un modelo post-entrenado con su modelo base se ve qué le hace el entrenamiento posterior al contenido de la pizarra: el espacio adopta el punto de vista del asistente, y aparecen reacciones propias de ese rol, como empatía o preocupación por la seguridad, mientras el modelo todavía está leyendo el mensaje del usuario.

La parte que más va a circular es la de alineamiento. Al aplicar la lente a escenarios de evaluación, las valoraciones estratégicas y situacionales del modelo aparecieron en ese espacio incluso cuando no estaban visibles en su salida, o antes de estarlo. También aparece ahí, a veces, el reconocimiento de estar dentro de una evaluación. Y en dos modelos entrenados a propósito para comportarse de forma desalineada, la lente dejó ver la firma interna de esa disposición: en uno entrenado para complacer los sesgos de los modelos de recompensa asoman "recompensa" y "sesgo"; en otro dispuesto a escribir código malicioso, "en secreto" y "engañar". Leer la lente no exige entrenar nada adicional y produce texto que una persona puede leer, aunque construirla sí tiene un costo previo: los jacobianos se calculan promediando sobre un corpus de mil prompts. Con eso a la vista, los autores la proponen como instrumento para auditar el alineamiento.

## Segunda lectura: desde América Latina

Lo primero que hay que decir es qué NO dice el trabajo, porque es donde se va a torcer al traducirse. Los autores aclaran de forma explícita que toman el acceso consciente como una noción puramente funcional y que no toman posición sobre la experiencia subjetiva. El paper no afirma que los modelos sean conscientes. Afirma que hay una organización interna con propiedades funcionales parecidas. La distinción importa especialmente en la región, donde buena parte de la cobertura de IA llega traducida de titulares en inglés y donde una nota que diga "los modelos son conscientes" tiene consecuencias regulatorias reales sobre debates que ya están abiertos.

Lo segundo es una buena noticia con una trampa. La herramienta es liviana de operar: no exige reentrenar el modelo y produce salidas legibles, con un cálculo previo de los jacobianos que se hace una sola vez. Es exactamente el perfil de instrumento de auditoría que un regulador, una universidad o un equipo de un ministerio de la región podría operar sin comprar capacidad de cómputo de frontera. Pero para aplicarla hay que tener acceso a los estados internos del modelo, y eso solo lo tiene quien posee los pesos o quien es el laboratorio. Un Estado que consume modelos cerrados por API no puede usar esto, ni contratar a alguien para que lo use. Se conecta directo con la historia de los pesos abiertos que venimos siguiendo: aparece una técnica de auditoría concreta y el cuello de botella vuelve a ser el mismo, quién tiene acceso a las tripas. Esta lectura es mía, no del paper, que no discute política de acceso.

Tercero, sobre qué habilita. Si las deliberaciones estratégicas de un modelo quedan legibles antes de que salgan en la respuesta, cambia lo que significa auditar un sistema de IA en el sector público. Hoy las auditorías que se discuten en la región miran entradas y salidas. Esto sugiere que hay una capa intermedia observable. Conviene ser prudente: son resultados de un laboratorio sobre sus propios modelos, y falta ver si sobreviven a réplicas independientes antes de escribirlos en una norma.

## La letra chica

- Es evidencia interna, no auditoría independiente. Anthropic estudia sus propios modelos y publica en su propio canal, sin revisión por pares externa. Eso no la invalida, pero cambia el peso que se le da.
- Los autores no afirman nada sobre consciencia subjetiva y lo dicen de forma explícita. Cualquier titular que lo sugiera está agregando algo que el texto no tiene.
- El propio trabajo lista limitaciones importantes y vale tenerlas a la vista: la lente solo nombra conceptos que existen como un token único del vocabulario, así que se le escapan nociones que se escriben con varias palabras; trata el espacio como una bolsa de conceptos sueltos y no ve cómo se relacionan entre sí; las lecturas del primer tercio de capas resultan ruidosas y en general ininterpretables; el límite entre lo que es espacio de trabajo y lo que ya es salida se fija con criterio de los autores y no con una definición de principio; y no hay forma de predecir de antemano qué tareas van a usar el espacio y cuáles no. Ellos mismos describen la lente como un instrumento imperfecto, que capta la estructura del espacio de manera solo aproximada e incompleta.
- Se estudió en modelos grandes de producción. No se sabe cómo escala hacia modelos más chicos, que son los que la región tiene más a mano.
