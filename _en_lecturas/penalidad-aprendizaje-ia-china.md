---
layout: lectura
numero: 20
tags: [educación, datos]
title: "With AI, homework grades go up and test scores go down"
description: "Thirty months of records from 26,811 secondary school students in a Chinese county. After adopting generative AI, homework grades rise 18% and the time spent on it falls by a third, but closed-book test scores fall 20% within six months, and the effect on admission exams takes two years to appear in full."
date: 2026-08-31
paper_titulo: "The Generative AI Learning Penalty: Evidence from Chinese Secondary Education"
paper_autores: "Strömberg, Lei and Wu"
paper_publicado: "SSRN, June 2026"
paper_doi: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6977138"
paper_archivo: "ssrn-6977138.pdf"
paper_keywords: "generative AI, learning, homework outsourcing, secondary education, difference-in-differences"
audio: true
hash_original: "e66d77cc9570"
---

## At a glance

- **What it is:** *The Generative AI Learning Penalty: Evidence from Chinese Secondary Education*
- **Who:** [David Strömberg](https://scholar.google.com/scholar?q=%22David+Str%C3%B6mberg%22+economics) (Stockholm University), [Victor Lei](https://scholar.google.com/scholar?q=%22Victor+Lei%22+%22University+of+Hong+Kong%22) and [Yanhui Wu](https://scholar.google.com/scholar?q=%22Yanhui+Wu%22+%22University+of+Hong+Kong%22) (University of Hong Kong)
- **Where:** SSRN, June 2026. Working paper, not yet peer-reviewed. [papers.ssrn.com/abstract=6977138](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6977138)
- **Type:** quantitative study. A 30-month administrative panel, 26,811 students, difference-in-differences with staggered adoption.

## First reading: what it does and what it finds

It helps to start with the design, because almost all of the paper's strength comes from it. The authors obtained from the education office of a county in central China, which they describe as representative of counties outside the developed coast, the records of 26,811 students from seventh through twelfth grade, 90 percent of those enrolled in secondary school there. The data run from September 2022 to June 2025 and combine three things that rarely appear in the same dataset: scores on monthly closed-book tests, the grade and submission time for weekly homework in nine subjects, and the two high-stakes national exams, the Zhongkao, which sorts students into different upper secondary schools, and the Gaokao, which in practice decides university admission.

A June 2025 survey asked in what month each student began using generative AI. Adoption went from nearly zero in 2022 to about 80 percent in 2025, and it advanced in a staggered way, which makes the design possible: comparing how outcomes change for those who adopted in a given month against those who never adopted. The most used tools were Doubao, DeepSeek, ChatGLM, Ernie Bot and Qwen, not specialized educational apps.

The central finding is a clean divergence between productivity and learning. Six months after adopting AI, homework grades rise 18 percent relative to the baseline mean and submission time falls from 64 to 45 minutes. At the same time, scores on monthly closed-book tests fall 20 percent. The two curves separate exactly in the month of adoption and had been moving together before, which is what the design needs.

The second finding is about time. The effect on monthly tests is complete in about six months; the effect on admission exams takes about two years to reach its full magnitude, 18 percent on the Gaokao and 24 percent on the Zhongkao, because those exams cover material from several years. The authors themselves draw the methodological consequence, and it is uncomfortable for the rest of the literature: short studies, which are almost all of them, underestimate the long-term cost.

The third finding explains the mechanism and avoids the crude conclusion that AI does harm on its own. The loss is concentrated among users whose pattern is consistent with outsourcing the homework, who make up 58 percent of AI users and rise to 81 percent among those who have been using it for more than five months: they submit in less time than even the fastest students without AI, get homework grades that match what these tools get right on that type of exercise, and perform very poorly on tests. By contrast, AI users who spend the same time on homework as non-users get test scores similar to theirs, with better homework grades, and they are not better students to begin with. The authors' conclusion is precise: AI reduces the time devoted to learning for most students, but it does not reduce the efficiency with which those who maintain their time learn.

Broken down by subject, the largest drops are in social sciences (27 percent on average), then STEM (22 percent) and finally languages (English 17 percent, Chinese 9 percent). It is worth noting, because previous experiments are almost all concentrated in math, programming and languages, and none of those is the hardest-hit subject here: math falls 22 percent and languages less than that. By profile, the drop is larger among younger students, among boys and among those with better initial performance, which compresses the distribution of skills through a different path from the familiar one: not because AI lifts those at the bottom, but because it penalizes those at the top more.

## Second reading: from Latin America

What makes this paper translatable is that it does not study a tool, it studies an incentive. The authors say so at the end: the literature is focused on how to design AI tutors that work well, and in China those tutors already exist and are cheap or free. Students still choose the general-purpose chatbot that delivers the answer directly. What is missing is not a good tool, it is a reason to prefer it.

From there comes the finding that most resembles the region, and it is a measurement problem before it is a technology problem. Among AI users with above-average homework grades, better homework grades are associated with worse test scores. Homework stops providing information about learning, and the gap only becomes visible in a closed-book assessment. That matters where classroom grades weigh in school marks and those marks feed into university admission. Chile with the NEM and the grade ranking, Brazil with the ENEM, Mexico with its entrance exams: the architecture of a high-stakes external exam coexisting with classroom grades that are now easy to outsource exists across the region. This last point is my reading and not the paper's, which studied one Chinese county and nothing more.

A clarification from the authors is worth not skipping: the time saved on homework is 2.2 to 2.8 hours per week, between 5 and 6 percent of total study time, much less than the 20 percent drop in scores. They suggest that other factors must be contributing, probably that those who outsource the weekend homework also outsource everything else.

There is an optimistic note that they themselves present as suggestive rather than established. Measured at five months of use, the penalty went from around 25 percent in early 2023 to around 16 percent in June 2025, and the pattern holds when the sample is fixed to early adopters. Something is adapting, among students or teachers, although the loss is far from disappearing.

Their three policy suggestions are modest and cheap, which is what makes them relevant for ministries without a budget for big reforms. Give students credible information about the learning cost of outsourcing homework, because today they do not perceive it. Increase the weight of in-person, closed-book assessments. And have teachers and families monitor inputs, study time and effort, instead of outputs, which is what AI has made uninformative.

The question it leaves is a direct one for any ministry in the region. If the homework grade no longer tells you whether the student learned, what is being used to assess them?

## The fine print

- It is a working paper on SSRN, not yet peer-reviewed.
- The month of adoption is self-reported and retrospective. The authors discuss this: reporting that was too late would have left pre-trends, which do not appear; reporting that was too early would explain part of the six-month ramp, but not the final magnitude.
- Identification is weaker for the admission exams, which are observed once or twice and where pre-trends cannot be shown. The authors acknowledge this and support their causal reading on the fact that the ordering of effects by subject and by profile is almost identical for both types of exam.
- Homework time is the interval between opening and submitting on the platform, not actual working time. The authors say so and treat it as a reasonable approximation, but it is the variable on which the entire outsourcing mechanism rests.
- The relationship between homework time and test scores is not causal, and they say so explicitly: it serves to characterize who does worse, not to conclude that requiring more time would restore learning.
- It is one county in China. The mechanisms travel better than the magnitudes.
