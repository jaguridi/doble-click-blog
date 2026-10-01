---
layout: lectura
numero: 7
tags: [trabajo, mercados, latam]
title: "AI writes the code, but the result depends on how much you know about the problem"
description: "Anthropic analyzed some 400,000 Claude Code sessions and found a consistent pattern: the person who directs the AI well is not necessarily someone who knows how to program, but someone who knows the problem's domain. Experience in the field weighs more than profession, and the gap between novices and everyone else is still there."
date: 2026-06-16
paper_titulo: "Agentic coding and persistent returns to expertise"
paper_autores: "Hitzig, Massenkoff, Lyubich, Heller and McCrory"
paper_publicado: "Anthropic, June 2026"
paper_doi: "https://www.anthropic.com/research/claude-code-expertise"
paper_keywords: "agentic coding, returns to expertise, division of labor, task composition, occupations, AI and work"
audio: true
hash_original: "8ea0b02cb136"
---

## At a glance

- **What it is:** *Agentic coding and persistent returns to expertise*, a report by Anthropic's economic research team.
- **Who:** Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Ryan Heller, and Peter McCrory.
- **Where:** published on Anthropic's website on June 16, 2026. It is not a peer-reviewed paper and has no DOI: it is a report by the company itself. [anthropic.com/research/claude-code-expertise](https://www.anthropic.com/research/claude-code-expertise)
- **Type:** large-scale observational study. They analyze around 400,000 interactive Claude Code sessions, from some 235,000 users, between October 2025 and April 2026, with a privacy-preserving method: the researchers do not read individual transcripts; instead, automated classifiers label each session and the researchers work with the aggregates.

## First reading: what it does and what it finds

It helps to start with what the study measures and what it does not. Claude Code is Anthropic's tool for programming by conversing with the model, where the person asks and the model carries out actions on the code. The study does not observe whether that code ends up being used or whether the project succeeds in the real world. What it observes is the session: how the work is split between the person and the model, what it consists of, and an internal measure of whether the session got somewhere. All the evidence comes from classifiers that automatically label each conversation, and the authors themselves warn that those classifiers are hard to validate at that scale. It is worth keeping in mind when reading any figure.

The first finding is about the division of labor. In a typical session, the person makes about 70% of the planning decisions but only 20% of the execution decisions. The model runs around ten actions for every instruction from the person, and in extreme cases more than a hundred. The pattern they draw is clear: the person defines what to do and the model works out how to do it.

What the work consists of also changed over the period. About 56% of sessions involve writing code (25%), fixing it (26%), or testing it (5%); 17% involve operating existing software; 14% involve planning or exploring; and 13% involve analyzing data or prose documents. Between October and April, code fixing fell from 33% to 19% and software operation rose from 14% to 21%. The authors read this as a shift from putting out fires toward tasks more focused on building and operating, although, again, it is a short snapshot of fast-moving terrain.

The core of the report, and the source of its title, is expertise. Here it is important to be precise about what is measured: it is not the person's profession or résumé, but a level of expertise in the specific domain of the task, inferred by a classifier on a five-point scale, from novice to expert. By that measure, expert sessions look different: the model runs about twelve actions per instruction and produces on the order of 3,200 words of output, compared with about five actions and 600 words in novice sessions. The difference is statistically significant at every level.

The big jump is in success. The study uses two yardsticks. A strict one, verified success, where there is some concrete sign that the task was accomplished: there novices reach 15%, and from intermediate upward the range rises to 28-33%. A lenient one, at least partial success: novices reach 77%, and from intermediate upward 91-92%. When the session gets complicated, the gap widens: among sessions with detected difficulties, novices end with verified success 4% of the time and experts 15%. And novices abandon the session at a rate of 19%, compared with 5-7% in the other groups.

