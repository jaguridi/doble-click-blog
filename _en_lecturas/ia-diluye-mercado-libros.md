---
layout: lectura
numero: 18
tags: [mercados, trabajo, gobernanza]
title: "AI books sell little each, but they lower what every title earns"
description: "Almost 14,500 self-published novels on Amazon, with AI detection on the full text and real daily sales. Books with substantial AI make up 20% of the catalog and just 12% of sales, but the catalog grew much faster than the money available, and books with no AI detected also earn less than before."
date: 2026-08-17
paper_titulo: "Generative AI floods and dilutes the market for books"
paper_autores: "Chakrabarty, Liu, Ginsburg and Dhillon"
paper_publicado: "arXiv, July 2026"
paper_doi: "https://doi.org/10.48550/arXiv.2607.20349"
paper_archivo: "chakrabarty-2026-generative-ai-floods-book-market.pdf"
paper_keywords: "generative AI, self-published genre fiction, market dilution, AI detection, copyright fair use"
audio: true
hash_original: "80ada3d1a478"
---

## At a glance

- **What it is:** *Generative AI floods and dilutes the market for books*
- **Who:** [Tuhin Chakrabarty](https://scholar.google.com/scholar?q=%22Tuhin+Chakrabarty%22) and [Xinyue Liu](https://scholar.google.com/scholar?q=%22Xinyue+Liu%22+Stony+Brook) (Stony Brook University), [Jane C. Ginsburg](https://scholar.google.com/scholar?q=%22Jane+C.+Ginsburg%22) (Columbia Law School), and [Paramveer Dhillon](https://scholar.google.com/scholar?q=%22Paramveer+Dhillon%22) (University of Michigan and MIT Initiative on the Digital Economy).
- **Where:** preprint on arXiv, version of July 26, 2026. Not peer reviewed as of this reading. [doi.org/10.48550/arXiv.2607.20349](https://doi.org/10.48550/arXiv.2607.20349)
- **Type:** observational market study. 14,419 self-published genre fiction e-books on Amazon between January 2023 and March 2026, with daily sales through June 2026 and AI detection on the full text of each book.

## First reading: what it does and what it finds

The starting point is a widespread belief: books written with AI are *slop*, cheap text that readers will ignore, so it does not matter how many there are. The authors separate two things that argument lumps together. That average quality is low does not mean the effect on the market is zero, because a book that costs almost nothing to produce can be produced by the hundreds, and at that volume even a mediocre product absorbs attention and sales that would have gone elsewhere.

To measure it, they assembled an unusual panel. Daily sales, price, and ranking come from a proprietary database belonging to one of the Big Five publishers, which covers around 95% of the daily volume of the e-book market. From there they drew a sample stratified by genre and date, chosen blind to content, and classified each book with the Pangram detector, chapter by chapter. The score is the percentage of text windows flagged as not written by humans, and with it they build three bands: no AI detected, light AI (up to 25%), and substantial AI (above 25%).

The first finding deflates the panic. Books with substantial AI appear in all eight genre groups, but they sell poorly: they are 20% of the sample and just 12.1% of sales, while those with no AI detected are 62.9% of titles and take 71.7%. The second points in the opposite direction: even so, they did not stay at the bottom. Their share of sales went from almost zero in early 2023 to about 20% by mid-2026, and among new titles entering the Top 25 the authors construct, the share with substantial AI rose from almost zero to 31%.

The third is the one that gives the paper its title. Between early 2023 and early 2026, the cumulative catalog of published titles grew 38.3-fold and the number of books selling anything in a quarter grew 19.2-fold, while units sold grew 7.3-fold and revenue 8.9-fold. The market added books much faster than it added money, so what each title earns fell. Comparing the 2023 launch cohort with the 2025 cohort over a fixed 90-day window, revenue per book fell in six of the eight genres. And the drop also appears when looking only at books with no AI detected: there it fell in seven of eight. That is why the authors rule out a composition effect, that arithmetic quirk where the average falls just because many titles that sell little came in.

The fourth closes the argument: the losses are concentrated where there is more AI. In the months and genres with the lowest exposure, books with no AI detected hold about 88% of Top 25 positions; in those with the highest exposure, about 63%. The drop is steeper where there is more Kindle Unlimited, because there readers draw from the same subscription pool and each new title competes for the same borrows. And in the genre that AI reached later and less, fantasy, paranormal, and horror, revenue per book for titles with no AI detected rose 35%.

Two more pieces, one for each side of the market. Of the 385 bylines that kept publishing books with substantial AI, 287 increased their monthly output, and the top-grossing one generated $1.7 million in gross revenue with eight titles. And among the bestsellers, books with substantial AI are more saturated with rare expressions that already appear in existing books: 45% coverage in the Top 50, versus 37.7% for those with no AI detected, with similar gaps in the Top 100 and the Top 200. Against a third comparison group, 200 award-winning works of fiction, the distance is greater: 19.1% versus 41.6% for those with substantial AI and 37.2% for those with no AI detected.

## Second reading: from Latin America

It is worth saying up front: the paper does not look at the region. It is an English-language market, on one platform, in one segment. What travels is the mechanism, and the authors themselves say so: the conditions that made this market vulnerable are not unique to it. Near-zero entry costs, readers who come back for more of the same, discovery through a shared pool of rankings where human and synthetic works compete on equal footing, and zero obligation to disclose how the work was produced. Wherever those conditions hold, they expect the same, and they name music, stock images, and short-form writing.

That yields the most useful regional reading, which is mine and not the paper's: if the damage depends on the ratio between new titles and available money, small markets are more fragile, not less. Genre fiction in Spanish moves a much smaller revenue pool than the US market, and in a smaller pool far fewer titles are needed to produce the same dilution. The paper has no data on this and I leave it as a hypothesis. But the asymmetry is hard to dodge: producing is cheap in any language, and what changes between markets is how much there is to go around.

The second point is which lever remains at hand. A good part of the article is built for a US legal question, the effect on the market as a *fair use* criterion, and for the dilution theory that Judge Chhabria raised in *Kadrey v. Meta*, saying that precisely the evidence this paper produces was missing. That doctrine does not exist in the region's copyright systems, which work with closed lists of exceptions: the economic finding crosses the border, the legal vehicle does not. What can be discussed here is disclosure, because none of these books states whether it contains AI text. The authors speculate that this opacity confers an advantage and make clear they have no data to back that claim, but it is the only condition on the list that can be changed without waiting for the ruling on the merits about training.

And there is something the paper leaves on the table for any regional discussion about compensating authors: the evidence here is not about quality, it is about volume. AI books sell poorly one by one and still move the needle, which suggests that trusting the public to tell good from bad is not enough to protect writers' income. The question that remains is practical: if the mechanism is scale, what instrument does a mid-sized country have so that its authors do not end up competing with an infinite supply on the same shelf?

## The fine print

- The comparisons are observational and associative, and the authors say so: they compare cohorts and relate outcomes to exposure by genre; they do not estimate a causal effect.
- Everything rests on a detector. A book has "no AI detected" according to Pangram 3.3, not according to its author, and the reported error rates come from the vendor itself. The authors do show that the results hold up when the 25% threshold is moved.
- The sales panel was provided by one of the Big Five publishers, an interested party in the copyright debate. The analysis is the researchers', but the data come from an actor with a stake in the outcome.
- Author identity is taken from the book's byline, so someone who publishes under several pen names appears split up: the reported concentration is a floor.
- The authors note that the net effect on welfare remains open, because readers may gain from more variety and lower prices. What they measure is the loss for those who write.
- The overlap in rare expressions is aggregate: it shows similarity to the distinctive language of existing books, not copying of any one in particular.
