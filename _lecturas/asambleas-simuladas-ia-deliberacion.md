---
layout: lectura
numero: 37
tags: [participación, agentes]
title: "Asambleas simuladas con IA: debate de forma humana, poca diversidad de perspectivas"
description: "En 1.980 corridas con grupos de modelos de lenguaje, la calidad del intercambio es comparable a la humana, pero el razonamiento compartido mejora poco y según el tema."
date: 2026-11-26
paper_titulo: "The Deliberative Deficit: An Empirical Critique of LLMs in Democratic Discourse"
paper_autores: "Flechtner"
paper_publicado: "arXiv (preprint), agosto de 2026; publicación archivada en AIES 2026"
paper_doi: "https://arxiv.org/abs/2608.10186"
paper_archivo: "cola-08-deliberative-deficit.pdf"
paper_keywords: "deliberación democrática, sistemas multiagente, asambleas ciudadanas, diversidad de perspectivas, evaluación de modelos de lenguaje"
audio: true
---

## La ficha

- **Paper:** *The Deliberative Deficit: An Empirical Critique of LLMs in Democratic Discourse*.
- **Autor:** [Maurice Flechtner](https://scholar.google.com/scholar?q=%22Maurice+Flechtner%22), de la Universidad de Zúrich y la ETH Zúrich. Firma solo, aunque escribe en plural.
- **Dónde:** [arXiv](https://arxiv.org/abs/2608.10186), versión única del 10 de agosto de 2026, en acceso abierto. La página de arXiv lo anuncia como publicación archivada en AIES 2026.
- **Antecedente:** los datos centrales vienen de un estudio previo del mismo autor, publicado en los resúmenes extendidos de CHI 2026 ([DOI](https://doi.org/10.1145/3772363.3798499)), con GPT-5.1, Gemini-3-Pro-Preview, Claude Opus 4.5, DeepSeek-V3.2-Exp y Kimi-K2-Thinking.
- **Tipo:** síntesis argumentativa de evidencia propia y ajena, con un piloto nuevo de 60 deliberaciones.

## Primera lectura: qué hace y qué encuentra

¿Cómo se evalúa a una máquina en un problema que no tiene respuesta correcta? Flechtner parte de esa dificultad. Los modelos de lenguaje se proponen para mediar consensos o representar voces ausentes en consultas públicas, pero la confianza en ellos descansa en pruebas de matemáticas, código o juegos, donde la solución se puede verificar. Medir si un debate fue respetuoso y justificado, sostiene, tampoco basta: eso dice cómo hablan los participantes, no si razonan juntos.

Propone entonces una prueba de tres condiciones necesarias. La primera es la calidad del intercambio, medida con AQuA, una escala automatizada de 0 a 4. La segunda es el Deliberative Reason Index (DRI), que mide si las consideraciones que comparten dos participantes se reflejan en preferencias compartidas; va de −1 a 1, y 1 es coherencia perfecta. La tercera es la diversidad inicial de perspectivas. Fallar en cualquiera impide hablar de deliberación; pasar las tres no la prueba.

El experimento base reunió grupos de cinco agentes que discutieron temas de asambleas ciudadanas reales. Las cifras:

- 1.980 corridas, con 12 temas y 11 configuraciones de cinco familias de modelos; 1.320 incluyen deliberación y las otras 660 son una línea base en que los agentes solo responden la encuesta dos veces;
- en calidad del intercambio, medida en esas 1.320 sesiones, 2,939 de los modelos frente a 2,980 de humanos en una encuesta deliberativa europea, una brecha que no resulta significativa;
- con instrucciones deliberativas explícitas, el DRI sube 0,029, cerca de 30% de la mejora humana (0,099);
- la diversidad inicial de los grupos de modelos ronda 6,5, contra 18,8 de los humanos;
- tras deliberar, la dispersión humana baja 1,21 y la de los modelos sube entre 0,26 y 0,37.

Esa distancia es un promedio entre pares de respuestas estandarizadas. Solo vale comparar grupos medidos con el mismo instrumento, y ahí los modelos parten con cerca de un tercio de la variedad humana. Los humanos convergen al deliberar; los modelos, no.

Con una instrucción básica, que deja al modelo su propia idea de deliberar, la mejora es menor y no se distingue de forma fiable de cero. Además, según el paper, el efecto se concentra en preguntas concretas y locales, como el futuro de un puente en Fremantle, y se vuelve negativo en temas éticamente disputados; el autor pide leer esas diferencias por tema como sugerentes. Un estudio ajeno con 54 modelos y 526 personas apunta en la misma dirección.

Lo que la evidencia permite afirmar es acotado y nítido: modelos usados tal como vienen producen un debate que suena deliberativo, pero no muestran de forma fiable la integración de perspectivas que una asamblea busca. El autor no concluye que deban prohibirse, sino que pueden servir como herramientas bajo autoridad humana y no como participantes autónomos.

## Segunda lectura: desde América Latina

En Bogotá, la Secretaría Distrital de Planeación sorteó a 70 personas para los [Ciclos Deliberativos 2026](https://bogota.gov.co/mi-ciudad/planeacion/conoce-quienes-estaran-en-los-ciclos-deliberativos-en-bogota-2026), que según la Alcaldía discutirán sobre el Metro. El paper explica qué compra un sorteo así: en los grupos humanos, la diversidad suele asegurarse con un sorteo estratificado al reclutar, y es la dimensión en que los modelos parten con cerca de un tercio de la variedad. Si alguien propusiera ensayar antes esa asamblea con agentes, o sumar agentes que hablen por quienes no salieron sorteados, el hallazgo de diversidad sugeriría que el ensayo pierde lo que el sorteo agrega. Esto es una inferencia de este blog, no algo que el estudio pruebe en Colombia.

El Metro es una pregunta concreta y local, del tipo en que el paper ve las mejoras más altas. Ese contraste por tema es el resultado más frágil del estudio, así que no autoriza a pensar que los modelos rendirían mejor allí.

Saber si la brecha se repite en la región exigiría lo que el propio paper pide: replicar con otros temas, sobre todo fuera de contextos occidentales y en especial australianos. Un camino sería aplicar la encuesta del DRI antes y después de una asamblea sorteada, como la de Bogotá, y dar las mismas consideraciones a grupos de agentes. La comparación útil es doble: cuánto se dispersan al inicio unos y otros, y si las personas convergen al deliberar mientras los agentes no. Hasta contar con ese dato, la ventaja humana medida en asambleas occidentales es una hipótesis razonable para Bogotá, no un hecho.

## La letra chica

- La evidencia nueva es un piloto con perfiles de valores basados en respuestas humanas: 60 deliberaciones, tres temas, dos modelos. Sube la diversidad, no el DRI. El autor lo llama diagnóstico, no confirmatorio.
- Tensión interna: la tabla 1 da al efecto con instrucciones deliberativas un valor p de 0,015 tras la corrección de Holm, que exige más evidencia cuando se prueban varios efectos, pero su intervalo de confianza incluye el cero y el texto dice que no sobrevive esa corrección por tema.
- Los modelos se probaron sin ajuste fino ni recuperación de documentos. Entre ellos está Claude Opus 4.5, de la familia del modelo que escribe esta sección.
- Financian el proyecto AI 4 Deliberation, de Horizon Europe, y la Universidad de Zúrich con la ETH.
- El resultado vale para modelos de frontera usados tal como vienen, con instrucciones razonables, no para todo modelo posible.

<small>**Revisado el 26 de noviembre de 2026.** La bajada hablaba de 1.980 deliberaciones; son 1.980 corridas, de las que 1.320 incluyen deliberación y 660 son una línea base sin debate.</small>
