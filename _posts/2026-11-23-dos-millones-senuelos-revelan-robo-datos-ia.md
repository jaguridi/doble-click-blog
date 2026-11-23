---
layout: post
title: "Dos millones de señuelos revelan robo de datos en servicios de IA"
description: "Tras la investigación de la firma Dragos, OpenRouter dio de baja a tres proveedores y sacó 125 puntos de acceso de su categoría sin retención de datos."
date: 2026-11-23 10:07:54 -0300
tags: [datos, seguridad, infraestructura, latam]
audio: true
fuentes:
  - nombre: "Dragos"
    fecha: "2026-11-19"
    url: "https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens"
    tipo: investigacion
    nivel: 2
  - nombre: "OpenRouter"
    fecha: "2026-11-22"
    url: "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/"
    tipo: empresarial
    nivel: 4
  - nombre: "Novita"
    url: "https://novita.ai/blog/minimax-requests-privacy-notice/"
    tipo: empresarial
    nivel: 4
  - nombre: "The Gleaner"
    fecha: "2026-11-16"
    url: "https://jamaica-gleaner.com/article/news/20261116/opposition-calls-disclosure-ai-infrastructure-mou-wants-document-tabled"
    tipo: prensa
    nivel: 3
  - nombre: "Somos Uruguay"
    fecha: "2026-11-19"
    url: "https://somosuruguay.com.uy/politicas-publicas/ceibal-anep-habilitaron-herramienta-ia-preparar-pruebas-acredita-n3669"
    tipo: prensa
    nivel: 3
---

## En 60 segundos

- **Qué pasó.** Dragos envió cerca de dos millones de prompts con credenciales señuelo y halló robo de datos en al menos tres proveedores de IA.
- **Por qué importa.** Si la etiqueta de retención cero falla ante un intruso, quien contrata estos servicios solo controla de verdad lo que escribe en sus prompts.
- **Qué falta saber.** Cuántos clientes quedaron expuestos y cuándo empezará OpenRouter a correr de forma continua las pruebas con señuelos que anunció.

Entre julio y noviembre, cada prompt que envió Dragos llevaba una URL y unas credenciales únicas. Funcionan como trampas: si alguien las usa, delatan de qué servicio salieron. Según su [informe](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) del 19 de noviembre, las claves señuelo de AWS, la nube de Amazon, se usaron en decenas de miles de llamadas. Los tres proveedores donde halló atacantes no lo sabían. Los proveedores de inferencia son los que ejecutan un modelo y devuelven su respuesta. Dragos también detectó revendedores de un mercado de inferencia que leían los prompts de sus clientes con registros estándar.

OpenRouter reparte pedidos de API, las conexiones con que un programa usa un modelo, entre esos proveedores. El 22 de noviembre dio de baja a tres de ellos, según su [comunicado](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/). También retiró 125 endpoints, los puntos de acceso a cada modelo, de su categoría de retención cero de datos, la que promete no guardar los pedidos. Por separado, [Novita](https://novita.ai/blog/minimax-requests-privacy-notice/) informó que pedidos a modelos de MiniMax enviados entre el 28 de mayo y el 11 de noviembre pudieron terminar en poder de un tercero.

Según Dragos, dos de esas intrusiones alcanzaron pedidos que tenían la marca de retención cero. Eso sugiere que la etiqueta describe lo que el proveedor promete guardar, no lo que un intruso puede leer. Una empresa que contrata modelos a bajo costo por un intermediario podría protegerse sobre todo de un modo: dejar las claves fuera de sus prompts y cambiar las ya expuestas. OpenRouter dijo también que convertirá esos señuelos en una prueba permanente. Si lo hace, la privacidad de cada proveedor podría verificarse desde fuera, y no solo por su propia palabra.

## También hoy

- **[La bolsa de Seúl cae más de 4% por la venta de acciones ligadas a la IA](https://koreatimes.co.kr/economy/others/20261123/seoul-shares-extend-losses-late-monday-morning-on-ai-driven-tech-sell-off)**: según Yonhap, el Kospi caía 4,33% a 4.659,33 puntos el 23 de noviembre, con Samsung Electronics y SK hynix a la cabeza.
- **[El científico jefe de OpenAI publica la perplejidad interna de sus modelos desde GPT-3.5](https://openai.com/index/perplexity-and-intelligence)**: esa métrica mide cuán bien un modelo predice texto. Jakub Pachocki propone usarla para comparar desarrolladores e informar estándares de seguridad compartidos.
- **[Renuncia el ministro de Educación de Corea del Sur por las medidas contra el fraude con IA en el examen de ingreso](https://www.koreajoongangdaily.com/korea/lee-accepts-education-ministers-resignation-after-csat-anticheating-measures-trigger-nationwide-confusion/12984387)**: el presidente Lee Jae Myung aceptó el 22 de noviembre la renuncia de Choi Kyo-jin, según Korea JoongAng Daily.

## En la región

En Jamaica, el primer ministro Andrew Holness anunció el 15 de noviembre, sin detalles, un memorándum con inversionistas extranjeros para explorar infraestructura de IA. El portavoz opositor Christopher Brown, del PNP, pidió el 16 que el texto se presente al Parlamento, según [The Gleaner](https://jamaica-gleaner.com/article/news/20261116/opposition-calls-disclosure-ai-infrastructure-mou-wants-document-tabled). También pidió no firmar más acuerdos antes de una política nacional de IA con salvaguardas de energía, agua y ambiente.

En Uruguay, Ceibal y la Administración Nacional de Educación Pública (ANEP) abrieron una plataforma con asistente de IA para preparar las pruebas Acredita de bachillerato. Unas 22.000 personas las rendirán entre el 28 de noviembre y el 5 de diciembre, según Presidencia, citada por una [nota](https://somosuruguay.com.uy/politicas-publicas/ceibal-anep-habilitaron-herramienta-ia-preparar-pruebas-acredita-n3669) (vía Somos Uruguay).

## Lanzamientos

- **[Monitor API de Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexitys-monitor-api)**: vigila búsquedas web o hasta 10 páginas con un calendario fijo y avisa a un agente solo cuando hay cambios relevantes. Se usa desde la API de Perplexity, que la propone para seguir avisos de reguladores.

## Hilos que seguimos

El caso de Nvidia y Jensen Huang, abierto el 7 de noviembre y contado [el 9 de noviembre](https://dobleclick.jaguridi.cl/2026/11/09/nvidia-investiga-relacion-huang-posible-espia-china.html), suma un giro. El secretario del Tesoro, Scott Bessent, no descartó en CBS el 22 de noviembre el regreso de Huang, según una [nota](https://investinglive.com/stocks/bessent-leaves-door-open-to-huang-return-at-nvidia-a-week-after-urging-an-outside-ceo/) (vía investingLive). Lo dijo una semana después de pedir un director ejecutivo externo y agregó que el gobierno aún no recibe las respuestas que pidió.

---

*Próximo hito: 25 de noviembre, vence el plazo de 10 días que Scott Bessent fijó el 15 de noviembre en el caso Nvidia.*
