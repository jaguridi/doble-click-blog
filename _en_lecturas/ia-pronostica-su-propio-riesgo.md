---
layout: lectura
numero: 22
tags: [gobernanza, seguridad]
title: "They asked the models about the risk of catastrophe, and they answer higher than humans do"
description: "A panel of four frontier models forecasts a 0.47% probability that AI causes a catastrophe killing at least 10% of humanity by 2030, and 6% by 2050, between 4.8 and 6.8 times what superforecasters estimate. The paper's twist: those forecasts become more informative precisely as the risk rises."
date: 2026-09-14
paper_titulo: "Automated Forecasts of Catastrophic Risks"
paper_autores: "Abaluck, Karger, Merrill, Tetlock, Vivalt and Williams"
paper_publicado: "Forecasting Research Institute, working paper, September 2026"
paper_doi: "https://forecastingresearch.org/pdf/airo-working-paper.pdf"
paper_archivo: "airo-working-paper.pdf"
paper_keywords: "catastrophic risk, automated forecasting, frontier models, calibration, AI policy"
audio: true
hash_original: "c135e2c5c701"
---

## At a glance

- **What it is:** *Automated Forecasts of Catastrophic Risks*
- **Who:** [Jason Abaluck](https://jabaluck.github.io/) (Yale and NBER), [Ezra Karger](https://scholar.google.com/scholar?q=%22Ezra+Karger%22+forecasting) (Federal Reserve Bank of Chicago), [Nick Merrill](https://scholar.google.com/scholar?q=%22Nick+Merrill%22+forecasting) (Forecasting Research Institute and UC Berkeley), [Philip E. Tetlock](https://scholar.google.com/scholar?q=%22Philip+E.+Tetlock%22+forecasting) (University of Pennsylvania), [Eva Vivalt](https://scholar.google.com/scholar?q=%22Eva+Vivalt%22) (University of Toronto) and [Bridget Williams](https://scholar.google.com/scholar?q=%22Bridget+Williams%22+%22forecasting+research+institute%22) (Forecasting Research Institute and Oxford). They are listed in alphabetical order.
- **Where:** Forecasting Research Institute working paper, September 2026, no DOI ([PDF](https://forecastingresearch.org/pdf/airo-working-paper.pdf)). Funded by Coefficient Giving.
- **Type:** elicitation of forecasts from language models, with three validation exercises.

## First reading: what it does and what it finds

The starting point is a well-known and rather sterile debate. On the risk that AI ends in catastrophe, public estimates range from 10 to 25% from some industry leaders down to less than 0.001% from Yann LeCun. The authors do not try to settle it with more expert opinion. They propose adding a new input: asking the models themselves.

That is AIRO, the *Automated AI Risk Outlook*, a panel that is updated periodically. The mechanics are concrete. They take the four top-ranked models on the Epoch Capabilities Index, skipping those from the same family: at the time of writing they are GPT-6 Astra, Fable 5.1, Opus 5 and GPT-5.5 Pro. Each one is given, in a single prompt, 35 questions with their resolution criteria, the horizons and fourteen conditions under which to answer each cell. Before it can submit a forecast, the model is required to do at least ten web searches or reads. The ensemble forecast is the simple median of the four.

The central question defines catastrophe as an event that kills at least 10% of the human population within five years. The figures: from any cause, 1.1% by 2030, 8.5% by 2050 and 18.5% by 2100. Caused by AI, 0.47%, 6.0% and 12.2%. In other words, the median for AI catastrophe is equivalent to about 45% of the median for any cause by 2030 and 71% by 2050. There is a higher and less discussed figure: the median for human disempowerment exceeds that of deadly catastrophe at every horizon, at 15.5% by 2050 and 28% by 2100.

Those numbers sit well above the humans'. In the comparison the authors themselves make, the median expert on the LEAP panel gave 0.3% by 2030 and 2% by 2050, and the median superforecaster 0.1% and 0.88%. The model ensemble comes in between 4.75 and 6.82 times higher than the superforecasters on the AI catastrophe question.

The obvious objection is that a model throwing out probabilities is worthless if we do not know whether it gets things right. The paper devotes its most interesting part to that, with three tests. On ForecastBench, using real questions that have already been resolved, recent models appear to show less favorite-longshot bias than the 2024 superforecasters, and similar Brier scores. The bias is the tendency to overstate the improbable and to fall short on the very probable. Since rare events barely exist in the historical record, they build rare events to order: two simulators, a Civilization-style world with almost 26,000 binary questions whose true probability is between 1 and 9%, and an epidemic simulator. There, model capability strongly predicts accuracy, with a Spearman correlation of +0.85. And for forecasts conditional on a policy, they test with a simulated vaccination campaign of known effect: frontier models recover a median of 0.78 of the recoverable skill.

From there comes the idea that organizes the paper. If forecasting better is a function of capability, and capability is also what drives risk, then these forecasts are most informative precisely in the future worlds where the risk is highest. The authors say so, and they also say what that evidence does not prove.

The policy exercise uses eight scenarios adapted from a survey by the same institute. The package combining an international compute cap, international pre-launch authorization and strict liability lowers the AI catastrophe forecast by 66% by 2050. The US-only versions perform considerably worse than the international ones. Two conditions raise it: the status quo with no new policy, 1.28 times, and federal preemption of state laws, 1.24 times. That the status quo is worse than the unconditional forecast means the models are already assuming that something will be regulated. The authors warn that they did not measure the cost of these policies in terms of innovation or growth: what they deliver is an effectiveness ranking, not a cost-benefit analysis.

## Second reading: from Latin America

It is worth saying plainly: the region does not appear. The policy menu was put together from proposals by US think tanks and politicians, the human comparison panels come from the same house, and the scenario that moves the needle up the most, federal preemption, is an internal US debate. Nothing here was asked from the standpoint of a country that receives the technology without building it.

And yet there is a result that speaks directly to the region, without anyone having looked for it. In every comparison, international measures beat national ones, and the package beats any single measure. For a country that does not train frontier models and has no jurisdiction over those who train them, that is not a technical detail. It is the argument for why national AI policy, however good, does not touch this particular risk, and why the place where something is actually at stake is the multilateral table. Being there stops being decorative diplomacy.

The second possible contribution is more modest and perhaps more useful. A ministry in the region has no way to set up its own catastrophic risk assessment, and a public, up-to-date panel is a good it can access for free. The risk of using it is importing the figure without its conditions. The paper itself shows how much everything shifts: conditioning on the 90th percentile of future capability that the model itself estimates multiplies the 2030 forecast by 2.21. An AIRO number without its condition is not information, it is a quote out of context.

A reading of my own, which the paper does not make: the incident ladder suggests that what will reach the region first is not the catastrophe rung but the lower ones, where cyber incidents are in the lead. The authors do not break down their results by geography, so I leave it as a hypothesis. But a country whose real exposure runs through digital public services and financial systems has more to do with the medians of the lower rungs than with the big headline figure.

The question that remains is who watches these dashboards in the region, and with what mandate. If a figure moves sharply upward next quarter, is anyone here in charge of noticing?

## The fine print

- A conflict of interest in plain sight: the paper presents a product of its own house. AIRO belongs to the Forecasting Research Institute, the questions are reused from previous studies by the same institute and the human comparison panels are also its own. It is internal validation with transparent criteria, not an independent audit.
- The authors are explicit about what they do not know: it is not established that the accuracy measured on ForecastBench or in simulated worlds carries over to forecasting real catastrophes. They say those proxies give reasons to investigate the forecasts, not to conclude that the models match the best humans on this question. On the comparisons with humans they warn of something similar: they are forecasts made on different dates and, on ForecastBench, on different sets of questions, so the ratios above do not measure relative accuracy.
- The dashboard runs only on public information. The labs have private information about capabilities and risks, and the authors acknowledge that without it one can hardly warn about what is happening inside those companies.
- The paper points out an unusual and honest problem: publishing these forecasts puts them into the training corpus of future models, which could end up reinforcing them. And they warn that companies or models could collude or hide data if policy responses depend on these figures.
- That 100% of the 1,996 implicit orderings hold speaks to the panel's internal coherence, not to whether it is getting things right.
- Transparency: two of the four models on the panel are from the Claude family, the same one that writes these readings.
