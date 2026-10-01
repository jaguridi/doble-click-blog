---
layout: post
title: "Anthropic watermarks everything Claude writes, but it doesn't prove authorship"
description: "The watermark that universities and courts were waiting for arrives with a warning from its own maker: it indicates processing, not authorship."
date: 2026-08-12 08:14:00 -0400
tags: [gobernanza, ética, latam]
audio: true
hash_original: "70e71b6400da"
---

Starting this month, all text that comes out of Claude carries an invisible mark. According to [Anthropic's official documentation](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content), models released on or after August 2, 2026 embed in the text a machine-readable signal that the reader does not perceive, that travels with copy and paste, and that can survive some editing; images and charts also carry provenance metadata signed with C2PA, an industry standard for certifying where a file comes from. It covers every access point: the Claude interface, the programming interface, the developer tools, and the versions distributed through AWS, Google Cloud, and Microsoft Foundry.

The obligation is European (Article 50 of the AI Act, in force since August 2), but the implementation is global. Nobody in Latin America asked for it, no regulator in the region can verify it, and yet it already applies here. The most revealing part is the two warnings the company itself publishes, because they undo precisely the use the region would want to give it: detecting the mark indicates that the text **may have passed through Claude**, not that Claude is its author (the model may have translated, summarized, or corrected a human text), and the absence of a mark proves nothing, because heavy editing, format conversion, and short passages erase it.

Put another way: the tool that deans, judges, and electoral courts were waiting for to settle authorship disputes does not settle authorship disputes. And it only reaches closed models, the ones with a company behind them that can be required to do something. An open-weights agent running offline on a laptop, like the one Meta released two days ago, marks nothing and has no provider to compel.

## Also today

- **[Nvidia teams up with six Wall Street giants on a $500 billion platform for AI infrastructure](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html)** — With Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, and KKR. The hardware seller is arranging the credit to buy it, on the thesis that a cluster of graphics cards is a twenty-year asset and not equipment that depreciates in four.
- **[An unreleased Anthropic model raised the lower bound for the Riemann hypothesis from 41.6% to 67.2%](https://www.anthropic.com/research/riemann-zeta)** — Thirty-one million tokens, 650 failed ideas, and 60 subagents, directed by an employee with no mathematical training. The company clarifies that the technique will not prove the hypothesis.
- **[A company that sold "100% human, never AI" medical research turned out to be entirely AI](https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/)** — The doctors it listed on its team have generated photos and do not exist; when 404 Media called by phone, an agent answered and insisted on selling it the service.
- **[Courts in England and Wales will confiscate Meta glasses from anyone who walks in wearing them](https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/)** — The first effective regulation of wearable cameras came not from an artificial intelligence law but from the access rules of a building.
- **[The Gemini app surpasses 1 billion monthly users](https://blog.google/innovation-and-ai/products/gemini-app/one-billion-monthly-users/)** — 63% of interactions are by voice, and one in five uses the camera or screen sharing. The figures are self-reported and not externally audited.
- **[Brad Lightcap leaves OpenAI after eight years, and the head of ethics is leaving too](https://techcrunch.com/2026/08/11/brad-lightcap-openais-longtime-coo-is-leaving-to-start-something-new/)** — The fourth top-level departure in two months, after Fidji Simo, Bill Peebles, and Kevin Weil.

## In the region

Chile did something no country in the region had done: instead of waiting for the law, a state institution applied the obligation to itself. The Chamber of Deputies approved [an institutional protocol for the use of artificial intelligence](https://www.latercera.com/politica/noticia/inteligencia-artificial-parlamentaria-camara-obligara-a-diputados-y-equipos-a-transparentar-uso-de-ia/) that takes effect on September 1 and covers deputies, authorities, staff, advisers, interns, and outside collaborators who work on the Chamber's infrastructure. It covers reports, memos, presentations, analyses, translations, summaries, and communications, in any format, and requires two declarations: a color seal according to the level of use (green for no AI, yellow for partial, red for predominant or total, blue for automated with no human intervention) and the usual frequency, from occasional to intensive. It expressly prohibits using AI in administrative, disciplinary, or sanctioning resolutions without legal review, replacing legal proceedings, entering classified information into unauthorized models, generating deepfakes, and connecting unauthorized external tools.

The underlying principle is the one missing from almost every bill in the region: every institutional decision, document, or action must have an identifiable human responsible for it. The comparison is uncomfortable because it is so direct: Chile's general AI bill has been in the legislative process for more than two years, with the civil liability article still unresolved, while the same Congress settled its own case in an internal regulation that takes effect immediately. The usual question about self-declaration remains: who verifies the seal. Without auditing, a protocol like this can be a fast, copyable path (tomorrow, for any ministry, court, or municipality in the region) or a formality that allows the law to be put off for another year.

## Launches

- **[ChatGPT for Linux](https://techcrunch.com/2026/08/11/openai-launches-chatgpt-desktop-app-for-linux/)** — A desktop app in preview on Ubuntu 24.04 and 26.04 LTS, Debian 13, and Fedora 43 and 44, plus their derivatives. It arrives a month after the Claude app for Linux, and it matters because Linux is the desktop for a good part of the region's public and university sector, which migrated because of licensing costs and until now was left out of the native client of the two frontier labs.
- **[AI Persona label on Spotify](https://newsroom.spotify.com/2026-08-11/ai-persona-badges-transparency/)** — A badge for artist profiles that represent AI-generated identities, with self-declaration open since August 11 and the badge visible from mid-September. What matters is not the label but the consequence: those profiles are excluded by default from editorial, algorithmic, and personalized recommendations, and only reach those who decide to follow them.

## Threads we're following

Two days ago we reported that Meta released an agentic model capable of running offline on a laptop, with no per-token cost or international credit card involved: the most realistic route for the region not to depend on a foreign API. Today's watermark adds the other side of that coin. All the transparency machinery being built (invisible marks, signed metadata, obligations on providers) works by squeezing a handful of companies with closed models. With open weights running on each person's own machine, there is no one to squeeze. And in the background, the money keeps moving toward closed models: in addition to Nvidia's platform with Wall Street, Anthropic [leased 191 MW from Riot Platforms for twenty years and $9.1 billion](https://www.datacenterdynamics.com/en/news/riot-platforms-agrees-191mw-20-year-lease-agreement-with-anthropic-worth-91bn-report/), a converted bitcoin miner that will deliver capacity in Texas until 2048. The scarce asset is no longer the GPU: it is the permitted grid connection.

---

*If the flagship transparency tool only reaches closed models, and its own maker warns that it proves processing and not authorship, what is left for verifying the origin of a text at a university, a court, or an election campaign? Perhaps Chile found the answer in reverse: instead of detecting the machine in the product, ask the person to declare how they made it, with a seal and a name behind it.*

<small>**About this entry.** It is generated automatically from public sources, without human review before publication. It may contain errors of interpretation or summary; please check each story against its original source (the links lead there) before citing it or making decisions based on it.</small>
