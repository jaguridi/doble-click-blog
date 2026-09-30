---
layout: lectura
numero: 19
tags: [datos, gobernanza, seguridad]
title: "Almost half of real-world AI use disappears when it is measured only as work"
description: "An academic consortium pooled seven sources of real conversations with AI assistants and annotated them with a single taxonomy. When the occupational filter of the Anthropic Economic Index is applied to them, 48% of the conversations are discarded, and what gets discarded is not noise: that is where health, relationships and much of the sensitive content are concentrated."
date: 2026-08-24
paper_titulo: "The AI Observatory: A Public Measure of Real-World AI Use"
paper_autores: "Longpre, Reuel, Ki and others"
paper_publicado: "Preprint, August 2026"
paper_doi: "https://ai-observatory.org"
paper_archivo: "ai_observatory.pdf"
paper_keywords: "real-world AI use, conversation taxonomy, annotation pipeline, occupational filter, measurement sensitivity"
audio: true
hash_original: "7447ed798db6"
---

## At a glance

- **What it is:** *The AI Observatory: A Public Measure of Real-World AI Use*
- **Who:** nineteen researchers from MIT, Stanford, Northeastern, Johns Hopkins, Berkeley, Carnegie Mellon, Brown, NYU, Maryland, Waterloo, EleutherAI, Cohere, Code Metal and Adaption Labs. First authorship is shared between [Shayne Longpre](https://scholar.google.com/scholar?q=%22Shayne+Longpre%22) (MIT), [Anka Reuel](https://scholar.google.com/scholar?q=%22Anka+Reuel%22) (Stanford) and [Dayeon Ki](https://scholar.google.com/scholar?q=%22Dayeon+Ki%22+Maryland) (Maryland). Among those who guided the work are [Sandy Pentland](https://scholar.google.com/scholar?q=%22Alex+Pentland%22) (MIT), [Sara Hooker](https://scholar.google.com/scholar?q=%22Sara+Hooker%22) (Adaption Labs) and [Sanmi Koyejo](https://scholar.google.com/scholar?q=%22Sanmi+Koyejo%22) (Stanford).
- **Where:** preprint, August 2026. Not peer-reviewed at the time of this reading. Taxonomy, annotations and annotation tools at [ai-observatory.org](https://ai-observatory.org)
- **Type:** measurement study. 23,158 conversations and 85,633 annotated turns, drawn from seven real-use sources collected between April 2023 and July 2025, classified with a common taxonomy of 145 traits.

## First reading: what it does and what it finds

The first thing is to understand what kind of work this is. It does not measure whether AI is useful or estimate effects: it builds a measurement infrastructure and then uses it to test how fragile the claims circulating about "what AI is used for" are. The authors pooled seven collections of real conversations (WildChat, ShareGPT, AI Archive, a scrape of public Grok conversations, LMSYS-Chat-1M, Chatbot Arena and the National Internet Observatory) and ran them through a single taxonomy of 145 traits, which labels each conversation at four levels: the prompt, the response, the turn and the full conversation. That taxonomy covers function, topic, sensitive uses, interaction style, multi-turn dynamics and structure. The annotation is done by a model, GPT-4.1, calibrated against a human validation set.

The first finding is that the sources are not interchangeable, by a wide margin. On Grok, 67.1% of conversations include information seeking, versus 26.2% on WildChat. ShareGPT leans toward content generation (63.6%) and AI Archive toward information analysis (53.9%). Topics diverge in the same way: Grok concentrates news and current events (38.5%) and business and society (64.5%), far above the rest. And the structure does not match either: WildChat prompts average 569.5 tokens versus a range of 51.8 to 181.0 in the others, and Grok responses average 1,322.9 tokens.

That matters above all for risks. Academic integrity problems, for example assignments that were probably copied, range from 23.1% on WildChat to 40.4% on AI Archive. Misinformation is concentrated on Grok (15.3%, versus a range of 4.2% to 10.2% in the rest). The authors are careful with the interpretation: since all the sources are opt-in, they cannot attribute any difference to a specific cause, whether the platform, the model or the period. What is established is the magnitude. Which source the data come from substantially changes the picture of use.

The second finding is the one that gives the title, and it is the most uncomfortable. The Anthropic Economic Index, in its March 2025 version, first filters the conversations relevant to some occupation and only then maps the tasks. The authors reimplemented that filter from the prompts and the taxonomy Anthropic published, and ran it on six of their seven sources: the National Internet Observatory is left out because its data agreement only allows extracting aggregate annotations agreed upon in advance, so the pipeline cannot be run there. 47.9% of conversations are classified as non-occupational, with a floor of 34.2% on AI Archive and a ceiling of 61.9% on LMSYS. Then they looked at what the filter discards, holding source and annotation fixed. What gets discarded is not random residue: it is much more likely to involve health and relationships (44.2% versus 31.2%), adult or illicit topics (7.9% versus 2.1%), harassment or hate (27.5% versus 5.6%) and sexual content (15.7% versus 2.4%). The conclusion they draw is about method, not an accusation: the filter is not a neutral preprocessing step, and a framework can look complete while systematically leaving out socially important uses. They themselves clarify two things that are worth not skipping. That 47.9% is not an estimate of Claude.ai traffic, and later versions of the Index no longer apply the occupational filter and find similar distributions.

The third is that use shifts. Between April 2023 and July 2025, within WildChat, prompts grew 1,049.5% in average tokens, responses 100.6% and turns 17.1%. And variants from the same developer sustain distinct usage regimes: short, template-like exchanges with GPT-3.5, longer and iterative assistance with GPT-4o, and long, single-pass technical problem-solving with reasoning models such as o1.

The fourth looks at people rather than averages. Among users who return to WildChat, the variety of uses narrows over time: distinct function labels drop from 4 to 3 and sensitive-use labels from 2 to 1. In other words, the aggregate expansion of conversations does not come from each user writing more, but from a change in who is using the tool.

## Second reading: from Latin America

The region does not appear in this work, and the authors say so: among the limitations they state that regions where the Global South predominates remain largely out of reach, even if somewhat represented, and they propose as a remedy integrating consented donation studies, regional sampling and provider-side aggregates. The taxonomy detects 72 languages, but the paper does not report any breakdown by language in its main body.

Even so, the central result translates directly. When the region discusses what to do about AI, the figures cited almost always come from two or three reports by the companies themselves. What this paper adds is a warning about how they are read: the choice of source and the choice of filter are not technical details, they are decisions that change the result before the analysis even begins. An AI policy for work based on an occupational framework is not measuring badly, it is measuring a part, and that part leaves out precisely what would fall to health, education or data protection.

There is a difference in position worth pointing out, and it is mine, not the paper's. The United States and Europe can offset the opacity of corporate reports with their own measurements: surveys, instrumented observatories, negotiated access to data. A mid-sized country in the region almost never has any of those three things, so it depends more on someone else's report and has less to check it against. What this work shows is that such a check does not require privileged access to anyone's servers: it requires conversations donated with consent, an explicit taxonomy and money for annotation. The total annotation cost they report is $5,680. For a public agency or a university center in the region, that number is not the barrier.

That leaves a practical question. The taxonomy and the annotation tools are published and extensible, and the paper itself acknowledges that its coverage of the Global South is weak. Who in the region is going to contribute the conversations in Spanish and Portuguese that today are not in any observatory?

## The fine print

- None of the seven sources is representative of AI use. All are opt-in, and the authors themselves suspect that sensitive uses are underrepresented, because people do not publicly share that kind of conversation.
- The labels are assigned by a model. Agreement with the human consensus has a median F1 of 0.856 per parent category, and that is why all comparisons in the main body are made at that level. The authors point out that "sensitive uses" is the least stable family, and ask that those prevalences be read as approximate.
- The validation set was produced by the same authors who designed the taxonomy and chose the pipeline. They say so: that shows the pipeline's fidelity to its own scheme, not the validity of the scheme.
- The temporal analysis and the user-profile analysis rely only on WildChat, the only source with multi-year timestamps and stable identifiers.
- It is a preprint without peer review. Several authors are affiliated with AI labs, and the work compares its measurement against a proprietary report from another lab; they themselves warn that the differences may be due to a mix of product, period and source changes.
