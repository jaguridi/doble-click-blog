---
layout: lectura
numero: 21
tags: [salud, diseño, ética]
title: "A mental well-being chatbot: supplement, medicine, or yoga instructor?"
description: "Twenty-four experts in clinical practice, ethics, public policy, and health technology design, more than a hundred regulatory documents, and a conclusion that is uncomfortable for the industry: what determines whether a mental well-being AI is well designed is not how good it is at conversation, but what concrete benefit it promises and to whom. A tool meant to serve everyone answers to no one."
date: 2026-09-07
paper_titulo: "Framing Responsible Design of AI for Mental Well-Being: AI as Primary Care, Nutritional Supplement, or Yoga Instructor?"
paper_autores: "Cooper, Guridi, Hwang, Kolko, McGinty and Yang"
paper_publicado: "CHI 2026"
paper_doi: "https://doi.org/10.1145/3772318.3791556"
paper_archivo: "3772318.3791556.pdf"
paper_keywords: "Responsible Artificial Intelligence, Design, Mental Health, Large Language Models"
audio: true
hash_original: "7e1666f53ab5"
---

## At a glance

- **What it is:** *Framing Responsible Design of AI for Mental Well-Being: AI as Primary Care, Nutritional Supplement, or Yoga Instructor?*
- **Who:** [Ned Cooper](https://scholar.google.com/scholar?q=%22Ned+Cooper%22+%22human-computer+interaction%22), [Jose A. Guridi](https://jaguridi.github.io/), and [Qian Yang](https://qianyang.co/) (Cornell University), [Angel Hsing-Chi Hwang](https://scholar.google.com/scholar?q=%22Angel+Hsing-Chi+Hwang%22) (University of Southern California), [Beth Kolko](https://scholar.google.com/scholar?q=%22Beth+Kolko%22+%22human+centered+design%22) (University of Washington), and [Emma Elizabeth McGinty](https://scholar.google.com/scholar?q=%22Emma+E.+McGinty%22+%22health+policy%22) (Weill Cornell Medicine)
- **Where:** *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*, Barcelona, April 2026. [doi.org/10.1145/3772318.3791556](https://doi.org/10.1145/3772318.3791556)
- **Type:** three-stage qualitative study: 24 expert interviewees and analysis of more than 100 regulatory documents.

## First reading: what it does and what it finds

The subject of the study is **non-clinical** tools: ChatGPT, Replika, and the like, used to vent or feel better, without a prescription or supervision by a professional. US law draws a sharp line here. The clinical side is regulated by the FDA as a medical device; the non-clinical side is overseen by the FTC with a light hand, as consumer technology. Millions of people are already on the light side.

That gives rise to the question, which is about design, not measurement: what does it mean, concretely, to design one of these tools responsibly. The authors do not evaluate any chatbot or measure any effect. They ask experts in medical ethics, health policy, AI regulation, and health technology design; they analyze more than a hundred public policy documents; and they go back to the interviewees to discuss what they found. The first interviews nearly failed, and that is part of the finding: the health policy experts did not see why they were being interviewed, and the technology policy experts shared the concern without offering anything actionable. The only thing that resonated with everyone was an offhand analogy: some of these tools resemble a nutritional supplement, and others an over-the-counter medicine.

The paper turns that intuition into a two-axis map: whether the tool is a product or a service, and whether or not it guarantees a health outcome. That leaves four boxes. The supplement is a product that guarantees nothing. The over-the-counter medicine guarantees relief for a defined symptom. Primary care is a service that guarantees the outcome, and if it cannot deliver it, it is obligated to refer. The yoga instructor is a service without a guarantee: their instruction can enhance or ruin the proven benefits of yoga, and even so they promise none.

What is interesting is not the idea itself but what it organizes: each box carries different primary risks and therefore different responsibilities. In a medicine-type tool, the urgent concerns are safety, effectiveness, and equitable access, and several interviewees were explicit that something that does not work equally for all groups cannot be called safe and effective. In a supplement-type tool it is almost the opposite: its clinical effectiveness matters little, and what matters is that it not replace clinical care or self-care. As one interviewee put it, it is not a problem for someone to talk to a therapy chatbot, whether it is effective or not; it is a problem when that person should be talking to a psychiatrist.

The second finding is the one with the most bite. All the interviewees, in different words, put **active ingredients** at the center: the proven mechanism by which a tool improves well-being. Clinicians and health policy experts called it that, ethicists spoke of a theory of change, industry of the product's real essence. Most considered that declaring them, and also guaranteeing that they are delivered well, is a condition of responsible design. With that, the authors distinguish three types: those validated as a whole through controlled trials, extremely rare; those that deliver a proven ingredient such as cognitive behavioral therapy without being validated themselves; and those that articulate no ingredient at all, such as out-of-the-box ChatGPT used to de-stress. No interviewee described this last category as responsible design, and the parallel that comes up several times is social media, which also did not understand how it was entertaining people and discovered too late that the engine was polarization and rage.

The third finding the authors do not resolve; they leave it on the table: where the line between risk and benefit lies. Most of the interviewees from medicine, health policy, and health technology accepted the reasoning applied to innovative drugs, where a drug that saves many is approved even if it is lethal for a few, as long as the risk is disclosed. Those from ethics and design strongly resisted that population arithmetic, and the split largely followed disciplinary lines. Where there was no nuance was among clinicians: several insisted that asking whether someone has suicidal thoughts is not enough, and described a real risk assessment and a guaranteed referral as non-negotiable.

## Second reading: from Latin America

The caveat first: the regulatory analysis is about the United States, and the authors say so. The FDA, the FTC, and the definition of primary care used by Medicare and Medicaid are the material the four analogies are made of, and none of that can be imported as is. But it is worth separating two layers. The legal one does not travel. The design one does, and it is what the paper really proposes: a vocabulary so that whoever builds the tool declares what it promises and to whom, before there is a law requiring it. Where regulation is in its infancy, that vocabulary arrives just when it is useful.

Where the framework comes under strain is referral. What separates primary care from the yoga instructor is the obligation to refer effectively when the tool cannot resolve the problem, and that assumes there is someone to refer to. In much of Latin America the specialist is not there, or is months away on a waiting list, so the criterion of the clinicians interviewed becomes more demanding than it sounds: a tool that refers into a void has not done its job. And asking that it not substitute for clinical care assumes that such care is an available alternative. For many people here, the free, Spanish-language chatbot does not compete with the psychologist; it competes with nothing, and discouraging its use stops being mere caution. This is my own reading: the paper did not study the region, and it would be unfair to ask it for an answer to that version of the dilemma.

Something similar happens with active ingredients. Cognitive behavioral therapy and the like were validated mostly in other populations and in another language, and what delivers them here is a model trained mostly in English. Declaring the ingredient is the floor, not the ceiling. This extrapolation is also mine, although it points toward where the authors are already looking when they propose a database of active ingredients that documents how well each mechanism works in different populations.

The question it leaves applies to any team building something like this in the region. If you had to write on the front page of your tool what it improves, in whom, and through what proven mechanism, could you? If the answer is that it works for everything and everyone, the paper suggests that is not versatility. It is the absence of anyone accountable.

## The fine print

- Disclosure: the author of this blog is a coauthor of the paper. The authors also state that they themselves design and research non-clinical tools of this kind, so the framework they propose applies to them too.
- It is a qualitative study: its value lies in offering a framework and making disagreements explicit, not in measuring how many experts think what. The regulatory analysis covers only the United States, and the authors justify this as a choice of depth over breadth.
- They did not interview users or patients, and they explain why: they wanted to look at risks that are not yet observable, for which the subjective experience of use is of no help. Several industry interviewees come from startups, and the authors themselves note that experts from large hospitals and insurers were less accessible.
- The paper does not propose a validated standard, nor does it claim to. It leaves open two questions its interviewees could not settle: whether these tools should be evaluated by their population-level effect, and whether a risk proportional to the benefit is a sufficient yardstick.