Here comes the finding the authors highlight as most striking: profession matters less than expertise. In sessions that produce code, software occupations have 34% verified success and the rest 29%, a difference of just five points. Each of the ten largest occupations in the dataset falls within seven points of software engineers. Management, sales, and law appear among the fastest-growing non-technical groups. Put another way: what makes it possible to direct the model well looks more like knowing the problem than knowing how to write code.

Hence the name, "persistent returns to expertise." It is a term borrowed from labor economics, where "return" is what a skill yields. The thesis is that AI that programs makes formal training in code less central, but it does not erase the value of expertise: it moves it elsewhere. What pays off now is domain knowledge. One nuance the authors themselves underline and that should not be lost: most of the gain appears in moving from novice to intermediate; from intermediate to expert, the improvement is modest. You do not need to be the best in the field to benefit, but starting from zero does come at a high cost.

The study closes with a value estimate that should be taken with a grain of salt. By comparing the tasks in the sessions with freelance job market postings, they calculate that the median value of a session rose 27% between October and April, with building in the lead (+43%). It is an indirect approximation, based on what is paid for one-off gigs, not salaried work, and the authors themselves describe it as a fuzzy match.

## Second reading: from Latin America

The study is global and does not break out Latin America, so almost everything that follows is my own extrapolation, not the report's. With that caveat up front, there is one signal that applies to the region.

The finding that profession carries little weight and that domain knowledge is what counts changes who can use these tools. In much of Latin America, trained software engineers are scarce, but domain experts are not: researchers, public officials, accountants, lawyers, people at small and medium-sized businesses who know their problem in detail even if they have never programmed. If what pays off is knowing the problem, the door opens for that profile, which is precisely the one that used to be left out for not knowing how to code. For someone like José, who moves between research and public policy without being an engineer, this is the kind of finding that makes you want to try it out.

But the same study puts on the brakes, and that is the part not to skip. The novice gap is real: 15% verified success versus 28-33%, and almost one in five abandons when things get complicated. The democratization is partial, not automatic. And the gain is concentrated in the stretch from novice to intermediate, that is, in learning just enough to stop being a novice. Read from the region, that says something concrete: access to the tool is not enough if it does not come with a minimum of practice and support to get through that first stretch. Handing out licenses without that leaves many people in the 15% and in the 19% who give up.

There is also a reason for caution that comes from looking at this from here. It is a study by the company that sells the tool, based on data we cannot audit, with inferred metrics. Before a ministry or a university in the region cites it to justify a purchase or a policy, it is worth asking for what the report itself lacks: evidence of real-world outcomes and, ideally, in contexts similar to ours. The signal is interesting and worth exploring; using it as finished proof would go further than the study can bear.

The question it leaves, and one the authors also ask, is whether these returns to expertise hold up or shrink over time. If they shrink, it would mean models are starting to supply the judgment the person provides today. If they hold up, the message for the region is rather the reverse: the tool lowers the coding barrier, but knowledge of one's own field remains what makes the difference, and that cannot be downloaded.

## The fine print

- It is a study by Anthropic about its own product. That does not invalidate the data, but it does call for caution: the company has an interest in the story coming out favorably, and the choice of what to measure and how to frame it is not neutral. It is best read for what it is, internal evidence and not an independent audit.
- Everything hinges on automated classifiers that label sessions, and the authors admit that validating them at this scale is difficult. "Expertise level" and "success" are not observed directly: they are inferred. I add something that is my own reading and not the paper's: if the same signal that makes a session look "expert" is part of what makes it look "successful," some of the relationship between expertise and success could come from how it is measured and not only from the world. The authors do not claim this; I leave it as a caution for interpretation.
- There are no real-world outcomes. The study does not see whether the code was used, whether the project worked, or whether anyone was satisfied. "Success" is a signal inside the session, not outside it.
- Coverage is partial. Non-interactive use, unsupervised automatic mode, and integrations with third-party editors are left out, as well as 7.7% of sessions discarded for lacking a clear objective. It is a portrait of how Claude Code is used conversationally, not of all AI use for programming.
