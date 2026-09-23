# adhd-exercise-adherence

Senior design project, CSC/CTC 492, Fall 2026.
California State University, Dominguez Hills.

## What this project is trying to find out

Exercise interventions for adults with ADHD consistently identify **adherence**,
not exercise selection, as the binding constraint. Trials solve it with human
staff: supervised group sessions, physiotherapists, and in one case an
occupational therapist delivering time-management and planning support.

The START trial registered a third arm to test exactly that cognitive
scaffolding, then failed to deliver it. Eleven of 43 intervention participants
received the training as an ad-hoc adherence fix and were pooled into the
exercise arm, which the authors describe as "a confounding factor... that could
not be isolated in the results." Their own protocol states that whether such
training "can contribute to increased physical activity or to maintaining
routines for this" has not been studied.

This project asks whether that scaffolding can be characterised and, ultimately,
delivered by software:

> Can software substitute for the executive-function scaffolding that
> exercise-for-ADHD trials currently supply with human staff, and what
> proportion of the documented adherence failure occurs at a point software
> could reach?

The research question is not final. It is being settled during the Literature
and scope milestone. See `notes/literature/evidence-table.md`.

## How to run it

Nothing to run yet. This section gets written when there is a pipeline, and it
will contain the exact commands needed to reproduce every number in the
write-up.

## State

Week 5. Literature review underway: seven sources examined, five read in full
text, with access levels and unverified claims tracked explicitly in
`notes/literature/evidence-table.md`. Repository scaffolding in place. No
pipeline yet. Milestone 1 in progress, running late.

## Layout

    notes/          research notes, dated, committed as written
      literature/   evidence table and per-paper extractions
    sandbox/        one folder per technology investigated, each with a README
                    saying what it showed. Never imported by the pipeline.
    paper/          the write-up in LaTeX, with its bibliography
    AGENT-LOG.md    what the agent did, and what was checked before accepting
    AGENTS.md       standing instructions read by any coding agent

## A note on method

Parts of this project are written with a coding agent. What it produced and what
was checked before acceptance is recorded in `AGENT-LOG.md`. Citations and
numbers are held to the rule in `AGENTS.md`: nothing enters the bibliography
unopened, and nothing enters the write-up unreproduced.
