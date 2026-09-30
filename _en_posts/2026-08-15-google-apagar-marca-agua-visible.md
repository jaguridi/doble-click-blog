---
layout: post
title: "Google lets users turn off its AI's visible watermark"
description: "The signal anyone could see disappears with a switch; the one that remains can only be read by whoever has the detector, and in the region nobody has it."
date: 2026-08-15 08:15:00 -0400
tags: [gobernanza, ética, latam]
audio: true
hash_original: "9619f5f7e2b9"
---

Google [let users turn off the visible watermark on its artificial intelligence generations](https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/). The switch lives in Settings > Media Watermark and covers images (Nano Banana), video (Omni), and music (Lyria) in the Gemini app and in the Flow editor. What always remains, whatever the user chooses, is SynthID (an invisible mark embedded in the file) and C2PA metadata, the standard that records the origin of a piece of content. Google paired the change with the release of Credentio, an open-source library that lets developers validate those credentials within their own applications.

The net result is that transparency has shifted place. The signal that was visible to anyone disappears, and the one that survives can only be read by whoever has the tool. That is the problem for Latin America: nobody has it deployed, not electoral authorities, not local platforms, not the media outlets that fact-check during a campaign. A citizen who sees a video on their phone no longer has any way of knowing, by looking at it, whether a machine generated it.

It is exactly the point Anthropic acknowledged the same day when it [published how its own text watermark works](https://www.anthropic.com/news/claude-text-watermark): the mark establishes the probability that the model was involved, not authorship; it degrades in short texts and in factual passages; and the public detection interface does not exist yet. Two labs, on the same day, putting in writing that the mandatory transparency of 2026 mainly protects those who have the means to read it.

## Also today

- **[Apple trained its own model for China and is the first foreign company approved by the Chinese regulator](https://www.macrumors.com/2026/08/14/apple-trained-own-ai-model-for-china/)** — It did so with support from Alibaba. A demanding regulator gets a tailor-made model; the region, with 650 million people and no conditions for entry, receives the global model without adaptation.
- **[Half of workplace AI use happens on free plans or plans paid out of pocket](https://epoch.ai/data-insights/employer-provided-ai-by-occupation)** — Only a third of those who use AI for work have a service provided by their employer, according to Epoch AI. In science and technology the ratio is reversed: 67% use a company tool. The sample is from the United States and serves as a floor, not as a regional estimate.
- **[Meta patented glasses that recognize faces to put together the highlight reel of your dinner party](https://www.404media.co/meta-patents-ai-glasses-to-use-facial-recognition-to-identify-people-make-highlight-reels-of-your-dinner-party/)** — The use case is given in the patent itself; the consent mechanisms for whoever appears in the frame are not.
- **[A paper on how to distribute queries among models shot up to 2,350 votes on Hugging Face](https://huggingface.co/papers/date/2026-08-14)** — Twenty-three times the day's runner-up. What the community wants to solve is no longer making the model smarter, but making the bill payable.
- **[OpenAI surpassed $40 billion in annualized revenue ahead of its IPO](https://www.pymnts.com/news/artificial-intelligence/2026/openais-revenue-run-rate-tops-40-billion-as-ipo-nears/)** — About double the rate at the end of 2025, with advertising (turned on in Mexico and Brazil three days ago) among the drivers of growth.
- **[The big six have accumulated close to $1.5 trillion in AI infrastructure purchase commitments](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone)** — Plus another $1.5 trillion in leases: future cash obligations that do not appear on the balance sheet the way debt does, and that explain why compute lands where there is energy and not where there are users.

## In the region

The region's only dated regulatory news once again comes from Brazil, and once again from its data protection authority: a preventive measure that [orders Discord to suspend live streaming in the country](https://www.gov.br/anpd/pt-br/assuntos/noticias/em-medida-preventiva-anpd-determina-que-discord-suspenda-transmissoes-ao-vivo-no-brasil) within three business days, under the ECA Digital (Law 15.211/2025). The case stems from the suicide of a 13-year-old girl from Naviraí, streamed live on July 22, with alleged incitement by criminal groups. The decision matters less because of Discord than because of the standard it sets: the agency concluded that the product's architecture prevents real-time video analysis and leaves the platform dependent on failed automated systems and on reports from users themselves. According to Tech Policy Press's reporting, the detector scored the fatal stream at 0.12 against its own threshold of 0.95, and removal took two hours. It is an argument that can be invoked against any streaming or generative AI service, and no other data authority in the region currently has in its law the power to suspend a feature within three days. With this, the agency has racked up two regulatory shutdowns in less than two weeks (the previous one was school facial recognition in Paraná) less than two months before a national election and with accusations of censorship already part of the political debate. Outside Brazil, the window was empty: no dated publications from UNESCO, the OECD, ECLAC, the IDB, CAF, or the OAS, nor from the ministries and data authorities of Chile, Colombia, Mexico, Argentina, Peru, Uruguay, or Panama.

## Launches

- **[GLM-5.3](https://www.unite.ai/z-ai-launches-glm-5-3-with-frontier-coding-and-a-cyber-capability-that-outgrew-its-training/)** — Z.ai launched the model and withheld its weights for two weeks because its offensive cybersecurity capability grew more than expected: it is the first time an open-weights lab has separated the launch of a model from the release of its weights because of risk. Same 744 billion parameter base as GLM-5.2, with the entire jump obtained in post-training (Terminal-Bench 3.0 from 4.6 to 28.3; DeepSWE v1.1 from 46.2 to 66.9). For now only through the programming interface and its coding plan; the open weights would arrive at the end of August. It matters for the region because the most realistic route to frontier capability becomes dependent on the discretionary judgment of a provider in Beijing.
- **[Visible watermark switch in Gemini and Flow](https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/)** — The control this entry is about, available for images, video, and music, with the invisible mark and the origin credentials always active.
- **[Auto mode by default in Claude Code](https://www.infoworld.com/article/4207959/anthropic-makes-claude-codes-auto-mode-default-for-paid-users.html)** — Since yesterday, new sessions on paid plans start without step-by-step approval: the agent only stops for irreversible or destructive actions or those directed outside the working environment. The enterprise and cloud versions arrive next month.

## Threads we're following

Three days ago this log reported that Anthropic had begun watermarking all the text Claude writes in order to comply with the European AI regulation, with the warning that the mark indicates processing and not authorship. Today the chapter is completed from the other end: Google, which did have a visible mark, stopped requiring it. Between the two moves, the real map of 2026's mandatory transparency takes shape (technical marks, robust and above all unreadable without tools), along with the pending work, which is who builds and deploys the detectors where they are needed.

---

*If the only watermark that survives is the one that can only be read by whoever has the detector, and in Latin America no electoral authority, platform, or media outlet has one, does mandatory transparency protect the public, or does it simply shift the burden of proof onto those with the fewest tools?*

<small>**About this entry.** It is generated automatically from public sources, without human review before publication. It may contain errors of interpretation or summary; please check each story against its original source (the links lead there) before citing it or making decisions based on it.</small>
