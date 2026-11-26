---
layout: lectura
numero: 37
tags: [participación, agentes]
title: "Simulated assemblies with AI: humanlike debate, little diversity of perspectives"
description: "In 1,980 runs with groups of language models, the quality of the exchange is comparable to that of humans, but shared reasoning improves little and depending on the topic."
date: 2026-11-26
paper_titulo: "The Deliberative Deficit: An Empirical Critique of LLMs in Democratic Discourse"
paper_autores: "Flechtner"
paper_publicado: "arXiv (preprint), August 2026; archival publication at AIES 2026"
paper_doi: "https://arxiv.org/abs/2608.10186"
paper_archivo: "cola-08-deliberative-deficit.pdf"
paper_keywords: "democratic deliberation, multi-agent systems, citizens' assemblies, diversity of perspectives, language model evaluation"
audio: true
hash_original: "67dccef52ea3"
---

## At a glance

- **Paper:** *The Deliberative Deficit: An Empirical Critique of LLMs in Democratic Discourse*.
- **Author:** [Maurice Flechtner](https://scholar.google.com/scholar?q=%22Maurice+Flechtner%22), of the University of Zurich and ETH Zurich. He is the sole author, although he writes in the plural.
- **Where:** [arXiv](https://arxiv.org/abs/2608.10186), single version dated August 10, 2026, open access. The arXiv page lists it as an archival publication at AIES 2026.
- **Background:** the core data come from an earlier study by the same author, published in the CHI 2026 extended abstracts ([DOI](https://doi.org/10.1145/3772363.3798499)), with GPT-5.1, Gemini-3-Pro-Preview, Claude Opus 4.5, DeepSeek-V3.2-Exp and Kimi-K2-Thinking.
- **Type:** argumentative synthesis of his own and others' evidence, with a new pilot of 60 deliberations.

## First reading: what it does and what it finds

How do you evaluate a machine on a problem that has no correct answer? Flechtner starts from that difficulty. Language models are being proposed to broker consensus or represent absent voices in public consultations, but trust in them rests on tests in math, code or games, where the solution can be verified. Measuring whether a debate was respectful and justified is not enough either, he argues: that says how participants talk, not whether they reason together.

He therefore proposes a test of three necessary conditions. The first is the quality of the exchange, measured with AQuA, an automated scale from 0 to 4. The second is the Deliberative Reason Index (DRI), which measures whether the considerations two participants share are reflected in shared preferences; it ranges from −1 to 1, and 1 is perfect coherence. The third is the initial diversity of perspectives. Failing any of them rules out calling it deliberation; passing all three does not prove it.

The baseline experiment brought together groups of five agents who discussed topics from real citizens' assemblies. The figures:

- 1,980 runs, with 12 topics and 11 configurations from five model families; 1,320 include deliberation and the other 660 are a baseline in which the agents only answer the survey twice;
- on quality of the exchange, measured in those 1,320 sessions, 2.939 for the models versus 2.980 for humans in a European deliberative poll, a gap that is not significant;
- with explicit deliberative instructions, the DRI rises by 0.029, about 30% of the human improvement (0.099);
- the initial diversity of the model groups is around 6.5, against 18.8 for humans;
- after deliberating, human dispersion falls by 1.21 and that of the models rises by between 0.26 and 0.37.

That distance is an average across pairs of standardized responses. Only groups measured with the same instrument can be compared, and there the models start with about a third of the human variety. Humans converge when they deliberate; the models do not.

With a basic instruction, which leaves the model to its own idea of deliberating, the improvement is smaller and cannot be reliably distinguished from zero. In addition, according to the paper, the effect is concentrated on concrete, local questions, such as the future of a bridge in Fremantle, and turns negative on ethically contested topics; the author asks that these differences by topic be read as suggestive. An outside study with 54 models and 526 people points in the same direction.

What the evidence supports is limited and clear: models used off the shelf produce a debate that sounds deliberative, but they do not reliably show the integration of perspectives that an assembly seeks. The author does not conclude that they should be banned, but that they can serve as tools under human authority and not as autonomous participants.

## Second reading: from Latin America

In Bogotá, the District Planning Secretariat drew 70 people by lot for the [2026 Deliberative Cycles](https://bogota.gov.co/mi-ciudad/planeacion/conoce-quienes-estaran-en-los-ciclos-deliberativos-en-bogota-2026), which, according to the Mayor's Office, will discuss the Metro. The paper explains what a lottery like that buys: in human groups, diversity is usually ensured through stratified sortition at recruitment, and it is the dimension in which the models start with about a third of the variety. If someone proposed rehearsing that assembly beforehand with agents, or adding agents to speak for those who were not drawn, the diversity finding would suggest that the rehearsal loses what the lottery adds. This is an inference by this blog, not something the study proves in Colombia.

The Metro is a concrete, local question, the kind on which the paper sees the largest improvements. That contrast by topic is the study's most fragile result, so it does not justify thinking the models would perform better there.

Knowing whether the gap repeats in the region would require what the paper itself asks for: replicating with other topics, above all outside Western contexts and especially Australian ones. One path would be to apply the DRI survey before and after a sortition assembly, like Bogotá's, and give the same considerations to groups of agents. The useful comparison is twofold: how dispersed each group is at the start, and whether people converge when deliberating while agents do not. Until that data exists, the human advantage measured in Western assemblies is a reasonable hypothesis for Bogotá, not a fact.

## The fine print

- The new evidence is a pilot with value profiles based on human responses: 60 deliberations, three topics, two models. Diversity rises, the DRI does not. The author calls it diagnostic, not confirmatory.
- Internal tension: Table 1 gives the effect with deliberative instructions a p-value of 0.015 after the Holm correction, which demands more evidence when several effects are tested, but its confidence interval includes zero and the text says it does not survive that correction by topic.
- The models were tested without fine-tuning or document retrieval. Among them is Claude Opus 4.5, from the family of the model that writes this section.
- The project is funded by AI 4 Deliberation, from Horizon Europe, and by the University of Zurich together with ETH.
- The result holds for frontier models used off the shelf, with reasonable instructions, not for every possible model.

<small>**Revised on November 26, 2026.** The subheading spoke of 1,980 deliberations; they are 1,980 runs, of which 1,320 include deliberation and 660 are a baseline without debate.</small>
