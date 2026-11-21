---
layout: post
title: "Un matemático de Anthropic dice haber probado Riemann con Claude"
description: "Andrew Sutherland ya revisó la prueba en Lean, según Scientific American; Kevin Buzzard espera otra comprobación. La historia se apoya en prensa y en el texto del autor."
date: 2026-11-21 10:06:09 -0300
tags: [educación, defensa, latam]
audio: true
fuentes:
  - nombre: "Levent Alpöge"
    fecha: "2026-11-20"
    url: "https://alpo.ge/remark.pdf"
    tipo: primaria
    nivel: 1
  - nombre: "Scientific American"
    url: "https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/"
    tipo: prensa
    nivel: 3
  - nombre: "Ravi Vakil"
    fecha: "2026-11-20"
    url: "https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/"
    tipo: investigacion
    nivel: 2
  - nombre: "Banca y Negocios"
    url: "https://www.bancaynegocios.com/venezuela-iniciara-gestiones-para-desbloquear-plataformas-internacionales-de-inteligencia-artificial/"
    tipo: prensa
    nivel: 3
  - nombre: "TRT World"
    url: "https://www.trtworld.com/article/163d51308f05"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** Levent Alpöge, matemático de Anthropic, afirma haber demostrado con Claude la hipótesis de Riemann, planteada en 1859, y su versión generalizada.
- **Por qué importa.** Sin un texto legible, aceptar el resultado depende por ahora de unos pocos especialistas en Lean y de pruebas automáticas, no de una revista.
- **Qué falta saber.** Cuándo aparecerá la versión que puedan leer los matemáticos y si alguna revista especializada la someterá a evaluación de pares.

Andrew Sutherland, del Instituto Tecnológico de Massachusetts (MIT), compiló la prueba y la pasó por el núcleo de Lean usando solo los tres axiomas estándar. El núcleo es la parte del programa que acepta o rechaza cada paso de una demostración. Lo informa [Scientific American](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/). En la misma nota, Kevin Buzzard, del Imperial College London, dijo que aún espera una corrida exitosa del comparador. Esa revisión descarta atajos que cambien el sentido del enunciado: una prueba correcta de una afirmación distinta no resolvería el problema.

La hipótesis de Riemann es uno de los problemas del milenio. Alpöge publicó su [texto](https://alpo.ge/remark.pdf) el 20 de noviembre. Ahí dice que la prueba está formalizada en Lean, un lenguaje en que una computadora verifica cada paso, y que por ahora solo existe así. Según ese mismo documento, habló con Dario Amodei antes de hacerlo público. Que el autor trabaje en la empresa que creó el modelo usado sugiere que la revisión de académicos de otras instituciones debería pesar más que de costumbre.

En la práctica, el juicio sobre el resultado quedaría en manos de quienes saben auditar ese código. Para las revistas, eso podría invertir el orden de costumbre: el veredicto técnico llegaría antes que el artículo. El mismo día, Ravi Vakil difundió en su [blog](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) una prueba humana de la versión generalizada, de Alessandro Masullo. Horas después informó que le habían señalado problemas. En octubre, OpenAI había publicado [722 manuscritos de un modelo interno](https://dobleclick.jaguridi.cl/2026/10/07/722-manuscritos-modelo-openai-162-prueba-formal.html), de los cuales 162 traían prueba formal.

## También hoy

- **[El Nasdaq 100 cae 5,6% y cierra su peor semana desde marzo de 2020](https://www.swissinfo.ch/eng/nasdaq-100-has-worst-week-since-2020-on-ai-drama:-markets-wrap/92410554)**: según Bloomberg, Nvidia bajó 14% el 20 de noviembre tras un reporte de Reuters sobre una investigación de reguladores a sus prácticas contables.
- **[METR estima en unas 40 horas el horizonte temporal de GPT-6 Astra](https://metr.org/blog/2026-11-20-q4-2026-capability-update/)**: esa medida indica cuán largas son las tareas que un modelo completa. La organización evaluadora calcula que se duplica cada 3,6 meses, con intervalos de confianza muy amplios.
- **[OpenAI detalla sus defensas contra la destilación adversarial](https://openai.com/index/combatting-adversarial-distillation)**: es el uso de respuestas de un modelo para entrenar una copia. La empresa dice que el éxito de un ataque para extraer razonamiento bajó de 54,0% a 0,2% entre GPT-6 Astra y GPT-6.2 Astra.
- **[Anthropic cierra su oferta pública inicial](https://www.anthropic.com/news/ipo-close)**: vendió 1.127 millones de acciones a 83 dólares, unos 93.500 millones brutos, según la empresa. El precio se contó [el 19 de noviembre](https://dobleclick.jaguridi.cl/2026/11/19/anthropic-sale-bolsa-83-dolares-sobre-rango.html).

## En la región

En Venezuela, Delcy Rodríguez habló el 20 de noviembre ante emprendedores. Dijo que instruyó al canciller Oliver Blanco a gestionar el desbloqueo total de ChatGPT, Copilot y Claude, según la agencia [EFE](https://www.bancaynegocios.com/venezuela-iniciara-gestiones-para-desbloquear-plataformas-internacionales-de-inteligencia-artificial/). Las aplicaciones muestran en el país un aviso de servicio no disponible, y el despacho no establece la causa del bloqueo.

En Uruguay, el Instituto Nacional de Empleo y Formación Profesional (Inefop) presentó el 18 de noviembre Serena, un asistente que transcribirá entrevistas y ayudará a preparar informes de orientación laboral. Lo desarrolló el Laboratorio Tecnológico del Uruguay con la empresa Automics y fondos de la Agencia Nacional de Investigación e Innovación. Se habilitará en 2027, según un [reporte](https://dplnews.com/uruguay-inefop-incorporara-inteligencia-artificial-para-fortalecer-la-orientacion-educativo-laboral-2/) (vía DPL News).

## Lanzamientos

- **[Inkling 2 Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)**: modelo multimodal de Thinking Machines, con pesos abiertos (se puede descargar), bajo licencia Apache 2.0. Pesa unos 20 GB y corre en un equipo con 32 GB de memoria, sin depender de un servicio externo.

## Hilos que seguimos

La Convención sobre Ciertas Armas Convencionales, cuyo debate sobre armas autónomas se sigue desde el 7 de septiembre, ya tiene resultado. La conferencia de Ginebra terminó por consenso el 21 de noviembre con un mandato para "elaborar" en dos años un instrumento sobre estas armas. El texto evita la palabra "negociar", que algunos países objetaron, según la agencia AFP en una [nota](https://www.trtworld.com/article/163d51308f05) (vía TRT World). Las definiciones acordadas sin obligaciones se contaron [el 7 de septiembre](https://dobleclick.jaguridi.cl/2026/09/07/primer-acuerdo-global-armas-autonomas.html).
