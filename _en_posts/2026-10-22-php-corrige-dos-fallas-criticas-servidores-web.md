---
layout: post
title: "PHP fixes two critical flaws that expose web servers"
description: "The October 21 release was moved up a day because the identifiers circulated on forums, according to the PHP Foundation. At disclosure, no working attacks were known."
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
  - nombre: "Peru's Secretariat of Government and Digital Transformation"
    fecha: "2026-10-19"
    url: "https://cdn.www.gob.pe/uploads/document/file/10829158/8743150-resolucion-de-secretaria-de-gobierno-y-transformacion-digital-n-004-2026-pcm-sgtd%282%29.pdf"
    tipo: regulador
    nivel: 1
  - nombre: "Ministério Público Federal"
    fecha: "2026-10-21"
    url: "https://www.mpf.mp.br/o-mpf/unidades/pr-rs/noticias/mpf-aciona-a-justica-para-barrar-bloqueios-e-restricoes-arbitrarias-praticados-pela-meta-em-redes-sociais"
    tipo: regulador
    nivel: 1
hash_original: "009c5f3af2dc"
---

## In 60 seconds

- **What happened.** The PHP project released four versions that fix two critical vulnerabilities through which an attacker without credentials can run code on a server.
- **Why it matters.** Anyone maintaining sites on PHP 8.1 or earlier no longer receives updates from the project and has to obtain the fix on their own.
- **What we don't know yet.** Whether attacks exploiting these flaws will appear now that they are public, and how many sites remain on unsupported versions.

On August 11, the firm Calif, which was auditing PHP as part of the Patch the Planet program, reported a remote code execution flaw, according to [the PHP Foundation](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). OpenAI reported the same root cause that day, and Wiz added other attack vectors. The fixes came out on October 21 in versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35. According to the foundation, 15 CVEs (public vulnerability identifiers) have been published since July 1. It also received more than 100 reports that turned out to be invalid or duplicates, and it is seeking funding from companies, governments and web hosting firms.

The schedule broke down early. The flaws' identifiers circulated on forums on October 20, and the project moved the release up by a day. Chainguard published its patch more than six hours before the coordinated time, according to the foundation. When the flaws were disclosed, the security team had not identified any programs capable of exploiting them in practice.

The [php.net advisory](https://www.php.net/archive/2026.php#2026-10-20-1) says that all installations serving web requests are at risk and that PHP 8.1 and earlier no longer receive updates from the project. Those versions have three ways out. One is the distribution that installed PHP, and another is a company that sells extended support. The third is a set of reduced patches for PHP 7.4 through 8.1, which the project's security maintainers prepared for users to compile themselves. Each path carries a cost, whether a contract or someone able to compile. That suggests the burden of this fix could fall mostly on those who did not update in time.

## Also today

- **[Microsoft attributes a campaign using AI agents to a Chinese state-aligned actor](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)**: according to the company, Storm-0940 used the open ARTEX framework and, after compromising ConnectWise, tried to break into more than 2,250 organizations on Microsoft 365.
- **[ChatGPT ads reach 26 new countries](https://openai.com/index/chatgpt-ads-expands-26-new-countries)**: they include Argentina, Chile, Colombia and Peru, on the Free and Go plans, according to [Infobae](https://www.infobae.com/tecno/2026/10/21/chatgpt-ahora-tiene-publicidad-argentina-chile-colombia-y-peru-tendran-anuncios-con-dos-versiones-de-la-ia/). OpenAI says more than 100,000 advertisers have used its platform.
- **[AI-generated women appear at Flávio Bolsonaro events to sell adult content](https://www.agencialupa.org/noticias/2026/10/20/perfis-eroticos-de-ia-usam-videos-em-atos-de-flavio-bolsonaro-para-atrair-seguidores-e-vender-conteudo-adulto/)**: Agência Lupa found two Instagram accounts with more than 1.7 million followers. It found no link to the campaign.

## In the region

In Peru, the Secretariat of Government and Digital Transformation approved the directive that sets the profile and responsibilities of the Artificial Intelligence Officer in public entities. It did so through [Resolution No. 004-2026-PCM/SGTD](https://cdn.www.gob.pe/uploads/document/file/10829158/8743150-resolucion-de-secretaria-de-gobierno-y-transformacion-digital-n-004-2026-pcm-sgtd%282%29.pdf), signed on October 19. The profile will be mandatory 12 months after the directive takes effect, and each entity pays for it from its own budget.

In Paraguay, Crusoe and Araico signed a partnership for AI compute powered by energy from Itaipú, according to [the U.S. Department of State](https://www.state.gov/releases/office-of-the-spokesman/2026/10/u-s-paraguay-cooperation-to-advance-prosperity-and-security). Its first phase would be operational by mid-2027. Neither the amount nor the allocated energy was disclosed.

## Launches

- **[Flint](https://recursive.com/updates/introducing-recursive-flint)**: a model from Recursive for agentic coding on local machines, without sending code to the cloud. According to TechCrunch, it can be downloaded for free on Hugging Face under the Apache 2.0 license.

## Threads we're following

The lawsuit against Meta over automated account blocks, which [on October 18](https://dobleclick.jaguridi.cl/en/2026/10/18/brasil-meta-revise-personas-antes-suspender-cuentas.html) was a proposal from Brazil's Ministry of Justice, is now before a court. The [federal prosecutor's office in Rio Grande do Sul](https://www.mpf.mp.br/o-mpf/unidades/pr-rs/noticias/mpf-aciona-a-justica-para-barrar-bloqueios-e-restricoes-arbitrarias-praticados-pela-meta-em-redes-sociais) filed it on October 21 with the 26th Federal Court (26ª Vara Federal) of Porto Alegre. It asks to prohibit blocks decided solely by algorithms, with a fine of 500,000 reais per account per day. We began following this thread on May 25.
