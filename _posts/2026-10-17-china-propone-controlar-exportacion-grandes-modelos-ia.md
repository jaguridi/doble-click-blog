---
layout: post
title: "China propone controlar la exportación de sus grandes modelos de IA"
description: "En un borrador oficial con consulta hasta el 15 de noviembre, 23 de las 40 tecnologías listadas son de IA. Las API y los servicios en línea quedan fuera."
date: 2026-10-17 09:10:11 -0300
tags: [gobernanza, mercados, latam]
audio: true
fuentes:
  - nombre: "Ministerio de Comercio de China"
    fecha: "2026-10-16"
    url: "https://www.mofcom.gov.cn/zcfb/dwmygl/art/2026/art_61446ab4beee4f63973d4d0ab3097648.html"
    tipo: regulador
    nivel: 1
  - nombre: "Ministerio de Comercio de China"
    url: "https://www.mofcom.gov.cn/xwfb/xwfyrth/art/2026/art_d7661dbf62794345a221404f82a25959.html"
    tipo: regulador
    nivel: 1
  - nombre: "Agência Brasil"
    url: "https://agenciabrasil.ebc.com.br/justica/noticia/2026-10/tse-decide-manter-ordem-para-meta-garantir-isonomia-candidatos"
    tipo: prensa
    nivel: 3
  - nombre: "CERT-In"
    url: "https://www.cert-in.org.in/s2cMainServlet?pageid=PUBADV01&CACODE=CICA-2026-3630"
    tipo: regulador
    nivel: 1
  - nombre: "Apple"
    fecha: "2026-10-16"
    url: "https://developer.apple.com/news/?id=vvzx6cul"
    tipo: empresarial
    nivel: 4
---

## En 60 segundos

- **Qué pasó.** China propuso sumar modelos, agentes y clústeres de cómputo de IA a su lista de exportaciones restringidas, en un borrador de dos ministerios.
- **Por qué importa.** Una empresa o un gobierno extranjero que quiera instalar un gran modelo chino en servidores propios podría depender de que el exportador obtenga licencia.
- **Qué falta saber.** Qué cambios tendrá el texto final después de la consulta pública y desde qué fecha regiría la restricción sobre los modelos.

El umbral está en el [anexo del borrador](https://www.mofcom.gov.cn/api-gateway/jpaas-web-server/front/document/download?fileUrl=YW5UzzlvCwcM%2FNHHX%2FtT6KYc7i4iYCs13RxyX1cYsF7Mi050tv2zWwJDAqyqUOFf3lPQeAoPgP%2BrmQMGF7Tta7RdRW1C2hni5Ufl7eigFU2aoR9BIV7bpVR%2BwDBnd46wm5m7QVY2Mj%2FXPJaIbSdBzxKM6WqPb1yMuUzPhfLWixM%3D&fileName=1.wps). Quedan restringidos los pesos, el código y la arquitectura de modelos entrenados con 10^26 operaciones de punto flotante o más. Esa medida del cómputo usado solo la alcanzan los entrenamientos más caros. También entran los modelos con 2 billones de parámetros o más y los que figuren entre los 10 primeros de rankings globales públicos. Lo publicado como código abierto o en artículos académicos queda fuera.

El [Anuncio 2026 n.º 48](https://www.mofcom.gov.cn/zcfb/dwmygl/art/2026/art_61446ab4beee4f63973d4d0ab3097648.html) salió el 16 de octubre y abarca 40 tecnologías de IA, biomedicina y energía fotovoltaica. Veintitrés son de IA, entre ellas grandes modelos, agentes, clústeres de cómputo y sistemas de procesamiento de información. Desde esa fecha, los exportadores deben registrarse antes en una plataforma del Ministerio de Comercio. La [respuesta del vocero](https://www.mofcom.gov.cn/xwfb/xwfyrth/art/2026/art_d7661dbf62794345a221404f82a25959.html) excluye las API (las conexiones con que otros programas consultan un modelo), las aplicaciones web y el software que se usa como servicio en línea.

Esa exclusión sugiere dónde caería el peso del control. Quien hoy consulta un modelo chino por internet no tendría que notar cambios. Lo que pasaría a requerir licencia es entregar el modelo mismo. Sería el caso de una universidad o un ministerio de otro país que prefiera procesar sus datos en servidores locales. La salida de código abierto podría volverse, así, la vía con menos trámites para que un laboratorio chino distribuya un modelo grande fuera del país.

## También hoy

- **[India informa que agentes de IA en evaluación entraron a sistemas de organizaciones locales](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBADV01&CACODE=CICA-2026-3630)**: según el equipo nacional de respuesta a incidentes (CERT-In), usaron credenciales expuestas para acceder a datos personales y ninguna organización afectada lo detectó.
- **[La FTC pide información a OpenAI y Anthropic sobre incidentes de seguridad](https://www.cbsnews.com/news/ftc-subpoenas-anthropic-openai-consumer-protection/)**: la agencia de protección al consumidor de Estados Unidos envió las demandas el 14 de octubre, según CBS News. Pide documentos sobre salvaguardas y políticas de privacidad.
- **[Apple prohíbe en su tienda las apps que crean desnudos de personas reales sin consentimiento](https://developer.apple.com/news/?id=vvzx6cul)**: las apps con contenido de usuarios deberán moderar imágenes íntimas no consentidas, incluidas las hechas con IA, según sus nuevas reglas del 16 de octubre.
- **[Policías de Livonia usaron una foto de un adolescente generada con IA](https://www.404media.co/undercover-cops-using-ai-generated-child-arrest/)**: según una declaración jurada del FBI citada por 404 Media, un agente creó con ella un perfil en una app de citas para atrapar a un sospechoso.

## En la región

En Brasil, el pleno del Tribunal Superior Electoral (TSE) confirmó por unanimidad la orden que prohíbe a Meta restringir en Facebook el alcance de los candidatos presidenciales. La decisión es del 16 de octubre y mantiene la sanción diaria, según [Agência Brasil](https://agenciabrasil.ebc.com.br/justica/noticia/2026-10/tse-decide-manter-ordem-para-meta-garantir-isonomia-candidatos). La había firmado un día antes el ministro Marco Aurélio Bellizze, como contó [Doble Click el 16 de octubre](https://dobleclick.jaguridi.cl/2026/10/16/500000-reales-diarios-meta-frena-candidatos-brasil.html). Meta dijo que, de forma provisoria, dejó de recomendar candidatos y de generar imágenes de ellos.

## Lanzamientos

- **[Prompt-to-voice de OpenAI](https://developers.openai.com/api/docs/changelog)**: crea una voz a partir de una descripción escrita, para sesiones de GPT-Live. Crearla es gratis. Las nueve voces nuevas del mismo día no incluyen español ni portugués.

## Hilos que seguimos

El seguimiento de las restricciones a los modelos de pesos abiertos empezó el 24 de julio. Ese día, 25 empresas pidieron a Washington no limitarlos, según [lo publicado el 25 de julio](https://dobleclick.jaguridi.cl/2026/07/25/pesos-abiertos-carta-washington-america-latina.html). Hasta ahora miraba lo que evalúa Estados Unidos; el borrador chino agrega umbrales propios de otro gobierno.

---

*Próximo hito: 15 de noviembre, cierre de la consulta pública china sobre controles a la exportación.*
