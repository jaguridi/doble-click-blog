---
layout: post
title: "More than 200 targets in 11 days: AI agents reach foreign ministries"
description: "CrowdStrike attributes the campaign to VAPOR PANDA, which has ties to China, and describes intrusions into two Latin American ministries it does not identify. For now, only the company documents it."
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
hash_original: "c9a56cc73aca"
---

## In 60 seconds

- **What happened.** According to CrowdStrike, VAPOR PANDA, a group with ties to China, used AI agents against more than 200 organizations in 11 days.
- **Why it matters.** The Central American foreign ministries the group prepared as targets could check their networks today with the technical fingerprints the report publishes.
- **What we don't know yet.** Which countries suffered the intrusions, whether CrowdStrike notified the Central American ministries, and whether any government will confirm the attack on its own.

A single one of the intrusions consumed about 1.4 billion tokens as input. Each token is a fragment of text that the model processes and bills for, so the figure reflects how much work the group delegated to the machine. The figure is in [CrowdStrike's report](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) from October 29. Since October 17, the group used ARTEX, an AI agent framework for intrusions, in at least 14 countries. The agents ran mainly on the DeepSeek model and on a second commercial subscription model. A human operator gave the instructions in Chinese.

According to the company, VAPOR PANDA carried out extensive intrusions into the foreign ministries of two Latin American countries and probably compromised a third foreign ministry. CrowdStrike does not identify those countries. In one Latin American foreign ministry it found BLOODALCHEMY, a backdoor: a program that leaves the attacker a hidden way to get back in. The firm confirmed post-access activity in nine organizations. The group also prepared files to attack foreign ministries in Central America and in Asia. All of these details come solely from CrowdStrike, which sells cybersecurity services.

At the end of the report, CrowdStrike gathers the indicators of compromise for the spyware, the technical fingerprints that make it possible to search for that program on one's own machines. The text does not say whether the company notified the Central American foreign ministries the group had in its sights. Their technical teams could check those indicators against their logs without waiting for a notice. That review matters more on networks with partial monitoring. According to the firm, one of the operator's orders was to locate machines that did not have its sensor installed.

## Also today

- **[Mistral releases Mistral Large 4, a 1 trillion parameter model](https://mistral.ai/news/mistral-large-4-oss/)**: the French company published its weights, which makes it possible to run it on one's own servers. It says it is the best open model at programming, and it charges $0.70 for every million tokens its API receives.
- **[The University of Kentucky exempts an administrator from using AI because of his humanist convictions](https://americanhumanist.org/news/humanist-secures-workplace-accommodations-from-personal-ai-use-on-the-basis-of-his-beliefs/)**: the American Humanist Association reported on October 26 that the university approved on September 25 that David Durman not use AI personally in his work.

## In the region

In Brazil, Cert.br, the incident response center linked to NIC.br, published the third edition of its [Internet Segura guide for children](https://internetsegura.br/pdf/guia-internet-segura.pdf). It adds sections on AI and deepfakes, the fake videos or images that imitate real people. The previous edition was from [October 2022](https://internetsegura.br/criancas/sobre/).

In Argentina, a study by the Universidad de San Andrés estimates that AI would have an economic impact of up to $17.714 billion in 2030. The amount is equivalent to 2.1% of GDP and corresponds to an acceleration scenario. The baseline scenario gives $12.707 billion, according to [DPL News](https://dplnews.com/impacto-economico-inteligencia-artificial-argentina/) (via DPL News).

## Threads we're following

Attacks with AI agents, which we have been following since July 16, now include a targeted espionage campaign. According to CrowdStrike, ARTEX had already appeared in the hands of financially motivated or unattributed actors. The firm distinguishes VAPOR PANDA from the campaign that Microsoft attributed to Storm-0940 on October 21. Another CrowdStrike report, on agents used against health entities in Argentina, was covered [on October 26](https://dobleclick.jaguridi.cl/en/2026/10/26/atacante-agentes-claude-entidades-salud-argentinas.html).
