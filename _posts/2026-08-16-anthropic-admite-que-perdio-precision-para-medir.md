---
layout: post
title: "Anthropic admite que perdió precisión para medir sus propios riesgos"
description: "El informe que la empresa escribe sobre sí misma reconoce que sus instrumentos ya no alcanzan, y sigue siendo el único mecanismo de rendición de cuentas que existe."
date: 2026-08-16 08:05:41 -0400
tags: [seguridad, gobernanza, latam, trabajo]
audio: true
---

Anthropic publicó su [segundo informe de riesgos](https://www.anthropic.com/aug-2026-risk-report), 186 páginas exigidas por su propia política interna de escalamiento responsable. Lo más interesante no es lo que el documento mide, sino lo que admite que ya no puede medir: la empresa reconoce que sus instrumentos para estimar cuánto avanzan realmente las capacidades de sus modelos perdieron precisión. Por eso sube el riesgo de daño catastrófico por desalineación —es decir, que un modelo persiga objetivos distintos de los que se le pidieron— de "muy bajo" a "bajo", y aclara que el cambio refleja incertidumbre, no un hallazgo nuevo.

En el camino, el informe revela dos cosas que no estaban en el radar público. La primera es Model 2, un modelo interno algo más capaz que Mythos 5, en uso intensivo dentro de la empresa, que no corrió la batería completa de pruebas previa a un despliegue y que, según el texto, no hay planes de liberar. La segunda es un error que duró once meses: entre mayo de 2025 y abril de 2026, una bandera de configuración dejó desactivado el clasificador que bloquea información biológica peligrosa en todo el tráfico de retroalimentación humana. Son 133 millones de intercambios con unos 50.000 contratistas externos.

Ese segundo dato es el que aterriza en la región. Los contratistas que alinean estos modelos —las personas que califican respuestas para enseñarle al sistema qué está bien y qué no— son en buena parte trabajadores del Sur global contratados por intermediarios. América Latina ya está adentro del proceso: pone trabajo y queda expuesta cuando un filtro falla, sin tener una sola institución capaz de auditar el informe, el modelo interno que describe, ni la escala con la que la empresa se puntúa a sí misma. El documento salió el mismo día en que se conoció [la mejor trimestral de su historia](https://finance.yahoo.com/technology/ai/articles/anthropic-revenue-surges-over-11-210857853.html): 11.500 millones de dólares en el segundo trimestre, catorce veces el mismo período de 2025, primer resultado operativo positivo y salida a bolsa prevista para el otoño boreal. La autoevaluación sigue siendo el único mecanismo de rendición de cuentas disponible, y la escribe la parte interesada. Para quien quiera leerlo completo, está el [PDF redactado de 186 páginas](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf), que cubre del 24 de febrero al 15 de julio de 2026.

## También hoy

- **[SpaceX cierra la compra de Cursor por 60.000 millones de dólares en acciones](https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/)** — Tras absorber a xAI, un mismo dueño concentra ahora modelo de frontera, flota de GPU y el editor de código con el que trabaja media región. Elegir asistente deja de ser una decisión técnica y pasa a ser una de dependencia.
- **[Los modelos Qwen superan los 3.000 millones de descargas y dejan atrás a Meta y Google sumados](https://fortune.com/2026/08/15/alibaba-qwen-open-ai-models-3-billion-downloads-meta-google/)** — Google registró 418 millones de descargas este año y Meta 227. Las cifras salen del [informe de Hugging Face sobre modelos abiertos](https://huggingface.co/blog/state-of-open-models-summer-2026), que no trae desglose por región.
- **[Una mujer se suma a la demanda contra xAI por 7.000 imágenes sexuales generadas con Grok a partir de una foto suya de los once años](https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/)** — La empresa restringió la función a suscriptores de pago en lugar de apagarla; el único remedio efectivo está en tribunales estadounidenses.
- **[Un adolescente acusado de matar a su madre y a su hermano usó ChatGPT horas antes para escribir la escena como ficción](https://www.cnn.com/2026/08/15/us/arjun-aravind-massachusetts-killing-chatgpt-hnk)** — Pedir en tercera persona lo que el sistema rechaza en primera: la laguna que discuten los proyectos regionales sobre acompañantes virtuales, ahora con expediente judicial.
- **[Libreros de segunda mano reciben pedidos de miles de ejemplares de compradores anónimos que no discuten precio](https://www.aol.co.uk/articles/secondhand-booksellers-uk-ireland-suspect-080051000.html)** — Único requisito: que el libro tenga ISBN. "Normalmente un pedido tiene un tema, pero esto está por todos lados", dice el dueño de Barter Books.
- **[Los robots humanoides expresivos generan vínculo más rápido y pierden más de la mitad de su influencia tras un solo error](https://theaiinsider.tech/2026/08/15/study-explores-impact-on-trust-when-expressive-humanoid-robots-make-mistakes/)** — Midieron oxitocina en saliva y actividad cerebral: la equivocación del robot que mira a los ojos se procesa como traición social, no como falla mecánica.

## En la región

Fin de semana sin publicaciones nuevas en los organismos multilaterales ni en los ministerios y autoridades de datos de la región. Lo que sigue corriendo viene de la semana pasada: la autoridad de protección de datos de Brasil mantiene el plazo de tres días hábiles que le dio a Discord el viernes para apagar las transmisiones en vivo bajo la nueva ley de protección de menores en entornos digitales, y el Ministerio de Ciencia y Tecnología brasileño anticipó que llevará el debate de soberanía de IA al Super Bots Experience de São Paulo, el 18 y 19 de agosto. Pero lo que de verdad mueve el tablero regional no se decidió acá: si los modelos abiertos chinos son hoy la vía de acceso dominante a capacidad de frontera, entonces la discusión latinoamericana sobre soberanía tecnológica se está dando sobre una infraestructura cuyo criterio de liberación se define en Hangzhou y cuya restricción se define en Washington. Ninguna de las dos conversaciones incluye a un actor de la región.

## Lanzamientos

- **[Qwen3.8-27B, variante FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)** — Modelo abierto de 27.000 millones de parámetros con codificador de visión integrado, 262.144 tokens de contexto nativo extensibles a un millón y licencia Apache 2.0. Es interesante porque es exactamente el tamaño que un laboratorio universitario o una agencia pública de la región puede correr en hardware propio, sin contrato de nube ni salida de datos del país. Un detalle a verificar antes de confiar en él: la ficha del modelo no declara cobertura de español ni de portugués.

## Hilos que seguimos

La demanda contra xAI por imágenes de abuso sexual infantil generadas con Grok venía sumando denunciantes desde hace semanas; la de hoy es la cuarta identificada como Jane Doe, y con ella ya son al menos seis acciones legales acumuladas contra la empresa en Estados Unidos y Reino Unido. El patrón se repite en cada capítulo: la respuesta de la empresa es restringir el acceso a la función, no eliminarla, y el único lugar donde la historia avanza es un tribunal fuera de la región. Ninguna autoridad de datos latinoamericana tiene hoy cómo ordenar nada sobre un caso así, aunque la foto de origen fuera de alguien que vive acá.

---

*Si el único mecanismo que existe para saber cómo se comporta un modelo de frontera es el informe que escribe la empresa que lo vende, y esa empresa acaba de dejar por escrito que sus propios instrumentos de medición perdieron precisión, ¿qué está regulando exactamente un legislador latinoamericano cuando escribe "el proveedor deberá evaluar los riesgos del sistema"?*

<small>**Sobre esta entrada.** Se genera de forma automática a partir de fuentes públicas, sin revisión humana antes de publicarse. Puede contener errores de interpretación o de resumen; conviene verificar cada noticia en su fuente original (los enlaces llevan ahí) antes de citarla o tomar decisiones a partir de ella.</small>
