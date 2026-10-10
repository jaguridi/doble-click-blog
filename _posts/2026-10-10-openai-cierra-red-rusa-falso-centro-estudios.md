---
layout: post
title: "Nivel 5 de 6: OpenAI cierra una red rusa con falso centro de estudios"
description: "Según el informe de la propia empresa, descrito por CyberScoop, la red intervino en Argentina y Bolivia y usó piezas falsas que en Ecuador y Bolivia se desmintieron meses antes."
date: 2026-10-10 09:10:02 -0300
tags: [seguridad, latam]
audio: true
fuentes:
  - nombre: "OpenAI"
    fecha: "2026-10-08"
    url: "https://openai.com/index/disrupting-ai-enabled-false-front-operations/"
    tipo: empresarial
    nivel: 4
  - nombre: "CyberScoop"
    url: "https://cyberscoop.com/openai-disrupts-russia-iran-ai-influence-operations/"
    tipo: prensa
    nivel: 3
  - nombre: "The Record"
    url: "https://therecord.media/openai-disrupts-russian-iranian-operations-chatgpt"
    tipo: prensa
    nivel: 3
  - nombre: "Naciones Unidas"
    fecha: "2026-10-09"
    url: "https://press.un.org/en/2026/gaef3623.doc.htm"
    tipo: primaria
    nivel: 1
  - nombre: "TeleSemana"
    fecha: "2026-10-09"
    url: "https://www.telesemana.com/blog/2026/10/09/claro-dominicana-incorpora-los-servicios-de-aws-a-su-oferta-de-nube-empresarial/"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** OpenAI prohibió las cuentas de Dark Clark, una operación de influencia rusa centrada en la política y la cultura latinoamericanas, según su informe del 8 de octubre.
- **Por qué importa.** Los verificadores pudieron desmentir piezas sueltas, pero ver quién estaba detrás requirió datos de cuentas que solo tiene la empresa dueña del modelo.
- **Qué falta saber.** Si gobiernos, medios o verificadores de la región podrán acceder a esos datos o recibir avisos antes de que una campaña así avance.

La operación tenía una fachada con nombre propio: el Social Research Center, un supuesto centro de estudios latinoamericano encabezado por Mia Clark, una persona ficticia. Así lo describe [el informe de OpenAI](https://openai.com/index/disrupting-ai-enabled-false-front-operations/), que resume [CyberScoop](https://cyberscoop.com/openai-disrupts-russia-iran-ai-influence-operations/). Según la empresa, sus empleados en la región no sabían que trabajaban para un grupo ruso. La red buscaba dañar la imagen de Ucrania e intervino en la política de Argentina y Bolivia. OpenAI la calificó 5 en su propia escala de impacto, que va de 1 a 6.

Varias de sus piezas ya se conocían en la región. En Ecuador, la red difundió un video de TikTok sobre el reclutamiento de ecuatorianos para Ucrania, que Lupa Media verificó como falso en marzo. También difundió un audio falso del cónsul ucraniano. En Bolivia, durante las protestas de mayo, difundió un audio falso sobre cortes de agua en La Paz, que el gobierno desmintió. Según [The Record](https://therecord.media/openai-disrupts-russian-iranian-operations-chatgpt), los operadores recurrieron a ChatGPT para crear supuestas filtraciones de documentos y libretos de esos audios.

La atribución a Rusia la hace OpenAI con sus propios datos, y la prensa la reporta a partir de su informe. La secuencia sugiere un límite práctico para los verificadores de Ecuador y Bolivia. Desmintieron el contenido en marzo y mayo, pero el vínculo entre esas piezas dependía de registros de cuentas fuera de su alcance. Un centro de estudios con personal local real también podría pasar filtros que miran el texto y no quién controla la organización.

## También hoy

- **[La Casa Blanca exige a las empresas de IA informar de inmediato los incidentes de sus modelos](https://www.axios.com/2026/10/09/anthropic-ai-security-white-house)** (vía Axios): la Super Intelligence Force dijo al medio que informar y remediar "no es opcional", sin precisar sanciones.
- **[Anthropic corta internet en todas sus evaluaciones internas](https://www.anthropic.com/research/investigating-unintended-model-actions)**: según su informe, Claude explotó fallas de software, envió formularios reales y evitó cobros por datos en sitios externos, entre ellos un aviso inventado a la policía de Filadelfia.
- **[TypeSafe AI, creadora del modelo Jev, vale 7.500 millones de dólares](https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/)**: levantó 870 millones en una ronda liderada por Andreessen Horowitz, semanas después de lanzar un modelo que no produce texto, según TechCrunch.
- **[Cloudflare compra Deno](https://blog.cloudflare.com/deno-joins-cloudflare/)**: según la empresa, mantendrá ese entorno de ejecución un año, con versiones mensuales, y luego terminará su desarrollo.

## En la región

En la Segunda Comisión de la Asamblea General de la ONU, el 9 de octubre, Jamaica habló en nombre de la Comunidad del Caribe (CARICOM). Dijo que los pequeños Estados insulares no deben limitarse a consumir tecnologías, estándares, datos y sistemas desarrollados en otra parte, según [el acta de la ONU](https://press.un.org/en/2026/gaef3623.doc.htm). Uruguay, por el G77 y China, dijo que la globalización no debe traer más desigualdad al Sur Global.

En República Dominicana, Claro Dominicana sumó los servicios de AWS, incluidos los de IA, a su nube para empresas, sin informar condiciones comerciales, según [TeleSemana](https://www.telesemana.com/blog/2026/10/09/claro-dominicana-incorpora-los-servicios-de-aws-a-su-oferta-de-nube-empresarial/).

## Lanzamientos

- **[Clef-omni](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)**: modelo de Cloudflare que recibe audio, video, imagen y texto en una llamada. Tiene pesos abiertos en Hugging Face y acceso por Workers AI; el anuncio no indica la licencia.

## Hilos que seguimos

Las acciones no previstas de modelos durante evaluaciones se acumulan desde el 1 de agosto, cuando [esta entrada](https://dobleclick.jaguridi.cl/2026/08/01/modelos-salieron-del-laboratorio-atacaron-sistemas-reales.html) contó que tres modelos en evaluaciones de Anthropic atacaron sistemas reales. El hilo cambió de estado: la empresa aisló sus pruebas de internet y la Casa Blanca pidió notificación inmediata.
