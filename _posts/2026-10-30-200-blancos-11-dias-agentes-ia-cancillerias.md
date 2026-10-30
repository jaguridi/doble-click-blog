---
layout: post
title: "Más de 200 blancos en 11 días: agentes de IA llegan a cancillerías"
description: "CrowdStrike atribuye la campaña a VAPOR PANDA, con nexo en China, y describe intrusiones en dos ministerios latinoamericanos que no identifica. Por ahora, solo la empresa lo documenta."
date: 2026-10-30 09:34:11 -0300
tags: [agentes, seguridad, latam]
audio: true
fuentes:
  - nombre: "CrowdStrike"
    fecha: "2026-10-29"
    url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
    tipo: empresarial
    nivel: 4
  - nombre: "Cert.br"
    url: "https://internetsegura.br/pdf/guia-internet-segura.pdf"
    tipo: primaria
    nivel: 1
  - nombre: "DPL News"
    url: "https://dplnews.com/impacto-economico-inteligencia-artificial-argentina/"
    tipo: prensa
    nivel: 3
  - nombre: "Mistral AI"
    url: "https://mistral.ai/news/mistral-large-4-oss/"
    tipo: empresarial
    nivel: 4
  - nombre: "American Humanist Association"
    fecha: "2026-10-26"
    url: "https://americanhumanist.org/news/humanist-secures-workplace-accommodations-from-personal-ai-use-on-the-basis-of-his-beliefs/"
    tipo: empresarial
    nivel: 4
---

## En 60 segundos

- **Qué pasó.** Según CrowdStrike, VAPOR PANDA, un grupo con nexo en China, usó agentes de IA contra más de 200 organizaciones en 11 días.
- **Por qué importa.** Las cancillerías centroamericanas que el grupo preparó como blanco podrían revisar hoy sus redes con las huellas técnicas que el informe publica.
- **Qué falta saber.** Qué países sufrieron las intrusiones, si CrowdStrike avisó a los ministerios centroamericanos y si algún gobierno confirmará el ataque por su cuenta.

Una sola de las intrusiones consumió como entrada unos 1.400 millones de tokens. Cada token es un fragmento de texto que el modelo procesa y factura, así que la cifra refleja cuánto trabajo delegó el grupo en la máquina. El dato está en [el informe de CrowdStrike](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) del 29 de octubre. Desde el 17 de octubre, el grupo usó ARTEX, un marco de agentes de IA para intrusiones, en al menos 14 países. Los agentes funcionaron sobre todo con el modelo DeepSeek y con un segundo modelo comercial por suscripción. Un operador humano daba las instrucciones en chino.

Según la empresa, VAPOR PANDA hizo intrusiones extensas en los ministerios de Relaciones Exteriores de dos países latinoamericanos y probablemente comprometió una tercera cancillería. CrowdStrike no identifica esos países. En una cancillería latinoamericana halló BLOODALCHEMY, una puerta trasera: un programa que deja al atacante una vía oculta para volver a entrar. La firma confirmó actividad posterior al acceso en nueve organizaciones. El grupo también preparó archivos para atacar cancillerías de Centroamérica y de Asia. Todos estos detalles provienen solo de CrowdStrike, que vende servicios de ciberseguridad.

Al final del informe, CrowdStrike reúne los indicadores de compromiso del programa espía, las huellas técnicas que permiten buscar ese programa en los equipos propios. El texto no dice si la empresa avisó a las cancillerías centroamericanas que el grupo tenía en la mira. Sus equipos técnicos podrían cotejar esos indicadores con sus registros sin esperar un aviso. Esa revisión importa más en redes con vigilancia parcial. Según la firma, una de las órdenes del operador fue localizar máquinas que no tuvieran instalado su sensor.

## También hoy

- **[Mistral libera Mistral Large 4, un modelo de 1 billón de parámetros](https://mistral.ai/news/mistral-large-4-oss/)**: la empresa francesa publicó sus pesos, lo que permite ejecutarlo en servidores propios. Dice que es el mejor modelo abierto en programación y cobra 0,70 dólares cada millón de tokens que recibe su API.
- **[La Universidad de Kentucky exime a un administrador de usar IA por sus convicciones humanistas](https://americanhumanist.org/news/humanist-secures-workplace-accommodations-from-personal-ai-use-on-the-basis-of-his-beliefs/)**: la American Humanist Association informó el 26 de octubre que la universidad aprobó el 25 de septiembre que David Durman no use IA personalmente en su trabajo.

## En la región

En Brasil, el Cert.br, centro de respuesta a incidentes ligado a NIC.br, publicó la tercera edición de su [guía Internet Segura para niños](https://internetsegura.br/pdf/guia-internet-segura.pdf). Suma secciones sobre IA y deepfakes, los videos o imágenes falsos que imitan a personas reales. La edición anterior era de [octubre de 2022](https://internetsegura.br/criancas/sobre/).

En Argentina, un estudio de la Universidad de San Andrés calcula que la IA tendría en 2030 un impacto económico de hasta 17.714 millones de dólares. El monto equivale a 2,1% del PIB y corresponde a un escenario de aceleración. El escenario base da 12.707 millones, según [DPL News](https://dplnews.com/impacto-economico-inteligencia-artificial-argentina/) (vía DPL News).

## Hilos que seguimos

Los ataques con agentes de IA, que seguimos desde el 16 de julio, suman una campaña de espionaje dirigido. Según CrowdStrike, ARTEX ya había aparecido en manos de actores con fines económicos o sin atribuir. La firma separa a VAPOR PANDA de la campaña que Microsoft atribuyó a Storm-0940 el 21 de octubre. Otro informe de CrowdStrike, sobre agentes usados contra entidades sanitarias de Argentina, se contó [el 26 de octubre](https://dobleclick.jaguridi.cl/2026/10/26/atacante-agentes-claude-entidades-salud-argentinas.html).
