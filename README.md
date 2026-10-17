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

## What gets built

A scheduler for adults with ADHD. Four capabilities:

- **Daily tasks** with alerts and reminders.
- **Weekly and monthly goals**, decomposed into daily actions.
- **Completion logging** — whether a task was actually done, not just scheduled.
- **Follow-up on a missed task**, re-prompting rather than letting it disappear.

Each capability replaces something the trials paid human staff to provide:

| Capability | What it replaces in the trials |
|---|---|
| Scheduling | Physiotherapist-led appointments, 2 x 50 min per week |
| Alerts and reminders | Automated email plus "a reminder text message to their smartphone" |
| Catch-up prompts | Make-up rules: a missed session could be taken another day that week, or at home with self-monitored reporting |
| Completion logging | Attendance tracked against a 50% minimum participation floor |
| Goal decomposition | Occupational-therapist-led training in "time management skills, planning and organization", six 60-minute sessions |

All five come from the START trial (Arvidsson Lindvall et al., 2023,
protocol). The last row is the one this project exists for: that arm was
registered and never delivered as a randomised arm. See
`notes/literature/evidence-table.md` section 7.

**What this is not.** Not a general to-do application. The feature set is
constrained to what the review finds load-bearing, and the prototype is
judged on whether it delivers those capabilities reliably — not on feature
count or user satisfaction.


## What this project does not claim

It makes no claim that the intervention improves attention, focus, or ADHD
symptoms. The far-transfer literature is where such claims go to fail. The
outcomes here are task completion and adherence, which are directly
measurable. This is a support tool, not a treatment or a diagnostic.

## How to run it

### The research pipeline

Searches PubMed with the committed query and turns the results into a list
of candidate trials. Python standard library only: nothing to install.
Tested with Python 3.14 and Expat 2.7.4; parse.py refuses to run with an
Expat older than 2.7.2.

1. Run the tests:

~~~
python3 -m unittest -v
~~~

2. Set the email NCBI asks programs to identify themselves with. It is read
   from the environment and never written into the repository:

~~~
export NCBI_EMAIL="you@example.com"
~~~

3. Harvest. Reads the query from notes/inclusion-criteria.md, saves the raw
   XML to data/raw/<date>/ (not committed), and writes a manifest of the
   query, run time, count and PMIDs to data/manifests/<date>.json:

~~~
python3 harvest.py
~~~

4. Parse. Reads the newest manifest and its raw XML, checks every PMID is
   accounted for, and writes data/candidates/<date>.csv:

~~~
python3 parse.py
~~~

Dates are UTC. PubMed adds papers daily, so a new run produces a new dated
manifest and CSV rather than reproducing an earlier count. The first run,
2026-10-16, found 360 records.

### The scheduler

Built in Milestone 4. Instructions are added then.

## State

Week 8, October 2026. Literature pass complete: ten sources examined, nine
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

Pipeline built. Milestone 1 closed 2026-10-03, two weeks late. Milestone 2
(Working pipeline) completed 2026-10-16: harvest.py and parse.py are tested
and merged, and the first run found 360 candidate records. Next: screening
(Milestone 3) and choosing the scheduler's platform (Prototype design, #10).

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
