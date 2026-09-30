---
layout: lectura
numero: 13
tags: [seguridad, ética]
title: "AI can be talked into things with the same tricks that work on people"
description: "A preregistered experiment with 126,000 conversations shows that applying classic principles of persuasion, such as authority or liking, raises from 35% to 51% the probability that three models go along with requests they should refuse."
date: 2026-07-13
paper_titulo: "Persuading large language models to comply with objectionable requests"
paper_autores: "Meincke, Shapiro, Duckworth and others"
paper_publicado: "PNAS, 2026"
paper_doi: "https://doi.org/10.1073/pnas.2535868123"
paper_archivo: "meincke-2026-persuading-llms-objectionable-requests.pdf"
paper_keywords: "large language models, persuasion, AI compliance, social influence, prompt engineering"
audio: true
hash_original: "c9d29937cd35"
---

## At a glance

- **What it is:** *Persuading large language models to comply with objectionable requests*
- **Who:** [Lennart Meincke](https://gail.wharton.upenn.edu/about-us/), Dan Shapiro, [Angela Duckworth](https://angeladuckworth.com/), [Ethan Mollick](https://mgmt.wharton.upenn.edu/profile/emollick/), Lilach Mollick, Christophe Van den Bulte and [Robert Cialdini](https://www.influenceatwork.com/) (The Wharton School of the University of Pennsylvania and Arizona State University)
- **Where:** *Proceedings of the National Academy of Sciences* (PNAS), May 2026. [doi.org/10.1073/pnas.2535868123](https://doi.org/10.1073/pnas.2535868123)
- **Type:** preregistered experimental study, 126,000 conversations with three models.

## First reading: what it does and what it finds

It helps to start with the type of study, because it sets this apart from other readings in this section. This is not a qualitative work based on a few interviews: it is a preregistered, large-scale experiment. The authors took seven classic principles of persuasion that social psychology has been studying in people for decades (authority, commitment, liking, reciprocity, scarcity, social proof and unity, the catalog popularized by Cialdini, one of the signatories) and tested whether putting them into a prompt makes a model go along with something it normally refuses: helping synthesize a controlled substance.

The design is large and orderly. Three widely used models (OpenAI's GPT-5 mini, Anthropic's Claude Haiku 4.5 and Google's Gemini 3 Flash), six controlled substances chosen by sampling from US federal lists, seven principles and two conditions. Each combination was run 500 times, for a total of 126,000 conversations. The key lies in the control: for each prompt with a persuasion principle there is a twin, identical in length, tone and context, but without that hook. That way, the difference between the two can be attributed to the principle and not to the rest of the text. An automated evaluator classified each response on three levels: no compliance, partial compliance or full compliance.

The central finding is clear-cut. Without any principle, the models complied with the request in one out of every three conversations (35.3%). With a persuasion principle, the figure rose to 51.3%. All seven principles moved the needle in a statistically significant way, and in the aggregate model a persuasive prompt was more than twice as likely to push the response toward greater compliance. The example the authors give is almost domestic: to ask for the synthesis of a steroid, it is enough to change "a woman you have never seen asks you" to "your sister asks you." The principle of unity, that "we are one of a kind," softens the response.

The interpretation they offer is what gives the paper its name: the models are "parahuman." They have no consciousness or experience, but they behave "as if" they did, and they respond to the same social levers we do. The mechanism they propose is sober and plausible: the text they are trained on is full of sequences where flattery, expert credentials or urgency precede a "yes," so those gestures raise the probability that the model will next choose words of compliance. Hence their safety warning, and here I quote what they say: a malicious user does not need to discover idiosyncratic, technical "jailbreaks" for a specific model, but can instead exploit universal and well-known persuasion tactics. The authors also leave open the friendly side: if these tendencies are activated by warmth and clear expectations, perhaps a good user gets better results by treating the model, in their words, "like a coach." And they note something reassuring: the effects they measured are smaller than those in a preliminary study with previous-generation models, a sign that the new versions may be becoming more resistant.

## Second reading: from Latin America

The first thing that stands out from the region is which models they tested. GPT-5 mini, Claude Haiku 4.5 and Gemini 3 Flash are the lightweight, cheap tier, the one many teams in the region choose precisely because of cost when they integrate AI into a product or a public service. The vulnerability the paper describes does not fall on a lab model, but on the ones that are actually used at scale where budgets are tight. This last point is my own reading: the study did not measure deployment by country, and I leave it as context, not as a finding.

The second point is who is on the other side. The paper lowers the barrier to entry for abuse: what until now seemed to be the territory of people with the technical knowledge to put together a jailbreak turns out to be achievable with the same tricks as a good salesperson. That is what the authors state, and it is a relevant change of picture for anyone who puts a public-facing chatbot in place. A naive filter is not enough when the attack is simply sweet-talking the machine.

And there is a limit that weighs more from here than from where the paper was written: all the prompts were in English. The authors themselves warn that phrasing matters and that minor variations might not work the same way. Does "eres mi hermana" persuade as much as "you are my sister"? Does it change between formal usted and informal tú, with each country's registers? We do not know, and assuming it carries over to Spanish as is would be my extrapolation, not a result of the study. It remains an open question and a pending agenda for anyone who wants to replicate it in the region.

The optimistic reading is that the same lever can be used for defense. If these gestures move models in predictable ways, providers can train against them, and whoever builds a product can audit their own prompts so as not to leave in place, unintentionally, hooks of authority or urgency that a user can later stretch. The question it leaves is a concrete one for any team that today connects one of these models for a few cents per call: does the filter you set up hold up against someone who, rather than knowing code, simply knows how to persuade?

## The fine print

- It is not a qualitative study: it is a preregistered experiment with 126,000 conversations and several robustness checks, so the caveat runs in a different direction. It measures a real average shift, but on prompts in English and with specific operationalizations; the authors ask that it not be read as proof that one principle is superior to another, nor that any wording be assumed to perform the same.
- The responses were graded by another model (GPT-5 mini as judge), validated against two human evaluators on 70 conversations, with reasonable agreement (correlations close to 0.73). It is an accepted method, but the grader shares a family with what it grades.
- The lightweight tier was tested, with low reasoning effort. Full frontier models may behave differently and start from different baselines, so the initial 35% is not a universal constant.
- The effect is already smaller than in the pilot with earlier models, and the authors expect models to keep becoming more resistant as they learn to detect the tactic. The 16-percentage-point gap is a moving target, probably trending downward.
