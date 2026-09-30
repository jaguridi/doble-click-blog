---
layout: lectura
numero: 6
tags: [educación, datos, latam]
title: "The poorer the country, the more AI is used for learning"
description: "An analysis of 686,000 conversations in 227 countries finds that educational use of AI rises where income falls, the opposite of what happened with the internet. And that English is taking over as the lingua franca of AI precisely where local languages work worst in the models."
date: 2026-06-16
paper_titulo: "How Early Adopters Used Generative AI Worldwide: Variation by Country Income and Language"
paper_autores: "Daepp and Slaughter"
paper_publicado: "arXiv preprint, 2026"
paper_doi: "https://doi.org/10.48550/arXiv.2605.30685"
paper_archivo: "daepp-2026-early-adopters-generative-ai-worldwide.pdf"
paper_keywords: ""
audio: true
hash_original: "79c68c53a0a6"
---

## At a glance

- **What it is:** *How Early Adopters Used Generative AI Worldwide: Variation by Country Income and Language*
- **Who:** [Madeleine I. G. Daepp](https://www.microsoft.com/en-us/research/people/mdaepp/) (Microsoft Research) and [Isaac Slaughter](https://scholar.google.com/citations?user=lg1C8i8AAAAJ) (University of Washington).
- **Where:** preprint on arXiv (cs.CY), May 2026, in conference format. It has not yet gone through peer review. [doi.org/10.48550/arXiv.2605.30685](https://doi.org/10.48550/arXiv.2605.30685)
- **Type:** a quantitative, descriptive study of 686,722 conversations from 54,841 users in 227 countries.

## First reading: what it does and what it finds

It helps to start with the type of study, because it organizes the rest. This is a large-scale descriptive work. The authors took a database of anonymized conversations, scrubbed of personal data, from a free chatbot available almost everywhere in the world, Bing Copilot, over six months of 2024 (April to September). To be able to compare countries, they built a stratified sample: up to 250 users per country, up to 20 conversations per user, and only people with at least five conversations, to keep those who genuinely found a use for the tool and not someone who tried it once. They do not measure whether AI is useful, nor do they evaluate any model. They describe what people use it for, depending on where they live and what language they write in.

To classify the "what for," they built a classifier based on a labor economics taxonomy that divides people's time into five uses: study, paid work, household production, personal care and leisure. They validated it against two human coders and report moderate agreement, comparable to that of similar work. The detail is worth noting: the classifier is a language model, and they apply it to conversations in many languages. It is the method they have for looking at hundreds of thousands of chats, but it is worth keeping in mind when reading the figures.

The first finding is the one that gives the title, and it runs counter to what happened with the internet. Study is the most frequent use: in two-thirds of countries (66.7%) it is the main purpose for most users. And the lower the country's income, the more study weighs (a strong inverse correlation, Spearman of -0.64). Paid work also rises as income falls. Leisure, by contrast, goes the other way: it grows with the country's wealth (correlation of 0.69). Put simply, in richer countries AI is used more for entertainment; in poorer ones, more for learning and for making a living. In addition, those who use the chatbot to study tend to concentrate a large share of their conversations there, more than for any other use.

The second finding is about language. English appears overrepresented as the language of AI, but unevenly. In Europe and the Americas, the proportion of people who know English is larger than the proportion who actually write to the chatbot in English; that is, people prefer their own language when they can. In Asia, Oceania and Africa the opposite happens: English works as the lingua franca of AI far beyond how many people actually master it. Why? The study cross-references this with how well models perform in each language (the MMLU-ProX benchmark). Use of languages other than English stays flat and very low until a language reaches a certain performance threshold; only then do people start using it. African languages, which score worst on that test, are practically absent from use. People, the data suggest, end up writing in English when their language works poorly in the model.

The conclusion the authors draw from putting the two things together is what gives the paper its meaning: whether this technology ends up widening the digital divide or, conversely, allows "leapfrogging" could depend, in large part, on how well models perform in each language.

## Second reading: from Latin America

The study is global and does not single out Latin America as a bloc, so what follows is my reading of where the region falls on its maps, not a finding about the region.

The first piece of news is relatively good. The harshest part of the language gap hits African languages and several Asian ones, not Spanish or Portuguese, which are among the languages best served by the models. On the language dimension, then, the region starts from a comfortable position compared with much of the Global South. The second piece of news is more interesting for thinking about public policy. By income level, the region sits in the middle band, where, according to the study's pattern, educational and work use weighs more than leisure. If that held true here (and it is an extrapolation: the paper did not measure it for these countries), it would mean that many people are already using these tools to study and to improve their employability, not just to entertain themselves.

That is where the opportunity the authors themselves speak of lies, and it is worth citing carefully, because they leave it as a possibility and not a certainty: if AI really helps people learn, there could be a leapfrogging effect in the places that need it most. But in the same breath they warn of the flip side, and that is theirs, not mine: for that to happen, models have to be designed so that people really learn and not so that they copy. The study does not settle which of the two is happening.

There is a third warning that the paper notes and that hits hard in the region. If models perform worse on safety and alignment in some languages, a "third-level" gap could open up: no longer in who has access or who knows how to use the tool, but in who bears the harms. Spanish is well covered, but it is worth not reading that as meaning the region is outside the problem: many Indigenous languages are not in any of these tests.

The question it leaves works for any ministry of education in the region. If what people do most with AI in countries like ours is study, are we treating these tools as a discipline problem (copying) or as the learning infrastructure that, judging by how they are used, they already are?

## The fine print

- It is a descriptive study: it shows correlations, not causes. The authors are explicit that they cannot say why these patterns appear, and they offer three possible explanations for educational use (that in poor countries the first to adopt AI are students, that users with money move to other paid chatbots, or that needs really are different).
- The sample is stratified by country, designed to compare countries, not to portray the total volume of use worldwide. And it looks only at "early adopters," people who used the chatbot at least five times, not those who tried it in passing.
- It is a single product (Bing Copilot) at a specific moment, 2024. Models have improved since then, especially in languages, so the authors themselves ask that these patterns be read as a snapshot of that time and not as something fixed.
