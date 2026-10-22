---
layout: post
title: "PHP corrige dos fallas críticas que exponen a los servidores web"
description: "La salida del 21 de octubre se adelantó un día porque los identificadores circularon en foros, según la PHP Foundation. Al divulgarse, no se conocían ataques funcionales."
date: 2026-10-22 09:10:09 -0300
tags: [seguridad, latam]
audio: true
fuentes:
  - nombre: "PHP Foundation"
    fecha: "2026-10-21"
    url: "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/"
    tipo: primaria
    nivel: 1
  - nombre: "PHP"
    url: "https://www.php.net/archive/2026.php#2026-10-20-1"
    tipo: primaria
    nivel: 1
  - nombre: "Microsoft"
    fecha: "2026-10-21"
    url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
    tipo: empresarial
    nivel: 4
  - nombre: "Secretaría de Gobierno y Transformación Digital del Perú"
    fecha: "2026-10-19"
    url: "https://cdn.www.gob.pe/uploads/document/file/10829158/8743150-resolucion-de-secretaria-de-gobierno-y-transformacion-digital-n-004-2026-pcm-sgtd%282%29.pdf"
    tipo: regulador
    nivel: 1
  - nombre: "Ministério Público Federal"
    fecha: "2026-10-21"
    url: "https://www.mpf.mp.br/o-mpf/unidades/pr-rs/noticias/mpf-aciona-a-justica-para-barrar-bloqueios-e-restricoes-arbitrarias-praticados-pela-meta-em-redes-sociais"
    tipo: regulador
    nivel: 1
---

## En 60 segundos

- **Qué pasó.** El proyecto PHP publicó cuatro versiones que corrigen dos vulnerabilidades críticas con las que un atacante sin credenciales puede ejecutar código en un servidor.
- **Por qué importa.** Quien mantiene sitios en PHP 8.1 o anterior ya no recibe actualizaciones del proyecto y tiene que conseguir la corrección por su cuenta.
- **Qué falta saber.** Si aparecerán ataques que aprovechen estas fallas ahora que son públicas, y cuántos sitios siguen en versiones sin soporte.

El 11 de agosto, la firma Calif, que auditaba PHP dentro del programa Patch the Planet, reportó una ejecución remota de código, según [la PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). OpenAI informó la misma causa ese día y Wiz sumó otras formas de ataque. Las correcciones salieron el 21 de octubre en las versiones 8.5.12, 8.4.27, 8.3.36 y 8.2.35. Según la fundación, desde el 1 de julio se publicaron 15 CVE (identificadores públicos de vulnerabilidades). También recibió más de 100 reportes que resultaron inválidos o repetidos, y busca fondos de empresas, gobiernos y firmas de alojamiento web.

El calendario se rompió antes de tiempo. Los identificadores de las fallas circularon en foros el 20 de octubre, y el proyecto adelantó un día la publicación. Chainguard publicó su parche más de seis horas antes de la hora coordinada, según la fundación. Al divulgarse las fallas, el equipo de seguridad no había identificado programas capaces de aprovecharlas en la práctica.

El [aviso de php.net](https://www.php.net/archive/2026.php#2026-10-20-1) dice que están en riesgo todas las instalaciones que atienden solicitudes web y que PHP 8.1 y anteriores ya no reciben actualizaciones del proyecto. Esas versiones tienen tres salidas. Una es la distribución que instaló PHP y otra, una empresa que venda soporte extendido. La tercera son parches reducidos para PHP 7.4 a 8.1, que los encargados de seguridad del proyecto dejaron listos para compilarlos uno mismo. Cada camino supone un costo, ya sea un contrato o alguien capaz de compilar. Eso sugiere que el peso de esta corrección podría caer sobre todo en quien no actualizó a tiempo.

## También hoy

- **[Microsoft atribuye a un actor alineado con el Estado chino una campaña con agentes de IA](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)**: según la empresa, Storm-0940 usó el marco abierto ARTEX y, tras comprometer ConnectWise, intentó entrar a más de 2.250 organizaciones en Microsoft 365.
- **[Los anuncios de ChatGPT llegan a 26 países nuevos](https://openai.com/index/chatgpt-ads-expands-26-new-countries)**: entre ellos están Argentina, Chile, Colombia y Perú, en los planes Gratis y Go, según [Infobae](https://www.infobae.com/tecno/2026/10/21/chatgpt-ahora-tiene-publicidad-argentina-chile-colombia-y-peru-tendran-anuncios-con-dos-versiones-de-la-ia/). OpenAI dice que más de 100.000 anunciantes usaron su plataforma.
- **[Mujeres generadas con IA aparecen en actos de Flávio Bolsonaro para vender contenido adulto](https://www.agencialupa.org/noticias/2026/10/20/perfis-eroticos-de-ia-usam-videos-em-atos-de-flavio-bolsonaro-para-atrair-seguidores-e-vender-conteudo-adulto/)**: Agência Lupa halló dos cuentas de Instagram con más de 1,7 millones de seguidores. No encontró vínculo con la campaña.

## En la región

En Perú, la Secretaría de Gobierno y Transformación Digital aprobó la directiva que fija el perfil y las responsabilidades del Oficial de Inteligencia Artificial en las entidades públicas. Lo hizo con la [Resolución N° 004-2026-PCM/SGTD](https://cdn.www.gob.pe/uploads/document/file/10829158/8743150-resolucion-de-secretaria-de-gobierno-y-transformacion-digital-n-004-2026-pcm-sgtd%282%29.pdf), firmada el 19 de octubre. El perfil será exigible 12 meses después de la entrada en vigencia, y cada entidad lo paga con su propio presupuesto.

En Paraguay, Crusoe y Araico firmaron una alianza para cómputo de IA con energía de Itaipú, según [el Departamento de Estado de Estados Unidos](https://www.state.gov/releases/office-of-the-spokesman/2026/10/u-s-paraguay-cooperation-to-advance-prosperity-and-security). Su primera fase operaría a mediados de 2027. No se informaron el monto ni la energía asignada.

## Lanzamientos

- **[Flint](https://recursive.com/updates/introducing-recursive-flint)**: modelo de Recursive para programar con agentes en equipos locales, sin enviar el código a la nube. Según TechCrunch, se descarga gratis en Hugging Face con licencia Apache 2.0.

## Hilos que seguimos

La demanda contra Meta por bloqueos automatizados, que [el 18 de octubre](https://dobleclick.jaguridi.cl/2026/10/18/brasil-meta-revise-personas-antes-suspender-cuentas.html) era una propuesta del Ministerio de Justicia de Brasil, ya está en un juzgado. La [Procuraduría en Rio Grande do Sul](https://www.mpf.mp.br/o-mpf/unidades/pr-rs/noticias/mpf-aciona-a-justica-para-barrar-bloqueios-e-restricoes-arbitrarias-praticados-pela-meta-em-redes-sociais) la presentó el 21 de octubre ante la 26ª Vara Federal de Porto Alegre. Pide prohibir los bloqueos decididos solo por algoritmos, con una multa de 500.000 reales por cuenta y por día. El seguimiento empezó el 25 de mayo.
