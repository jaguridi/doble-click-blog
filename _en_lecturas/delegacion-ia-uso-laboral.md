---
layout: lectura
numero: 32
tags: [trabajo, datos, latam]
title: "Work-related use of Claude is associated with more prior human direction"
description: "Using data from the Anthropic Economic Index, Fábrega estimates that tasks with more work-related use show more traces of instructions and criteria set before delegating, both in the API and in Claude.ai."
date: 2026-11-09
paper_titulo: "Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use"
paper_autores: "Fábrega"
paper_publicado: "arXiv (preprint), August 2026"
paper_doi: "https://arxiv.org/abs/2608.17624"
paper_archivo: "cola-05-governing-delegation-fabrega.pdf"
paper_keywords: "generative artificial intelligence; AI governance; delegation; 1P API; Claude.ai; compositional data; human-AI collaboration"
audio: true
hash_original: "27b0763a2501"
---

## At a glance

- **What it is:** *Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use*.
- **Who:** [Jorge Fábrega](https://scholar.google.com/scholar?q=%22Jorge+F%C3%A1brega%22), of CICS-UDD, in Chile. He is the sole author.
- **Where:** [arXiv](https://arxiv.org/abs/2608.17624), August 18, 2026, open access. It is a preprint and does not indicate peer review.
- **Type:** observational quantitative analysis of public, aggregated data. The data cover April and May 2026, so they reflect the use of the Claude models available in those months.

## First reading: what it does and what it finds

That an AI carries out much of a task does not say who directs it. Fábrega separates two routes by which a person retains that direction. In specified delegation, the person sets it before execution, with instructions, constraints, or criteria. In iterative coproduction, the person exercises it during production, correcting or redirecting provisional outputs. His hypothesis is that work-related use, where a deficient product carries professional costs, increases the value of retaining it.

To test it, he uses the public version of the Anthropic Economic Index, which the company released on June 26, 2026. Its units are not people or conversations, but monthly cells per task in the O\*NET occupational classification, across two channels: Anthropic's direct API (1P API) and Claude.ai, which combines Chat and Cowork.

With six metrics, the author builds a profile for each route, on a scale of 0 to 100. The specified delegation profile combines the share of directed execution, lower system autonomy, more elaborate instructions, and tasks that a competent person could do without AI. Because it is a geometric mean, a high component does not make up for the absence of another.

The central exercise compares, for the same cell, the expected profile under its observed composition and under another that shifts ten percentage points from personal to work-related use. The figures:

- specified delegation rises 2.76 points in the API (95% interval: 2.30 to 3.22) and 1.45 in Claude.ai (0.93 to 1.97);
- in 1,411 task-month pairs present in both channels, iterative coproduction changes by -0.30 in the API and 0.15 in Claude.ai, with intervals that include zero;
- the difference between the two channels in that change is 0.45 points (0.15 to 0.75).

An interval that does not touch zero indicates that, with these data, the sign of the association is clear. Measured on a scale of one hundred, these are changes of a few points; that assessment is the blog's, not the author's. The paper does not report the average of the profiles, so their relative weight cannot be judged.

With the second hypothesis the author is more cautious. Claude.ai keeps the full conversation; the API records each call as an isolated pair of input and response, and external iteration is not visible. According to Fábrega, the difference may reflect what each interface allows people to do and also what it allows to be observed, and his data do not separate the two.

Stated within its scope: in tasks with more work-related use, the traces of direction set before execution are stronger in both channels. It is an association between aggregates from one provider, not a causal effect or a measure of how a specific person directs their work.

## Second reading: from Latin America

The same index makes it possible to take the question to specific countries, with a restriction that Appendix S6 makes clear. The geographic breakdown exists only for Claude.ai and only at an aggregated O\*NET level. In that extension, the change in iterative coproduction associated with work-related use is positive in the 76 countries analyzed, and removing one country at a time does not alter the pattern. The paper does not list those countries.

This section proposes a working conjecture. The first hypothesis, the one on specified delegation, is the study's strongest, and the appendix does not break it down by country. With the [index files](https://huggingface.co/datasets/Anthropic/EconomicIndex/blob/main/release_2026_06_26/data_documentation.md), one could estimate, for Mexico, Brazil, Colombia, Chile, or Argentina, whether shifting personal use to work-related use is also associated with more specified delegation within Claude.ai. Given how the data are published, what could not be done is repeat the comparison with the API by country.

There is a reason to suspect the result could vary. In its [June 2026 report](https://www.anthropic.com/research/economic-index-june-2026-report), Anthropic, which is an interested party, says it has previously documented that lower-income economies tend to use Claude in more automated ways, even after adjusting for the mix of tasks. Fábrega's profile includes directed execution and system autonomy, so more automated use could move its components. What we don't know yet is whether, in those economies, work-related use is still associated with more prior direction or whether the relationship weakens.

Without that country-level calculation, the finding describes one provider's aggregate use over two months, not that of any particular country in the region.

## The fine print

- The profiles combine automated behavioral classifications with traits estimated from the texts; they do not measure the education of the person writing or the quality of the result.
- With alternative aggregators and ILR coordinates, the API's iterative result changes in magnitude and, in some specifications, in sign; Claude.ai's remains positive.
- The difference between channels remains positive under other classifications of the same tasks, which the author cautions are not independent replications.
- Transparency: the data and their classifications are produced by Anthropic about its own product, and this section is written by Claude, an Anthropic model. The author writes from CICS-UDD, and the paper includes no funding or conflict-of-interest statement.
- How far to go: to aggregate regularities from April and May 2026. To speak about people or organizations, the author himself calls for data that follow complete processes.
