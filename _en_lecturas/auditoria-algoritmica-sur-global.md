---
layout: lectura
numero: 28
tags: [gobernanza, latam, ética]
title: "Eticas counts fewer than twenty published AI audits in the Global South"
description: "Galdon Clavell and Magaard argue that the evaluation gap is one of funding, not capacity, and propose that funders require independent evaluations and their publication."
date: 2026-10-26
paper_titulo: "Open Veins of Algorithmic Auditing: Why AI Assessment Lags Behind Its Deployment in the Global South"
paper_autores: "Galdon Clavell and Magaard"
paper_publicado: "arXiv (preprint, Eticas Foundation), 2026"
paper_doi: "https://arxiv.org/abs/2607.21317"
paper_archivo: "cola-01-open-veins-algorithmic-auditing.pdf"
paper_keywords: "algorithmic auditing, AI evaluation, Global South, AI governance, accountability, algorithmic impact assessment"
audio: true
hash_original: "fcded604a505"
---

## At a glance

- **What it is:** *Open Veins of Algorithmic Auditing: Why AI Assessment Lags Behind Its Deployment in the Global South*. The PDF's cover titles it *Open Veins of AI Auditing*.
- **Who:** [Gemma Galdon Clavell](https://scholar.google.com/scholar?q=%22Gemma+Galdon+Clavell%22) and [Alexandra Magaard](https://scholar.google.com/scholar?q=%22Alexandra+Magaard%22). It is a publication of Eticas Foundation, the nonprofit arm of Eticas.
- **Where:** [arXiv](https://arxiv.org/abs/2607.21317), July 23, 2026, open access. The authors present it as a draft ahead of future publications, without peer review.
- **Type:** position paper grounded in the organization's own practice: one published audit, two unpublished ones, rapid assessments during the pandemic, thirteen evaluations in sub-Saharan Africa and Asia Pacific, and a regional study for UNDP.

## First reading: what it does and what it finds

Galdon Clavell and Magaard begin by counting. They define an audit in the strict sense: an independent evaluation of a specific system, already deployed or about to be, that leaves documented findings. With that yardstick they review a decade of published work in Africa, Latin America, the Caribbean, and South and Southeast Asia. They count fewer than twenty audits and evaluations carried out by someone other than the developer. Under the strictest criterion, between ten and fifteen remain. In sub-Saharan Africa, Southeast Asia, and the Caribbean, their team found no published full audit.

The most concrete part is an audit that Eticas delivered in March 2020 and that was never published. It evaluated a national child risk alert system in a Southern Cone country, not identified for confidentiality reasons:

- the model scores 3.9 million children with 280 variables drawn from seven administrative registries;
- the event it predicts occurs in about 3 out of every 1,000 children;
- the metric that was communicated, an area under the ROC curve of 0.94, measures how well the model ranks all children by risk and gets closer to 1 the better it ranks them;
- at the threshold that triggers alerts, the model detected 73% of cases, so that about one in four children separated from their families had been classified as not at risk.

With such a rare event, the paper explains, the first metric is inflated because the model ranks well the vast majority who were never at risk, and it says nothing about the cutoff point that is used. The audit also found that the predicted variable, entry into a program involving family separation, was chosen because it was the easiest to predict. Indigenous children received higher predicted risk even though that condition had been excluded from the model.

The second case is Robot Laura, a Brazilian system that anticipates the deterioration of hospitalized patients. Its audit, commissioned by the IDB and published in 2021, found that the system deliberately overestimates mortality and more often underestimates the risk of young women.

From these cases and the thirteen evaluations, the text draws four patterns and five lessons. The thesis is that the gap is one of funding: every evaluation in its record existed because a development bank, an agency, or a UN program decided to pay for it, and none because of a legal obligation.

The paper maintains that, in every system its team examined, problems appeared that the user institution had not detected. How widespread those problems are, the paper does not measure.

## Second reading: from Latin America

All three audits in the paper are of Latin American systems, and the comparison between two of them is its central argument. According to the text, the audit that a funder decided to publish informed whoever used the system and a regional program; the one left to the contracting institution's discretion informed no one, despite being the most alarming.

In the blog's view, the first place to test that idea is the IDB. The paper credits it with commissioning the Robot Laura audit, within its fAIr LAC initiative, and with adopting a 2020 ethical assessment as a permanent internal tool. If that tool contractually required the publication of audits, the decision to publish would be taken out of the hands of the audited institution, which is precisely the point where the child case was lost. The paper states that, to the best of its authors' knowledge, none of the roughly twelve funders that concentrate the money for AI in development currently requires an independent evaluation as a condition.

Brazil offers the second test, this time a budgetary one. According to the paper, of the roughly $4.25 billion that the Brazilian Artificial Intelligence Plan commits through 2028, less than half a percent goes to oversight and governance. In the blog's view, the size of that line would determine how many audits like Robot Laura's the state itself could pay for, without waiting for an outside funder.

In Chile, the paper notes that the GobLab at Universidad Adolfo Ibáñez maintains a public repository of state algorithms and has evaluated more than a dozen models, published as case summaries and not as audits. Counting how many algorithms in the repository have some published evaluation, and of what depth, would give for one country the figure the paper estimates for the entire Global South.

The publication argument rests on two cases from the same organization. Before turning it into a rule, the region would need to know how many audits were commissioned and never saw the light of day.

## The fine print

- Conflict of interest: Eticas's commercial arm sells audits, and the paper asks funders to pay for independent evaluations. The publication itself declares that its first author chairs the International Association of Algorithmic Auditors. It is internal evidence from a market participant.
- The child audit remains unpublished and anonymized: its figures cannot be checked against the original report.
- The audit count is presented as "to our knowledge" and depends on inclusion criteria; the paper does not describe how the search was conducted.
- Transparency: the paper critically analyzes a partnership between Anthropic, which develops Claude, the model that writes this section, and the Gates Foundation.
- The audited cases are the ones someone decided to fund. They serve to show that evaluating is possible and finds flaws, not to estimate how often the region's systems fail.

<small>**Revised on October 26, 2026.** The title now specifies that the count is of published audits: the paper counts fewer than twenty published evaluations in a decade, while Eticas reports several hundred audits and evaluations of its own.</small>
