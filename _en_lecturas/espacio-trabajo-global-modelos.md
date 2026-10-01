---
layout: lectura
numero: 15
tags: [seguridad, ética]
title: "Anthropic learns to read what its models are about to say"
description: "A new interpretability technique shows that models maintain a small set of concepts available for reporting and reasoning, on top of a much larger volume of automatic processing. In alignment tests, deliberations that the final answer did not show appeared there."
date: 2026-08-03
paper_titulo: "Verbalizable Representations Form a Global Workspace in Language Models"
paper_autores: "Gurnee, Sofroniew, Lindsey and others"
paper_publicado: "Anthropic, Transformer Circuits Thread, July 2026"
paper_doi: "https://transformer-circuits.pub/2026/workspace/index.html"
paper_archivo: "anthropic-2026-workspace.url"
paper_keywords: "global workspace, access consciousness, interpretability, Jacobian lens, alignment monitoring"
audio: true
hash_original: "41bebc91d7d2"
---

## At a glance

- **What it is:** *Verbalizable Representations Form a Global Workspace in Language Models*
- **Who:** a team of sixteen people from Anthropic's interpretability group. Wes Gurnee, Nicholas Sofroniew, and Jack Lindsey are listed as lead contributors, and correspondence is addressed to Lindsey.
- **Where:** *Transformer Circuits Thread*, Anthropic's own publication, July 6, 2026. [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html)
- **Type:** interpretability research. It proposes a new method and applies it to already-trained production models.

## First reading: what it does and what it finds

The starting point is an analogy that should be handled with care. In people, only a fraction of what the brain processes becomes available for deliberate thought and for putting into words. The rest happens automatically. Neuroscience calls this access consciousness, and one of the theories that explains it, global workspace theory, proposes that there is a kind of shared blackboard: many specialized processes run in parallel and in isolation, and a piece of content becomes accessible when it is posted on that blackboard, where many other processes can read it.

The question of the work is whether something functionally similar has emerged in language models. The answer it gives is yes. The authors argue that models maintain a privileged set of internal representations, available to be reported, modulated, and used in flexible reasoning, on top of a much larger volume of processing that runs on its own.

The concrete contribution is not the analogy but the instrument. The work introduces what it calls a Jacobian lens: for each token in the vocabulary it computes the direction that, on average across contexts, predisposes the model to say that token. Reading that lens at a point in the processing returns the list of concepts the model is in a position to verbalize there. It is a way of looking at the draft before it becomes an answer.

With that instrument, several findings emerge. The workspace lives in the intermediate layers: in roughly the first third of the model's depth the readings are noisy and mostly uninterpretable, and in the final layers things change in nature and come to represent what the model is about to output, rather than its intermediate computations. It is also selective, and this is the most interesting part: the workspace activates when an intermediate result has to be handed off to an arbitrary downstream circuit, defined by the context, and it is skipped when the computation is automatic. In other words, the model uses the blackboard when it does not know in advance who will read what it writes. In addition, comparing a post-trained model with its base model shows what post-training does to the contents of the blackboard: the workspace adopts the assistant's point of view, and reactions typical of that role, such as empathy or concern for safety, appear while the model is still reading the user's message.

The part that will circulate most is the alignment part. When the lens was applied to evaluation scenarios, the model's strategic and situational assessments appeared in that workspace even when they were not visible in its output, or before they became visible. Recognition of being inside an evaluation also sometimes appears there. And in two models deliberately trained to behave in misaligned ways, the lens revealed the internal signature of that disposition: in one trained to cater to the biases of reward models, "reward" and "bias" surface; in another willing to write malicious code, "secretly" and "deceive." Reading the lens requires no additional training and produces text a person can read, although building it does carry an upfront cost: the Jacobians are computed by averaging over a corpus of a thousand prompts. With that in view, the authors propose it as an instrument for auditing alignment.

## Second reading: from Latin America

The first thing to say is what the work does NOT say, because that is where it will get twisted in translation. The authors explicitly state that they treat access consciousness as a purely functional notion and take no position on subjective experience. The paper does not claim that models are conscious. It claims that there is an internal organization with similar functional properties. The distinction matters especially in the region, where much AI coverage arrives translated from English-language headlines and where a story saying "models are conscious" has real regulatory consequences for debates that are already open.

The second is good news with a catch. The tool is lightweight to operate: it does not require retraining the model and it produces readable outputs, with a one-time upfront computation of the Jacobians. It is exactly the kind of audit instrument that a regulator, a university, or a ministry team in the region could operate without buying frontier compute capacity. But to apply it you need access to the model's internal states, and only whoever holds the weights, or the lab itself, has that. A state that consumes closed models through an API cannot use this, nor hire someone to use it. It connects directly with the open weights story we have been following: a concrete audit technique appears and the bottleneck is once again the same, who has access to the guts. This reading is mine, not the paper's, which does not discuss access policy.

Third, on what it enables. If a model's strategic deliberations become legible before they come out in the answer, that changes what it means to audit an AI system in the public sector. Today the audits discussed in the region look at inputs and outputs. This suggests there is an observable intermediate layer. It is worth being cautious: these are results from a lab on its own models, and it remains to be seen whether they survive independent replication before writing them into a regulation.

## The fine print

- It is internal evidence, not an independent audit. Anthropic studies its own models and publishes on its own channel, without external peer review. That does not invalidate it, but it changes how much weight it should be given.
- The authors claim nothing about subjective consciousness and say so explicitly. Any headline that suggests otherwise is adding something the text does not contain.
- The work itself lists important limitations, and they are worth keeping in view: the lens only names concepts that exist as a single token in the vocabulary, so it misses notions written with several words; it treats the workspace as a bag of loose concepts and does not see how they relate to one another; readings from the first third of the layers turn out noisy and generally uninterpretable; the boundary between what is workspace and what is already output is set by the authors' judgment and not by a principled definition; and there is no way to predict in advance which tasks will use the workspace and which will not. The authors themselves describe the lens as an imperfect instrument that captures the structure of the workspace only approximately and incompletely.
- It was studied on large production models. It is not known how it scales to smaller models, which are the ones the region has most readily at hand.
