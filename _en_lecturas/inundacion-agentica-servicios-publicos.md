---
layout: lectura
numero: 34
tags: [agentes, gobernanza, latam]
title: "84 possible cases of public services flooded by AI-generated text"
description: "Schmitz, Hammond, and Chan posit that the phenomenon is probably already happening in many services, almost always through generated text, and that the quickest response, charging fees or adding obstacles, tends to reduce access."
date: 2026-11-16
paper_titulo: "Characterizing Agentic Flooding of Government Services"
paper_autores: "Schmitz, Hammond and Chan"
paper_publicado: "arXiv (preprint), August 2026; AIES 2026 proceedings"
paper_doi: "https://arxiv.org/abs/2608.16603"
paper_archivo: "cola-06-agentic-flooding-government.pdf"
paper_keywords: "agentic flooding, public services, administrative burden, AI agents, digital identity"
audio: true
hash_original: "b18f2438fd89"
---

## At a glance

- **The paper:** *Characterizing Agentic Flooding of Government Services*.
- **Authors:** [Chris Schmitz](https://scholar.google.com/scholar?q=%22Chris+Schmitz%22), of the Hertie School's Centre for Digital Governance; [Lewis Hammond](https://scholar.google.com/scholar?q=%22Lewis+Hammond%22), of the Cooperative AI Foundation; and [Alan Chan](https://scholar.google.com/scholar?q=%22Alan+Chan%22), of GovAI.
- **Publication:** [arXiv](https://arxiv.org/abs/2608.16603), open access. The first version was uploaded on August 17, 2026, and the second on the 19th. According to the cover page, it will appear in the proceedings of AAAI's 9th AIES conference, held in October 2026. The case database is on [GitHub](https://github.com/CLSchmitz/flooding-dataset).
- **Method:** qualitative case collection with a language-model-assisted workflow and human review, plus a risk matrix and a map of responses built on precedent and theory.

## First reading: what it does and what it finds

In Germany's social courts, some filings ran to more than 4,000 pages. That appears in a database Schmitz, Hammond, and Chan built to find out whether AI agents, by making dealings with the state cheaper, are already causing surges in demand that strain services. They call this agentic flooding and require two conditions for it: that it be caused by agents interacting with the service and that the strain be substantial. They distinguish quantitative flooding, more requests, from qualitative flooding, more complex requests.

The team reviewed 13 government domains in 12 countries, among them Brazil, the only one with a Latin American administrative tradition. A case was included only if it met three requirements: a plausible mechanism, evidence of a change in demand, and an explicit attribution to AI, made by the government or by a reliable external source. The database's figures:

- 84 cases in 11 jurisdictions;
- in 58 of them (69%), it is officials who state that AI was involved;
- in 87%, the mechanism is a language model that cheaply drafts legally sophisticated texts;
- 60% are coded as quantitative flooding and 90% as qualitative;
- in 56%, the government responded explicitly.

The pattern is almost uniform: AI-generated text, submitted by people who do the rest of the process by hand. More sophisticated uses, such as agents navigating portals on their own, are not yet seen in the database, according to the authors. The observed impacts are moderate, they write, and they consider acute operational collapse unlikely.

Looking ahead, based on the common features of its database, the paper posits that the near-term risk appears greater in financially attractive services whose demand was held back by the complexity of the process, such as taxes and courts, and warns that this pattern may also reflect which cases officials notice. To assess each service, it proposes a matrix of thirteen factors. It then sorts the responses into two strategies, and according to the precedent reviewed, both would probably suffice. Suppressing demand with fees, in-person appointments, or per-person limits is the quickest to apply. It happened in 14 cases: Australia considered reinstating fees for freedom of information requests, and Japan blocked submissions by IP address in a public consultation. The cost, the authors warn, is that this friction deters above all poorer users or those with less digital literacy. Increasing capacity, by redesigning services or using AI for processing, could avoid that cost, but it requires time and investment, and a structural redesign can take years.

The database supports something narrower than its size suggests: there are many episodes, in several countries, in which those who run a service attribute a new burden to AI. How much flooding there is and exactly what role agents play are beyond its scope, because the method, they themselves point out, does not allow causal or quantitative claims.

## Second reading: from Latin America

The Brazilian case in the database is INSS's auxílio-doença, the temporary incapacity benefit. The authors code it as qualitative flooding and use it as an example of bad faith: people seeking the benefit with AI-generated medical certificates. They also record the response, AI tools to detect those fake certificates.

In this blog's view, the case combines two factors from the matrix at once. It is a cash payment, the type of service the paper sees as most exposed, and its digital channel does away with a filter that, according to the authors, no agent gets through: the in-person appointment. In April 2026, the [Ministry of Social Security announced](https://www.gov.br/previdencia/pt-br/noticias/2026/abril/atestados-medicos-de-ate-90-dias-nao-tem-mais-pericia-presencial) that medical certificates of up to 90 days no longer go through in-person examination. If the pattern of the Brazilian case holds, that expansion would place more weight on the automated detection INSS has already adopted. Finding out would require comparing the share of certificates rejected as fake before and after the change, a figure INSS could publish.

Chile offers a contrast on the legal side. The paper warns that some forms of friction may be prohibited by law and recommends reviewing which responses the law allows before a wave. For freedom of information requests, [Law 20,285](https://www.bcn.cl/leychile/navegar?idNorma=276363), in its text in force as of November 2026, sets free access as a principle (Article 11, letter k), and its Article 18 limits charges to the direct costs of reproduction. The Australian shortcut of reinstating fees would not be available without amending the law. Faced with a surge attributed to AI, what would remain are frictions that do not charge, such as the IP address blocking Japan used or per-person limits, and the slow responses on the map: redesigning the channel or adding capacity. Whether Chilean law allows those frictions is the legal review the paper recommends carrying out before a wave.

Neither is a finding of the study, which does not compare countries. They are the matrix applied to two services in the region, and testing them depends on volume series that most cases in the database do not include.

## The fine print

- Only 25 cases have volume series, so the paper rules out even correlational claims. Some series in its Figure 1 rise before the launch of ChatGPT.
- Requiring public attribution probably leaves out real cases and could include others that were misattributed.
- The workflow used Gemini 3.1 Pro Preview and Flash-Lite, with instructions in English and a cost of about $200. The human reviewer was the first author; there was no inter-rater coding.
- The countries were chosen because they report publicly on their administration, with no claim to representativeness.
- The matrix rests mostly on precedent and theory rather than on the data, and it has yet to be validated.
- Funding: the Dieter Schwarz Foundation, through the Hertie School; part of the work was done during a GovAI fellowship, Chan's institution.
- The result is enough to audit services with a checklist of factors. The magnitude of the phenomenon remains unmeasured.

<small>**Revised on November 16, 2026.** The risk of lucrative and complex services is now attributed to the analysis of the database rather than to the matrix, the capacity route is described as possible rather than immediate, and the paragraph on Chile no longer reduces the options to the slow responses.</small>
