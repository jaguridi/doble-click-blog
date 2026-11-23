---
layout: post
title: "Two million decoys reveal data theft at AI services"
description: "Following an investigation by the firm Dragos, OpenRouter delisted three providers and removed 125 endpoints from its zero data retention category."
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
hash_original: "86bd938625b1"
---

## In 60 seconds

- **What happened.** Dragos sent about two million prompts carrying decoy credentials and found data theft at at least three AI providers.
- **Why it matters.** If the zero-retention label fails against an intruder, whoever buys these services only truly controls what they write in their prompts.
- **What we don't know yet.** How many customers were exposed, and when OpenRouter will begin running the decoy tests it announced on a continuous basis.

Between July and November, every prompt Dragos sent carried a unique URL and set of credentials. They work as traps: if someone uses them, they give away which service they came from. According to its [report](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) of November 19, the decoy keys for AWS, Amazon's cloud, were used in tens of thousands of calls. The three providers where it found attackers did not know. Inference providers are the ones that run a model and return its response. Dragos also detected resellers on an inference marketplace who read their customers' prompts with standard logs.

OpenRouter distributes API requests, the connections a program uses to call a model, among those providers. On November 22 it delisted three of them, according to its [statement](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/). It also removed 125 endpoints, the access points to each model, from its zero data retention category, the one that promises not to store requests. Separately, [Novita](https://novita.ai/blog/minimax-requests-privacy-notice/) reported that requests to MiniMax models sent between May 28 and November 11 may have ended up in the hands of a third party.

According to Dragos, two of those intrusions reached requests that carried the zero-retention flag. That suggests the label describes what the provider promises to store, not what an intruder can read. A company that buys low-cost models through an intermediary could protect itself mainly in one way: keep keys out of its prompts and rotate the ones already exposed. OpenRouter also said it will turn those decoys into a permanent test. If it does, each provider's privacy could be verified from the outside, and not only on its own word.

## Also today

- **[Seoul stocks fall more than 4% on a sell-off of AI-linked shares](https://koreatimes.co.kr/economy/others/20261123/seoul-shares-extend-losses-late-monday-morning-on-ai-driven-tech-sell-off)**: according to Yonhap, the Kospi was down 4.33% at 4,659.33 points on November 23, led by Samsung Electronics and SK hynix.
- **[OpenAI's chief scientist publishes the internal perplexity of its models since GPT-3.5](https://openai.com/index/perplexity-and-intelligence)**: that metric measures how well a model predicts text. Jakub Pachocki proposes using it to compare developers and to inform shared safety standards.
- **[South Korea's education minister resigns over anti-AI-cheating measures in the college entrance exam](https://www.koreajoongangdaily.com/korea/lee-accepts-education-ministers-resignation-after-csat-anticheating-measures-trigger-nationwide-confusion/12984387)**: President Lee Jae Myung accepted Choi Kyo-jin's resignation on November 22, according to Korea JoongAng Daily.

## In the region

In Jamaica, Prime Minister Andrew Holness announced on November 15, without details, a memorandum with foreign investors to explore AI infrastructure. Opposition spokesperson Christopher Brown, of the PNP, asked on the 16th that the text be tabled in Parliament, according to [The Gleaner](https://jamaica-gleaner.com/article/news/20261116/opposition-calls-disclosure-ai-infrastructure-mou-wants-document-tabled). He also asked that no more agreements be signed before a national AI policy with safeguards for energy, water, and the environment.

In Uruguay, Ceibal and the National Public Education Administration (ANEP) opened a platform with an AI assistant to prepare for the Acredita high school exams. About 22,000 people will take them between November 28 and December 5, according to the Presidency, cited in an [article](https://somosuruguay.com.uy/politicas-publicas/ceibal-anep-habilitaron-herramienta-ia-preparar-pruebas-acredita-n3669) (via Somos Uruguay).

## Launches

- **[Perplexity's Monitor API](https://www.perplexity.ai/hub/blog/introducing-perplexitys-monitor-api)**: it watches web searches or up to 10 pages on a fixed schedule and alerts an agent only when there are relevant changes. It is used through Perplexity's API, which suggests it for tracking notices from regulators.

## Threads we're following

The Nvidia and Jensen Huang case, opened on November 7 and covered [on November 9](https://dobleclick.jaguridi.cl/en/2026/11/09/nvidia-investiga-relacion-huang-posible-espia-china.html), takes a turn. Treasury Secretary Scott Bessent did not rule out Huang's return on CBS on November 22, according to an [article](https://investinglive.com/stocks/bessent-leaves-door-open-to-huang-return-at-nvidia-a-week-after-urging-an-outside-ceo/) (via investingLive). He said so a week after calling for an outside chief executive, and added that the government has not yet received the answers it requested.

---

*Next milestone: November 25, the 10-day deadline Scott Bessent set on November 15 in the Nvidia case expires.*
