---
layout: lectura
numero: 30
tags: [participación, datos, latam]
title: "In 119 Polis consultations, the software also shaped the groups"
description: "Using the exported votes, Gelauff could not reproduce the grouping the platform reported. He concludes that the result reflects design decisions as much as the participants' choices."
date: 2026-11-02
paper_titulo: "It Takes Three to Converse: Empirical Observations on How the Developer, the Convener and the Participant Shaped 119 Polis Conversations"
paper_autores: "Gelauff"
paper_publicado: "arXiv (preprint), August 2026"
paper_doi: "https://arxiv.org/abs/2608.28368"
paper_archivo: "cola-03-it-takes-three-polis.pdf"
paper_keywords: "digital citizen consultation, Polis, opinion clustering, proposal moderation, democratic innovation"
audio: true
hash_original: "00090d087df4"
---

## At a glance

- **What it is:** *It Takes Three to Converse: Empirical Observations on How the Developer, the Convener and the Participant Shaped 119 Polis Conversations*.
- **Who:** [Lodewijk Gelauff](https://scholar.google.com/scholar?q=%22Lodewijk+Gelauff%22), a researcher at Generation Lab and an affiliate of Stanford's Deliberative Democracy Lab. He is the sole author and states that he did the work in a personal capacity, without the involvement of those organizations.
- **Where:** [arXiv](https://arxiv.org/abs/2608.28368), August 28, 2026, open access and not peer reviewed.
- **Type:** an observational study of public data exported from real consultations, complemented by a reading of the platform's source code.

## First reading: what it does and what it finds

Polis is an open-source program for asynchronous consultations: each participant sees short statements, one at a time, and marks agree, disagree, or pass; they can also propose statements of their own. Using those votes, a mathematical engine sorts participants into opinion groups, and that number of groups often leads the reports from the press and the organizers.

Gelauff tracked public mentions of these consultations and downloaded the data that each one left open. He wanted to know which part of the result is decided by each of three actors: whoever developed the platform, whoever convenes, and whoever participates. The key figures:

- he gathered 271 consultations and analyzed 119 in depth, each with at least 100 voters, totaling nearly 6.9 million votes;
- in 85 of the 114 that report how many groups the platform found, the result was two;
- when recalculating on the final votes with the same rules, but without carrying over previous cycles, the result matched what was reported in 70 of 112 cases, and among the differences, getting more groups predominated (33 times versus 9);
- with ten votes each and all else equal, a statement with only agreements gets 121 times more priority to be shown than one with only disagreements;
- the convener's seed statements achieved majority agreement in 70.1% of statements, versus 84.2% of those written by participants.

The author attributes to the design the fact that the groups cannot be reproduced. The engine recalculates in cycles and each cycle starts from the state left by the previous one, which the author calls the *warm path*. The exported file keeps only the final state, so the path that led there is lost. On top of that, the code never returns fewer than two groups or more than five, and in this corpus the only limit that actually constrained the result was the floor of two.

The advantage of statements with agreement comes from the priority formula that the author reconstructs from the code. The convener defines the seed statements, the moderation policy, and who is invited. On the participants' side, the most striking finding is descriptive: in consultations with few statements available, the typical participant answered almost all of them, and in open-ended ones, a small fraction. The author presents this as a hypothesis, without confirmed causality.

With these data, the number of groups in a Polis report stands as a snapshot of the engine at export time, conditioned by rules in the code and decisions by the organizers. The author does not claim his recalculation is more correct, only that it gives a different result, and that is why he recommends that conveners redo the analysis with the complete data at closing.

## Second reading: from Latin America

The paper records two Brazilian projects within the Polis family. One is EJ (*Empurrando Juntas*), a platform that reimplemented the method in its own code and operated between 2018 and 2022. The other is Pentano, which in 2017 rewrote only the mathematical part. The table where EJ appears warns that those platforms do not run on the engine the study analyzes.

What follows is this blog's interpretation. The floor of two groups and the carryover from one calculation to the next, which make the reported grouping irreproducible, are features of the original code. Whether a consultation run with EJ inherits them depends on its own math repository, which the paper names as ej-math. Checking it against the same points Gelauff checks in the original (the allowed range of groups, whether each calculation starts from the previous one, and how each statement is prioritized) would show how much of this diagnosis applies to those Brazilian consultations. The paper itself shows the issue is not theoretical: as of August 2026, two platforms in the family no longer used the original engine, and the author warns that several findings might no longer apply to them.

The paper's main recommendation also carries a practical cost. Redoing the analysis requires someone able to regroup the exported votes, and the paper warns of a trap: the database encodes agreement with one sign and the exported file with the opposite one.

The finding about participants remains an open question for the region. Gelauff acknowledges that the same interface can be received very differently depending on the culture. To know whether a short list of statements also leads people to answer almost all of them, one would need to compare, in Latin American consultations with open data, the share of available statements each person voted on in their first session, between fixed-list and open-ended consultations. Before that, an inventory is missing: of the countries identified in the corpus, none from Latin America is among the ten with the most consultations, and 37 of the 119 have no country assigned.

## The fine print

- A preprint without peer review; the data will be published with the final version.
- There are inconsistencies: the corpus period appears as 2015 to 2026 in one section and as 2017 to 2025 in a table, and the median number of participants per consultation appears as both 332 and 118.
- Between March 2025 and July 2026, a bug in the code made statement priority uniform. The author suggests it could serve as a natural experiment.
- It is an observational study and several conveners recur: a single operator, DEMDIS, from Slovakia, appears in 22 of the 119 consultations.
- The author states that he used Claude Code, from the same family of models that writes this section, for scripts and drafting.
- It gives reasons to treat the groups Polis reports with caution. On the behavior of participants, it leaves hypotheses rather than proven effects.
