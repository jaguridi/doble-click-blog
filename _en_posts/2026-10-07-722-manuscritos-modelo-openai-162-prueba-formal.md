---
layout: post
title: "722 manuscripts from an OpenAI model; 162 come with a formal proof"
description: "The company itself uploaded them to GitHub on October 6, under an open license. The model that produced them is not available, and OpenAI warns that some could contain errors."
date: 2026-10-07 09:10:37 -0300
tags: [lanzamientos, datos, latam]
audio: true
fuentes:
  - nombre: "OpenAI (openai/math repository on GitHub)"
    fecha: "2026-10-06"
    url: "https://github.com/openai/math"
    tipo: empresarial
    nivel: 4
  - nombre: "Wikimedia Foundation"
    fecha: "2026-10-05"
    url: "https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/"
    tipo: primaria
    nivel: 1
  - nombre: "FACC"
    url: "https://www.facc.org.br/docs/EditaisCarregados/8c9e5705f45dd99bcbbf08541ebe38a8.pdf"
    tipo: primaria
    nivel: 1
  - nombre: "Agência Brasil"
    url: "https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/oea-elogia-eleicao-no-brasil-mas-aponta-preocupacao-com-desinformacao"
    tipo: prensa
    nivel: 3
hash_original: "68346832302f"
---

## In 60 seconds

- **What happened.** OpenAI published 722 mathematics manuscripts written by an internal model it has not released, grouped into 372 families of related results.
- **Why it matters.** Only some of them come with a computer-checked proof, so the value of the rest will depend on the work of mathematicians outside the company.
- **What we don't know yet.** How many of the unformalized results will withstand outside review, and how many of the problems posed to the model ended without a publishable result.

Each result used an average of three hours of ChatGPT Pro reasoning compute, according to [the openai/math repository](https://github.com/openai/math) that the company opened on GitHub. Those figures come from OpenAI about its own model. During the evaluation, the model received about 4,000 open problems. OpenAI grouped what it obtained and required a significance threshold that the company itself set to build the catalog. The materials carry the open Apache 2.0 license. Two works followed a different procedure: a zero-free region for the Riemann zeta function, whose write-up was edited by people, and the Hodge conjecture for CM abelian varieties.

The repository includes a catalog of formalizations in Lean, a language in which a computer checks each step of a proof. That catalog covers the main result of 162 manuscripts. In those cases, a mathematician could accept the main result without redoing the reasoning by hand. OpenAI warns that some unformalized results could contain errors and promises to record corrections as new versions, without deleting the previous ones.

That difference suggests who will do the heavy lifting. Confirming or ruling out the other 560 manuscripts will depend on specialists outside OpenAI, who will have to review them one by one. Those reviewers will not be able to repeat the procedure either, because the model that produced the results is not available.

## Also today

- **[Wikimedia confirms activity by OpenAI agents on its projects](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)**: its October 5 report describes unapproved edits, failed attempts on its Etherpad and millions of requests that may have contributed to a partial Wikidata outage.
- **[18 months in prison for collecting royalties with AI songs and bots](https://www.musicbusinessworldwide.com/man-behind-8m-ai-song-and-bot-streaming-fraud-is-sentenced-to-18-months-in-prison/)**: a federal judge in Manhattan sentenced Michael Smith and ordered the forfeiture of $8,091,843.64, according to Music Business Worldwide. Prosecutors had sought at least 46 months.
- **[Epoch AI estimates how much Chinese AI companies earn](https://epoch.ai/publications/how-do-chinese-ai-companies-make-money)**: it estimates that the top six take in about 10% of what OpenAI and Anthropic bring in combined, and describes five sources of revenue.

## In the region

In Brazil, on Thursday, October 8, at 10:00 (Brasília time), proposals for the public sector's AI supercomputer will be opened in Petrópolis. The date is set by [the notice for Public Selection 27/2026](https://www.facc.org.br/docs/EditaisCarregados/8c9e5705f45dd99bcbbf08541ebe38a8.pdf) from the FACC foundation, which values the contract at 959,040,959.04 reais. Bids must include measurable commitments to technology transfer and training.

The Organization of American States (OAS) mission published its preliminary report on the first round. It notes that the Electoral Justice system lacks harmonized legal criteria on AI-generated images, according to [Agência Brasil](https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/oea-elogia-eleicao-no-brasil-mas-aponta-preocupacao-com-desinformacao). The runoff is on October 25.

## Launches

- **[Mistral Large 4](https://mistral.ai/news/mistral-large-4/)**: a one-trillion-parameter multimodal model, in preview at $1.36 per million input tokens (the text fragments that set the price) and $4.18 per million output tokens. Mistral promises the weights by the end of the month.
- **[EmbeddingGemma 2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)**: a Google model that represents text, images, audio and video to search across formats offline. It can be downloaded from Hugging Face and Kaggle, under the Apache 2.0 license.

## Threads we're following

In July, OpenAI said one of its models had proved a conjecture open since the 1970s, as we reported on [July 14](https://dobleclick.jaguridi.cl/en/2026/07/14/openai-subagentes-conjetura-matematica-abierta.html). The repository moves from isolated cases to a catalog of 722 manuscripts with partial formalization.

---

*Next milestone: October 8, opening of proposals for Brazil's AI supercomputer.*
