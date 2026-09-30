---
layout: lectura
numero: 8
tags: [trabajo, mercados, latam]
title: "With AI in the mix, the code you hand in is no longer enough to prove you can program"
description: "Simulated programming interviews with AI allowed show that evaluators do not change what they understand as expertise, but they do change the evidence they ask for. The code handed in no longer suffices: what now gives away a good programmer is which tool they choose, how they talk to it, and when they distrust what the model spits out."
date: 2026-06-19
paper_titulo: "Evolving Enactions of Expertise: Software Engineers' Evaluation and Demonstration of Coding Expertise with AI Coding Assistants"
paper_autores: "Jang, Sakashita, Niinuma and Gupta"
paper_publicado: "CHI 2026"
paper_doi: "https://doi.org/10.1145/3772318.3791260"
paper_archivo: "jang-2026-coding-expertise-ai-assistants.pdf"
paper_keywords: "AI Coding assistant, Coding Expertise, Software Engineering"
audio: true
hash_original: "60d4dbc68a16"
---

## At a glance

- **What it is:** *Evolving Enactions of Expertise: Software Engineers' Evaluation and Demonstration of Coding Expertise with AI Coding Assistants*
- **Who:** [Yeonju Jang](https://scholar.google.com/scholar?q=Yeonju+Jang+coding+expertise) (Cornell University; the work was done during an internship at Fujitsu), [Mose Sakashita](https://scholar.google.com/scholar?q=Mose+Sakashita), [Koichiro Niinuma](https://scholar.google.com/scholar?q=Koichiro+Niinuma), and [Aakar Gupta](https://scholar.google.com/scholar?q=Aakar+Gupta) (Fujitsu Research of America).
- **Where:** *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (CHI 2026), Barcelona. [doi.org/10.1145/3772318.3791260](https://doi.org/10.1145/3772318.3791260)
- **Type:** qualitative study. Twelve simulated programming interviews, with sixteen software engineers paired up two at a time in each session, one as evaluator and the other as candidate, with AI allowed.

## First reading: what it does and what it finds

It helps to start with what kind of study this is, because it frames everything else. It is qualitative work that uses a technique called *user enactment*: instead of asking in the abstract, the researchers set up a plausible scene from the near future and let people act within it. The scene chosen is the live programming interview, where someone solves a problem while sharing their screen as another person evaluates. They recruited sixteen engineers through social networks and technical communities, paired them by specialty and language, and put together twelve sessions. In each one, the evaluator designed their own task and criteria; the candidate had thirty minutes and could use any AI tool or search engine. The study does not measure whether AI improves productivity or evaluate any model. It describes how expertise is demonstrated and judged when the model is on the table.

The first finding is the one that gives the paper its title. Evaluators barely changed their criteria. Understanding the problem, explaining the code, handling errors, writing clean code: the usual. What changed was the evidence they accept to consider those criteria met. Finished code, which for decades was the ultimate proof that someone knows what they are doing, is no longer enough on its own, because now the model can write it. One evaluator noticed that the candidate's tidy comments were there, but the AI had generated them, so they did not count as the candidate's own expertise. Another watched someone solve the task and still concluded they could not have done it without AI. The practical consequence is that evaluators rely much more on follow-up questions: asking candidates to modify the solution, explain it line by line, say what would happen if such-and-such were changed. The test shifts from the product to the process.

The second finding is that expertise began to show itself in new ways and to hide in others. Three new signals appear: which tool the candidate chooses and why, how they talk to the model, and what they do with what the model gives back. Choosing Perplexity when reliable sources were needed was read as a smart move; an overly broad prompt, as a lack of understanding of the problem. At the same time, other traditional signals fade: when the model breaks down the task, writes the entire code, or detects the bug and fixes it in one go, the candidate loses the chance to show how they understand, how they build their approach, and how they debug. One evaluator anticipated this and split the task into three steps that she handed over one at a time, so that it would be the candidate, and not the AI, who developed the reasoning.

The third finding is that none of this weighs the same for everyone. Evaluators split between those who value planning and those who value implementation. For the former, AI is almost a relief: if the key thing is thinking the problem through well, it matters little that the model writes the code. One evaluator took for granted that the code would work because it came from a generative model, and looked at whether the candidate was thinking the right way. For those focused on implementation, by contrast, the new signals matter much more, because they doubt the model produces extensible code and they watch how the candidate chooses, asks, and discards.

The fourth finding is a tension. With AI available, an expectation of higher productivity emerged that no one defined as a criterion but that still operated beneath the surface, and without agreement on which part of expertise produces it, there were misunderstandings in both directions. One candidate avoided AI at first to show off her understanding and then feared that it would make her look inexperienced at using tools. Another used it right away to finish quickly and left the evaluator unconvinced, because he explained nothing of what the model had given him. The tool that promises speed also makes it slipperier to know what is being measured.

## Second reading: from Latin America

The study is not about Latin America. Participants were recruited through international networks and communities and the paper does not report where they are from, so almost everything that follows is my reading, not the study's. With that caveat up front, there is one point that lands hard in the region.

A good share of the programming work the region sells to the world goes through exactly this filter: the remote technical interview. For many talented people in Santiago, Bogotá, São Paulo, or Buenos Aires, that half hour of screen sharing is the gateway to a well-paid job without emigrating. And that gate is changing its lock right now, with no new rules written down. If handing in correct code is no longer enough, and what gets judged is how you steer the model, someone who practiced a thousand LeetCode-style problems but never learned to interrogate an AI tool can come off badly even if they know how to program. And the reverse: someone who masters the back-and-forth with the model could pass without the foundation the company thinks it is buying.

There is one detail from the paper worth bringing in here: several participants described a hesitation to use AI in the interview, a stigma the authors call *AI shaming*. One felt discouraged from using it even though the instructions allowed it. In a regional market where many people's jobs hinge on these tests, if the unwritten rule penalizes both using AI and not using it, the interview ends up measuring who best read the evaluator's signals and not who best solves the problem. What the study suggests, and I extend to the region, is that the way out is not simply to ban or allow, but to make explicit what is being evaluated. The companies and bootcamps that make a living placing talent have a concrete task there: to say out loud what counts as expertise when AI is allowed, before each evaluator improvises their own yardstick.

The question it leaves applies to any hiring process. If two equally capable people can be judged differently just because of how they position themselves in front of AI, is expertise being measured, or the ability to read expectations? The study does not resolve it, but it makes clear that as long as the rule is not written down, the answer is left to the judgment of whoever is evaluating.

## The fine print

- It is a qualitative, lab-based study: its value lies in showing how and why these dynamics change, not in measuring how widespread they are. That there are sixteen people and twelve sessions is not a flaw; it is what makes it possible to look closely at something that is only just emerging.
- These are simulated interviews, not real hiring. The authors themselves warn that a live interview does not capture the collaborative, long-term nature of real work, where expertise shows over time and in teams. It is a portrait of a moment, not of the whole craft.
- Each evaluator designed their own task, so the variety of tasks and difficulty levels is part of the picture and not a controlled constant. That is consistent with a study that seeks to explain phenomena, but it is worth keeping in mind before generalizing from a single scene.
