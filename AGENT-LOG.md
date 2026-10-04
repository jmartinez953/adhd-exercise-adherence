# Agent log

What a coding agent did, and what I checked before accepting it.

The rule this file enforces: the agent can describe a change, but it cannot
report a check it did not watch me perform. Every "What I checked" entry is
something I ran myself.

| Date | Issue | What the agent did | What I checked |
|------|-------|--------------------|----------------|
| 2026-09-15 | - | Read 7 sources on exercise and attention in ADHD; produced `notes/literature/evidence-table.md` with per-paper extractions and access tags | **Verified 2026-10-04 against the source papers.** Zhu et al. (PMC10080114): open-skill SUCRA 98.0%, SMD 1.96 (95% CI 1.15-2.77) for executive function - matches. Mehren et al. (PMC6443849): flanker task began 9.8 min post-exercise, range 7-16 - matches. |
| 2026-09-22 | - | Drafted `README.md`, `AGENTS.md`, `.gitignore`, this file | Read each file in full before committing |
| 2026-10-02 | - | Read Yang et al. (2025), J Glob Health 15:04025, in full; wrote evidence-table section 8 | **Not independently verified.** Figures are the agent's extraction. |
| 2026-10-03 | #5 | Drafted the scheduler specification for README and the Design wiki page | Read the full diff; confirmed insertion not overwrite (30 insertions, 0 deletions); confirmed the mapping table matches across README, wiki and deck |
| 2026-10-04 | #6 | Corrected the Mehren claim in the presentation deck | I found the error myself while spot-checking. See below. |

## Verification status

Both spot-checks listed as outstanding on 2026-09-22 are **complete as of
2026-10-04**.

### What the Mehren check found

The T2 measurement at 33.2 minutes was an **fMRI measurement of brain
activation** using a passive checkerboard task - not a cognitive performance
measure. The authors' words:

> "For the visual task at T2, there was no difference in brain activation
> between the two conditions, implicating a limited duration of exercise
> effects."

**Consequence:** "the effect is gone by 33 minutes" is *not* supported. The
defensible claim is that the study cannot speak to persistence beyond about
26 minutes - the flanker task ran roughly 7 to 26 minutes post-exercise -
and that the authors' own imaging check at 33 minutes was null.

The agent's original extraction said "the 33-minute probe was negative"
without specifying what it measured. Accurate as far as it went, and
imprecise enough to support a claim the paper does not.

### Still unverified

- Yang et al. (2025) figures in evidence-table section 8.
- Xu et al. (2026) acute effect sizes, taken from a paywalled abstract.

## Notes on method

Early in this project the agent reported study counts and participant numbers
taken from search-engine snippets rather than from the papers themselves.
Those figures were wrong in attribution and would have entered the
Milestone 1 write-up uncorrected.

The rules in `AGENTS.md` under "Research integrity" were written in response,
and the access-tag scheme in the evidence table exists to make that kind of
failure visible rather than plausible. The 2026-10-04 spot-checks are the
first time the process caught a **substantive** error rather than a cosmetic
one.
