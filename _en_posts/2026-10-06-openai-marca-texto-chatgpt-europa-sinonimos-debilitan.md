---
layout: post
title: "OpenAI watermarks ChatGPT's text in Europe; synonyms weaken it"
description: "With 10% of words changed, detection drops from about 92% to 66%, according to OpenAI tests cited by BleepingComputer. At first, the detector will be for researchers only."
date: 2026-10-06 09:11:08 -0300
tags: [ética, lanzamientos, latam]
audio: true
fuentes:
  - nombre: "OpenAI"
    fecha: "2026-10-05"
    url: "https://openai.com/index/eu-text-provenance"
    tipo: empresarial
    nivel: 4
  - nombre: "TechCrunch"
    fecha: "2026-10-05"
    url: "https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/"
    tipo: prensa
    nivel: 3
  - nombre: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/artificial-intelligence/openai-is-adding-invisible-watermarks-to-chatgpt-and-codex-text-in-the-eu/"
    tipo: prensa
    nivel: 3
  - nombre: "Convergência Digital"
    fecha: "2026-10-02"
    url: "https://convergenciadigital.com.br/inovacao/tribunal-de-justica-do-rio-grande-do-sul-cria-agentes-ia-proprios-para-reduzir-custo-dos-tokens/"
    tipo: prensa
    nivel: 3
hash_original: "9fc3bda0e24f"
---

## In 60 seconds

- **What happened.** OpenAI announced that, in the coming weeks, it will put an invisible watermark on the text that ChatGPT and Codex generate for users in the European Union.
- **Why it matters.** Anyone who uses the detector to judge a paper or a piece of evidence will get a probability that a minor edit to the text can change considerably.
- **What we don't know yet.** When and under what conditions universities, courts or employers will be able to use the detector, and whether there will be independent evaluations of its accuracy.

The system is called textGrain and works by adjusting the model's choice of words. That leaves a pattern a detector can recognize, even though the reader does not notice it, according to [OpenAI's post](https://openai.com/index/eu-text-provenance) of October 5. It will reach all plans in the European Union. In the application programming interface, which developers use to build their own products, the watermark is optional worldwide and comes turned off, according to [TechCrunch](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/). The outlet links it to the transparency rules of the AI Act, the European AI law, in force since August 2.

The performance figures come from the company's own tests, with no independent evaluation. In them, detection falls from about 92% to 66% if 10% of the words are swapped for synonyms, and to 17% if 25% are swapped, according to [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-is-adding-invisible-watermarks-to-chatgpt-and-codex-text-in-the-eu/).

Those figures suggest a limit for anyone who wants to use the watermark as evidence. A university reviewing an essay, or an employer evaluating a report, would get a probabilistic result, and a minor edit could lower it a lot. A negative result, then, could say little about where the text came from. Outside Europe, moreover, text will be watermarked only if the developer of each product turns on the option. Anthropic had already built a similar watermark into Claude, according to [the August 12 entry](https://dobleclick.jaguridi.cl/en/2026/08/12/anthropic-marca-texto-claude-no-prueba-autoria.html), with the caveat that it indicates processing, not authorship.

## Also today

- **[OpenAI apologizes to the Australian Parliament for its agents' access to government sites](https://citynewsqbn.com.au/2026/ai-giants-fly-in-as-safety-copyright-debates-heat-up/)**: Jason Kwon said in Sydney that the company should have responded better. In August it detected a June access to a Medicare site and gave notice in September, according to the AAP news agency.
- **[OpenAI, Anthropic, Google and Meta testify under oath before the New York City Council](https://www.amny.com/news/ai-giants-nyc-council-whistleblower-warnings/)**: they did not commit to halting launches that fail an independent audit, and xAI did not appear despite a subpoena, according to amNY.
- **[Bain estimates $5 trillion to $6.5 trillion to add about 150 GW of data centers](https://www.bain.com/insights/ai-data-center-boom-can-we-build-it-if-they-come-technology-report-2026/)**: it is the projection to 2030 in its Technology Report 2026, published on September 29.

## In the region

In Brazil, the Court of Justice of Rio Grande do Sul is certifying its own AI agents, developed with Amazon Web Services. They aim to lower what it pays for tokens, the units of text by which use of a model is billed. Its technology director, Antônio Braz da Silva Neto, spoke with [Convergência Digital](https://convergenciadigital.com.br/inovacao/tribunal-de-justica-do-rio-grande-do-sul-cria-agentes-ia-proprios-para-reduzir-custo-dos-tokens/). According to him, the Gaia tool will process about 1,500 of the 5,000 new cases filed each day and will reach 350,000 lawyers. The court also created a division that investigates misuse of AI in filings and can recommend sanctions.

## Launches

- **[Beam](https://reflection.ai/blog/introducing-beam)**: an open-weights model from Reflection, downloadable for in-house servers. The company says it matches GLM-5.2 in reasoning with 3 to 4 times less compute, and will publish the weights in October.

## Threads we're following

The Australian government confirmed an OpenAI agent's access to a Medicare portal, according to [the September 25 entry](https://dobleclick.jaguridi.cl/en/2026/09/25/empresas-ia-consejo-seguridad-onu.html). Kwon's appearance in Sydney now adds an apology before Parliament.
