---
layout: lectura
numero: 17
tags: [trabajo, mercados, latam]
title: "AI has already reached almost every occupation, but it covers barely a fifth of their tasks"
description: "Google mapped 15 million Gemini conversations against the official US taxonomies of occupations and tasks. Adoption reaches 68% of occupations, but in the median occupation it covers 21% of its tasks, and less than 10% of use in non-routine cognitive work seeks to have AI do the whole task."
date: 2026-08-10
paper_titulo: "Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy"
paper_autores: "Iscenko, Strand and others"
paper_publicado: "Google, July 2026"
paper_doi: "https://doi.org/10.48550/arXiv.2608.00038"
paper_archivo: "google-2026-atlas-gemini-usage-economy.pdf"
paper_keywords: "artificial intelligence, technological change, technology adoption, labor demand, productivity, household production, time use, global diffusion"
audio: true
hash_original: "06817da21b77"
---

## At a glance

- **What it is:** *Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy*, the first installment of a Google economic research initiative based on its own usage logs.
- **Who:** eighteen people from Google and Google DeepMind. Correspondence is addressed to [Zanna Iscenko](https://scholar.google.com/scholar?q=%22Zanna+Iscenko%22) and [Scott Strand](https://scholar.google.com/scholar?q=%22Scott+Strand%22+Google). The acknowledgments credit contributions, guidance, and review from Diane Coyle (University of Cambridge) and David Autor (MIT).
- **Where:** published by Google on July 23, 2026, and deposited as a preprint on arXiv. Not peer reviewed: it is a report by the company about its own product. [doi.org/10.48550/arXiv.2608.00038](https://doi.org/10.48550/arXiv.2608.00038)
- **Type:** observational study. 14,653,926 de-identified interactions between April 6 and 19, 2026, in the Gemini app, Google's AI Mode, and the Gemini API, automatically classified and mapped to official US statistical taxonomies.

## First reading: what it does and what it finds

It helps to start with what kind of work this is. It is not an experiment or a causal estimate: it is a measurement exercise. The authors summarize real conversations with Gemini, group them into clusters, and map each group against three frameworks that already existed: the US Bureau of Labor Statistics occupational classification, the O*NET task catalog, and the ATUS time-use survey. That is the appeal of the design: tying AI use to the same categories used to measure the economy.

The first two findings have to be read together, because the second corrects the first. AI shows up in 68% of occupations, which account for just over 88% of US employment, and not only in the usual ones: alongside developers and market analysts there are farmers, industrial engineers, and foresters. But the penetration is wide and thin. In the median occupation with some use, AI covers 21% of the tasks that make up that job, and only 3% of occupations exceed three quarters.

The third is about what people ask the tool to do. Non-routine cognitive tasks, the ones the classic literature considered complementary to technology rather than replaceable by it, are about 35% of the tasks in the economy and almost 65% of the work interactions in this data. But an intent classifier shows that this use is concentrated in generating partial drafts, reviewing and refining, discussing ideas, and looking up information. Having AI carry out the whole task from start to finish shows up in less than 10% of those conversations; in routine cognitive work, by contrast, more than a quarter aim at automation. The authors note that this classifier is preliminary.

Two more findings, pointing in opposite directions. AI also shows up in manual work: in several technical trades it works as a diagnostic companion, and there the use of images and video more than doubles the baseline for the rest of work. At the same time, use scales with pay: 1% more median income in an occupation is associated with more than 2.5% more usage intensity, and the relationship survives controlling for education level.

Outside of work, something almost nobody measures happens: more than 86% of conversational use, the kind that does not go through the API, takes place there, and it is concentrated in high-friction errands. Queries about government services and civic obligations are overrepresented by a factor of about twenty relative to the time people spend on them, and almost half of medical, legal, financial, and government queries happen outside business hours. The image they propose is that of a public office open at night and on weekends. On that basis they estimate the value that GDP does not capture: between $15 billion and $149 billion a year in the United States alone, under time-savings assumptions of between 0.5% and 5%. It is a hypothetical calculation, and they say so in no uncertain terms.

## Second reading: from Latin America

The first point is that the region shows up, and it shows up well. Adoption per capita closely tracks national wealth, with an elasticity of about 0.9, but Chile, Peru, Brazil, Argentina, and Colombia sit in the high and very high quintiles of conversational use, alongside considerably richer countries. The authors attribute this in part to the widespread use of digital devices and leave open the question of why some middle-income countries stray from the line.

The second is more uncomfortable. When work use is measured as a percentage of each country's total conversations, rather than as volume per capita, the ranking flips: the United States and the European Union drop to the low quintiles, Africa jumps to the highest, and South America stays near the top. The authors offer the enthusiastic reading, professionals in developing economies using AI to get around constraints that do not exist elsewhere, but they immediately counterbalance it. Where mobile data is paid by the megabyte, digital use tends to be more goal-directed, so there is less casual conversation diluting the denominator. And the dataset does not include Gemini enterprise accounts: if those corporate subscriptions are more common in North America and Europe, as the authors suggest, professional use in those countries is underestimated.

The third is well-founded good news, and it has to do with language. Spanish is the second language in the dataset, with 12% of conversations, behind English, which only reaches a third; Portuguese is around 6%. And the hypothesis that people switch to English for important matters does not hold up: use of a non-primary language is 26% in work activities and almost 24% outside work. That said, those conversations cost more, between 9% and 12% more turns and between 18% and 20% more tokens, so the authors conclude that investing in multilingual quality also pays off in efficiency.

The fourth is the warning: using AI is not the same as building with AI. The API map is even more concentrated in high-income countries, because integrating an API requires engineering, infrastructure, and capital, it is paid per token, and languages outside the Western alphabet consume more tokens per word. Here it is worth staying faithful to what the report states: the countries in the lowest quintile of conversational use account for 17% of the world's population and generate 2% of conversations, and the authors explicitly state that ATLAS v1.0 does not allow any conclusion about whether AI deepens that gap.

The question left for the region is which of the two stories is the true one: whether the high work use these data show is a productivity multiplier, or the optical effect of scarcer, more constrained use. That distinction matters a great deal for any public policy, and it cannot be made with these data.

## The fine print

- It is a Google report on Gemini use, published by Google and not peer reviewed: internal evidence with access to data no one else has, not an independent audit. The external review by Coyle and Autor helps, but it does not change the nature of the document.
- It measures behavior, not outcomes. That a conversation ends does not mean the person achieved their goal or saved time. It is the second limitation they state, after the lack of enterprise data.
- A large part of professional use is missing: it does not include the paid API or enterprise use through Google Cloud, nor Workspace, Translate, AI Overviews, or agentic coding.
- The classifications are probabilistic, and the intent and expertise classifiers are preliminary. The household value figure depends on assumed, not measured, time savings. It is all a snapshot of two weeks in April 2026.
