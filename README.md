# adhd-exercise-adherence

Senior design project, CSC/CTC 492, Fall 2026.
California State University, Dominguez Hills.

## What this project is trying to find out

> **Can software deliver the executive-function scaffolding — scheduling,
> initiation prompting, and completion tracking — that behavioral
> interventions for adults with ADHD currently supply with human staff?**

Three sub-questions:

1. What scaffolding do published interventions actually provide, and how
   consistently is it reported?
2. Which of those components can software deliver without a person present?
3. Does a prototype deliver them reliably enough to be trusted?

## The work this follows

Three papers define the gap this project occupies.

**Svedell et al. (2023)** identified the problem. In a 12-week exercise pilot
for adults with ADHD, 33% of the intervention group dropped out before
attending a single session, and none dropped out after starting. The authors
attributed this to executive-function impairment: "difficulties with planning
and organization are expected to be obstacles to achieving sustained
participation." One participant reported: "It has not been possible to
exercise on my own at all... Even though I felt motivated, it didn't work."

**Arvidsson Lindvall et al. (2023)**, the START trial protocol, proposed the
solution. A third randomized arm would deliver occupational-therapist-led
cognitive skills training "aiming to improve time management skills, planning
and organization," six 60-minute sessions over 12 weeks.

**Axelsson Svedell et al. (2025)**, the START results, abandoned it. Eleven of
43 intervention participants received the training as an ad-hoc adherence fix
and were pooled into the exercise arm, which the authors describe as "a
confounding factor... that could not be isolated in the results."

The START protocol states the gap directly: whether such training "can
contribute to increased physical activity or to maintaining routines for this"
has not been studied. This project picks up that thread.

## What this project does not claim

It makes no claim that the intervention improves attention, focus, or ADHD
symptoms. The far-transfer literature is where such claims go to fail. The
outcomes here are task completion and adherence, which are directly
measurable. This is a support tool, not a treatment or a diagnostic.

## How to run it

Nothing to run yet. This section gets written when there is a pipeline, and it
will contain the exact commands needed to reproduce every number in the
write-up.

## State

Week 6, October 2026. Literature pass complete: ten sources examined, nine
read in full text, with access levels and unverified claims tracked in
`notes/literature/evidence-table.md`.

Direction changed this week. The project began as "find an exercise that
improves focus and deliver it in an app." The evidence did not support that:
the best-ranked modality works because it is externally paced and cannot be
delivered by software, exergaming was the only category in Zhu et al.'s
network that failed to beat control, and the adult chronic-exercise literature
is too thin to pool. The binding constraint identified across these trials is
adherence, not exercise selection. The project now targets the scaffolding
itself. The rejected approach is recorded on the wiki Appendix page.

No pipeline yet. Milestone 1 closing; Milestone 2 next.

## Layout

    notes/          research notes, dated, committed as written
      literature/   evidence table, reading list, per-paper extractions
    sandbox/        one folder per technology investigated, each with a README
                    saying what it showed. Never imported by the pipeline.
    paper/          the write-up in LaTeX, with its bibliography
    AGENT-LOG.md    what the agent did, and what was checked before accepting
    AGENTS.md       standing instructions read by any coding agent

## A note on method

Parts of this project are written with a coding agent. What it produced and
what was checked before acceptance is recorded in `AGENT-LOG.md`. Citations
and numbers are held to the rule in `AGENTS.md`: nothing enters the
bibliography unopened, and nothing enters the write-up unreproduced.
