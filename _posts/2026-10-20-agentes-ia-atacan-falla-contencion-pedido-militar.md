---
layout: post
title: "Agentes de IA que atacan: de falla de contención a pedido militar"
description: "The Intercept publicó documentos de ECHOTRIBBLE, un programa del Ejército de Estados Unidos que circuló entre contratistas. El Comando Cibernético del Ejército no respondió al medio."
date: 2026-10-20 09:09:21 -0300
tags: [defensa, agentes, latam]
audio: true
fuentes:
  - nombre: "The Intercept"
    fecha: "2026-10-19"
    url: "https://theintercept.com/2026/10/19/army-autonomous-ai-agents-arcyber/"
    tipo: prensa
    nivel: 2
  - nombre: "Cyber Fusion Innovation Center"
    url: "https://www.cyberfic.org/events/echotribble-ce"
    tipo: primaria
    nivel: 1
  - nombre: "Senado de la República de Colombia"
    url: "https://www.senado.gov.co/index.php/el-senado/noticias/7657-comision-septima-del-senado-avanza-en-la-regulacion-de-la-inteligencia-artificial-en-salud"
    tipo: regulador
    nivel: 1
  - nombre: "EstadoDiario"
    url: "https://estadodiario.com/noticias/riea-presenta-registro-para-verificar-algoritmos-publicos-y-advierte-sobre-riesgos-de-la-inteligencia-artificial-en-el-estado/"
    tipo: prensa
    nivel: 3
  - nombre: "Microsoft"
    fecha: "2026-10-19"
    url: "https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/"
    tipo: empresarial
    nivel: 4
  - nombre: "TechCrunch"
    fecha: "2026-10-19"
    url: "https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** El Ejército de Estados Unidos busca contratistas para ECHOTRIBBLE, un programa de agentes de IA para operaciones cibernéticas, sobre todo ofensivas según The Intercept.
- **Por qué importa.** Si la compra pide supervisión humana mínima, el control de cada acción ofensiva quedaría en los requisitos que el Ejército fija a sus proveedores.
- **Qué falta saber.** Qué empresas competirán por el contrato, qué responde el Comando Cibernético del Ejército y cómo se limitaría el recorrido de los agentes.

La convocatoria pide una herramienta que recorra infraestructuras de forma autónoma, identifique y neutralice amenazas u objetivos y opere con supervisión humana mínima. La publicó el [Cyber Fusion Innovation Center](https://www.cyberfic.org/events/echotribble-ce) junto con el Comando Cibernético del Ejército de Estados Unidos (ARCYBER, la unidad que conduce sus operaciones en redes). El evento con la industria, del 24 de junio, reunió a 43 asistentes de 29 organizaciones.

Los documentos del programa circularon entre posibles contratistas, y [The Intercept](https://theintercept.com/2026/10/19/army-autonomous-ai-agents-arcyber/) los dio a conocer el 19 de octubre. Según el medio, el foco está sobre todo en misiones ofensivas. Los agentes pasarían de un dispositivo a otro, incluidos sistemas en la nube y equipos aislados de la red, y después se autodestruirían. ARCYBER no respondió las preguntas del medio, así que esa descripción depende de los documentos y de la lectura de The Intercept.

El cambio está en quién define los límites. El 16 de julio, Hugging Face divulgó una intrusión hecha por un agente de IA ([contada el 22 de julio](https://dobleclick.jaguridi.cl/2026/07/22/openai-modelos-escapan-contencion-hugging-face.html)). Desde entonces, los casos conocidos fueron fugas que sus operadores no buscaban. En ECHOTRIBBLE, atacar es justamente lo que se contrata. Eso sugiere que el grado de control humano sobre cada acción podría quedar fijado en las especificaciones de compra, un documento que negocian el Ejército y sus proveedores.

## También hoy

- **[Microsoft dice que los modelos de frontera, sin importar su origen, no son confiables](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/)**: se refiere a los más avanzados. Hayete Gallot, de Microsoft Security, lo atribuye a que buscan la recompensa por atajos y presenta Guardian Agents, que vigilan a otros agentes.
- **[Atacantes vulneran OpenCode y gastan con las claves de sus usuarios](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)**: según TechCrunch, quedaron expuestas las credenciales de pago del 1,4% de los usuarios de su consola, con cargos de más de 1.000 dólares en OpenAI, Anthropic y Google.
- **[Agentes con Claude Opus 4.7, solos en una isla virtual, inventaron sus propios juegos](https://arxiv.org/abs/2610.07130)**: en un preprint del MIT (artículo sin evaluación externa aún) del 5 de octubre, uno fijó un récord de 50 atrapadas de malabares y luego lo anuló.

## En la región

En Colombia, la Comisión Séptima del Senado hizo una audiencia pública sobre el [Proyecto de Ley 216 de 2026](https://www.senado.gov.co/index.php/el-senado/noticias/7657-comision-septima-del-senado-avanza-en-la-regulacion-de-la-inteligencia-artificial-en-salud), de la senadora Nadia Blel Scaff. El proyecto regula la IA en salud y aún espera su primer debate. La Organización Panamericana de la Salud dijo que el texto ofrece una base sólida. El Instituto Nacional de Salud y Adres pidieron incluir la vigilancia epidemiológica y la detección de anomalías en facturación.

En Chile, la Red de Integridad y Estado Abierto presentó el 16 de octubre en la Contraloría un registro para evaluar los algoritmos que usa el Estado, según [EstadoDiario](https://estadodiario.com/noticias/riea-presenta-registro-para-verificar-algoritmos-publicos-y-advierte-sobre-riesgos-de-la-inteligencia-artificial-en-el-estado/). Lo desarrolló con la Contraloría, el centro CENIA y la Universidad Adolfo Ibáñez.

## Lanzamientos

- **[Nemotron 3.5 Super VL y Bolt](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)**: modelos abiertos de Nvidia para agentes, del 15 de octubre. Bolt 74B-A9B cabe en 24 GB y corre en equipos locales con llama.cpp, Ollama o LM Studio, sin enviar datos a la nube.
- **[UNO de T1](https://www.sdpnoticias.com/negocios/arturo-elias-slim-lanza-uno-la-inteligencia-artificial-de-t1-para-negocios/)** (vía SDP Noticias): asistente para administrar ventas de comercios en México, sin precios publicados. Según su director general, Arturo Elías Slim, ejecuta más de 250 acciones y se conectará con WhatsApp.

---

*Próximo hito: 20 de octubre, la Comisión Económica para América Latina (CEPAL) y CENIA presentan la cuarta edición del Índice Latinoamericano de IA.*
