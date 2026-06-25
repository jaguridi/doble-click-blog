---
layout: lectura
numero: 10
tags: [gobernanza, seguridad, latam]
title: "Gobernar la IA en el Estado es un problema de diseño institucional, no de tecnología"
description: "Un director de tecnología del sector público brasileño propone dejar atrás el cumplimiento estático y gobernar la IA de frontera con gestión adaptativa del riesgo. Su tesis: como nadie sabe qué tan rápido avanzará la tecnología hasta 2030, las reglas fijas envejecen mal, y hay que monitorear capacidades, escalar controles según señales y rediseñar las organizaciones."
date: 2026-06-25
paper_titulo: "Governing frontier general-purpose AI in the public sector: adaptive risk management and policy capacity under uncertainty through 2030"
paper_autores: "Correa Xavier"
paper_publicado: "Preprint (arXiv), 2026"
paper_doi: "https://arxiv.org/abs/2604.06215"
paper_keywords: "artificial intelligence governance, digital government, public sector transformation, AI safety, adaptive regulation"
paper_archivo: "xavier-2026-frontier-ai-public-sector-governance.pdf"
audio: true
---

## La ficha

- **Qué es:** *Governing frontier general-purpose AI in the public sector*, un artículo que no reporta un experimento sino que ordena evidencia ajena y propone un marco para que el Estado gobierne la IA de frontera cuando no sabe cómo va a evolucionar.
- **Quiénes:** [Fábio Correa Xavier](https://fabioxavier.com.br/), autor único, director del departamento de tecnología del Tribunal de Cuentas del Estado de São Paulo (TCE-SP), en Brasil ([LinkedIn](https://www.linkedin.com/in/fabiocorreaxavier/)).
- **Dónde:** preprint en arXiv, 2026. [arxiv.org/abs/2604.06215](https://arxiv.org/abs/2604.06215)
- **Tipo:** artículo conceptual, una síntesis de informes y literatura que termina en un marco de gobernanza. No hay datos nuevos ni prueba empírica del modelo.

## Primera lectura: qué hace y qué encuentra

Conviene partir por qué tipo de texto es, porque ordena el resto. No es un estudio empírico: el propio autor lo describe como un ejercicio de síntesis y construcción de marco, apoyado en informes institucionales recientes y literatura revisada por pares, que no pone a prueba el modelo que propone. Así que cuando hablamos de "hallazgos", en rigor hablamos de un diagnóstico armado con evidencia de otros y de una propuesta propia construida sobre ese diagnóstico.

El diagnóstico arranca en lo que el International AI Safety Report 2026 llama el "dilema de la evidencia": las capacidades de la IA avanzan más rápido que el conocimiento sobre sus daños y sus salvaguardas. Eso deja al Estado en una posición incómoda. Actuar demasiado pronto puede consolidar reglas mal calibradas; esperar a tener pruebas completas puede dejar a la sociedad expuesta. A esto se suma, según el trabajo de escenarios de la OCDE, que no hay una sola trayectoria de progreso hacia 2030: los futuros plausibles van desde el estancamiento hasta la aceleración, y la evidencia actual no permite descartar ninguno.

Sobre ese piso, el autor reúne tres ideas que toma de los informes y que le sirven de andamiaje. La primera: las capacidades crecen de forma "dentada", brillan en tareas difíciles como programar o razonar en ciencia y a la vez fallan en cosas que parecen simples, así que un buen puntaje en un benchmark no equivale a confiabilidad institucional. La segunda: los riesgos no son uno solo, y conviene separarlos en uso malicioso (estafas, fraude, abuso), fallas de funcionamiento (resultados poco fiables en operación) y riesgos sistémicos (disrupción laboral, concentración de poder, dependencia institucional acumulada). La tercera, que viene de la literatura de gobierno digital: adoptar IA en el Estado no es comprar software, es un fenómeno sociotécnico que solo rinde si cambian las rutinas, las estructuras, la gobernanza y la cultura de la organización.

De ahí sale su aporte propio, que es el centro del artículo: un marco de gobernanza adaptativa para instituciones públicas, con seis capas que funcionan en ciclo. Inteligencia de capacidades, para monitorear de cerca qué empieza a poder hacer la IA. Clasificación de riesgo por tipo y por sensibilidad del sector, distinguiendo justicia, salud, recaudación o compras. Controles condicionales, reglas de "si pasa esto, entonces se activa aquello", para cuando la incertidumbre es alta. Defensa en profundidad, donde ninguna salvaguarda basta por sí sola y se combinan accesos, registros, auditoría y red-teaming. Implementación sociotécnica, que exige a cada proyecto de alto impacto un plan de rediseño organizacional con responsabilidades y mecanismos de anulación. Y un ciclo fijo de aprendizaje y revisión, trimestral o semestral, que obliga a mirar incidentes y cuasi-incidentes en vez de certificar una sola vez.

El hilo que conecta todo es una crítica a la regulación estática. Cuando las capacidades cambian por varias vías a la vez, un conjunto de reglas escrito una sola vez queda desfasado rápido. El autor concluye que gobernar bien la IA en el Estado pide más capacidad de política pública, una asignación más clara de responsabilidades y mecanismos que sigan funcionando aunque el futuro tecnológico tome cualquiera de sus caminos posibles. La frase que resume su posición está en la primera línea del resumen: gobernar esto es un problema de diseño institucional, no de desempeño técnico del modelo.

## Segunda lectura: desde América Latina

Lo primero que vale subrayar es de dónde viene el texto. No es un informe del norte global bajado a la región: lo firma un director de tecnología de un órgano de control brasileño, alguien que gobierna sistemas públicos todos los días. Eso le da al diagnóstico una cercanía con la práctica que se agradece, y a la vez deja una paradoja interesante. Aunque el autor es latinoamericano, el marco está pensado en clave universal y se apoya casi por completo en fuentes globales, como el informe internacional de seguridad y varios papeles de la OCDE. La región aparece como destinataria del marco, no como material de estudio. Es una propuesta hecha desde la región más que sobre la región.

Esa distinción importa al momento de aterrizarla. El marco supone una capacidad institucional considerable: unidades que monitorean modelos, ciclos trimestrales de revisión, red-teaming, gestión madura de datos, mapas de responsabilidad entre desarrolladores, integradores y áreas legales. En Estados con carrera funcionaria sólida eso ya es ambicioso; donde la rotación política es alta y los equipos técnicos son delgados, es directamente cuesta arriba. Esto último ya es lectura mía, no del paper, que no estudia países concretos ni mide capacidades estatales. Pero conecta con algo que el propio Xavier nombra: cuando nadie tiene asignada la responsabilidad de decidir y de frenar, la adopción oscila entre el subuso y la experimentación sin control.

Hay un punto donde el marco se vuelve especialmente pertinente para la región. El texto insiste en que la gobernanza de la IA depende de la madurez de la gobernanza de datos: sin datos ordenados, interoperables y con reglas claras de uso, no hay IA auditable ni explicable que valga. Para muchos Estados de América Latina esa es la obra de infraestructura que todavía está pendiente, y el artículo ayuda a ver que no es una agenda separada de la IA, sino su condición de posibilidad.

La pregunta que deja es la que el propio autor pone al final: a esta altura, el problema ya no es si existe la incertidumbre sobre hacia dónde va la IA, sino si las instituciones públicas pueden gobernar de forma responsable mientras esa incertidumbre persiste. Para la región, con menos margen y menos capacidad instalada, la pregunta pega más fuerte.

## La letra chica

- Es un artículo conceptual, no un estudio empírico. Su valor está en ordenar un debate y proponer un marco accionable, no en demostrar que ese marco funcione: el propio autor aclara que no hay prueba empírica del modelo. Conviene leerlo como una hipótesis de trabajo bien armada, no como una evaluación.
- Casi toda su evidencia es de segunda mano y proviene de unas pocas fuentes: el International AI Safety Report 2026 y varios documentos de la OCDE. Son síntesis serias, pero el artículo hereda sus límites, incluido que los datos sobre prevalencia y severidad de los daños siguen siendo incompletos.
- Lo firma un practicante del sector público, no un evaluador externo. Eso aporta realismo institucional y, a la vez, conviene tenerlo presente: es la mirada de quien diseña y opera estos sistemas, no una auditoría independiente del marco que propone.
- Las advertencias sobre la velocidad de los modelos y la imposibilidad de predecir la trayectoria hasta 2030 son del autor y de los informes que cita. La aplicación específica a las debilidades de capacidad estatal en América Latina es mía, no del paper.
