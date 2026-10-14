# Inclusion criteria

Written 2026-10-07, before any search was run. Issue #9.

The search finds candidates; these rules decide which ones count. Each
criterion is answered yes or no for a given paper. A paper is included only
if it meets every inclusion criterion and none of the exclusions.

## Population

1. Participants are adults with ADHD.
   - **Age:** the trial's own eligibility rules require participants to be
     18 or older. A trial that admitted anyone under 18 is excluded, even
     if the average age is adult.
   - **Diagnosis:** participants have a formal ADHD diagnosis made by a
     clinician against standard criteria (DSM or ICD). A screening
     questionnaire or self-report alone does not qualify.

## Intervention

2. Participants receive assistant-type support (scheduling, prompting,
   checking in, or teaching planning skills) delivered by either:
   - a human: coach, therapist, occupational therapist, exercise staff, or
     similar; or
   - software alone: an app, website, or automated messages, with no human
     delivering the support.

   The support may accompany any kind of activity, including exercise.

## Comparison

3. No comparison group is required. Trials are compared against each other
   by the kind and amount of support given. Two-group trials are recorded
   as such so they can be reported separately as the stronger evidence.

## Outcomes

4. The paper reports at least one of: attendance or sessions completed,
   dropout, or tasks or goals completed. Attention, focus, or symptom-scale
   outcomes do not qualify on their own.

## Publications

5. A peer-reviewed journal article reporting the trial's results.
6. Written in English.

No date limit.

## Exclusions

| Excluded | Reason |
|---|---|
| Trial admitted anyone under 18 | Age rule |
| No formal ADHD diagnosis | Cannot claim participants have ADHD |
| No assistant-type support (e.g. medication only) | Nothing to study |
| Only attention, focus, or symptom outcomes | The project makes no attention or focus claims (README) |
| Trial protocols | No outcomes yet; followed to the results paper if one exists |
| Conference abstracts | Too little detail to tell what support was given |
| Not in English | Every included paper must be read in full |

## Recorded for every included trial

- **Design:** two-group or single-group.
- **Support source:** human, software, or both.

## Limitations these rules create

- English only: trials published in other languages are not seen.
- The strict age rule excludes mixed-age trials, such as college samples
  that admitted 17-year-olds.
- Comparing across trials is weaker evidence than comparing within one,
  because trials differ in more ways than their support.

## Search


Run on the PubMed website (pubmed.ncbi.nlm.nih.gov) on 2026-10-12.
`harvest.py` sends this exact string to PubMed's E-utilities API.

~~~
("Attention Deficit Disorder with Hyperactivity"[mh] OR ADHD[tiab] OR "attention deficit"[tiab]) AND ("Adult"[mh] OR adult*[tiab] OR "college student*"[tiab] OR "university student*"[tiab]) AND (coach*[tiab] OR "Mentoring"[mh] OR "Cognitive Behavioral Therapy"[mh] OR "cognitive behavio*"[tiab] OR "Occupational Therapy"[mh] OR "time management"[tiab] OR "organizational skill*"[tiab] OR "Self-Management"[mh] OR "Exercise"[mh] OR "Exercise Therapy"[mh] OR exercise[tiab] OR "physical activity"[tiab] OR "Reminder Systems"[mh] OR reminder*[tiab] OR "Mobile Applications"[mh] OR smartphone*[tiab] OR app[tiab] OR apps[tiab] OR "Text Messaging"[mh] OR "text messag*"[tiab] OR "Internet-Based Intervention"[mh] OR "Telemedicine"[mh] OR "digital intervention*"[tiab]) AND ("Randomized Controlled Trial"[pt] OR "Clinical Trial"[pt] OR "Controlled Clinical Trial"[pt] OR random*[tiab] OR trial[tiab] OR pilot[tiab] OR feasibility[tiab] OR "open label"[tiab] OR "single arm"[tiab] OR "pre-post"[tiab])
~~~

### How each block narrowed the results (2026-10-12)

| Blocks combined | Results |
|---|---|
| 1. ADHD | 61,246 |
| 1 + 2. Adults | 18,906 |
| 1 + 2 + 3. Assistant-type support | 990 |
| 1 + 2 + 3 + 4. Trials | 359 |

PubMed adds papers daily, so the same query returns a different count on a
later date. The count is only meaningful with its date.

### Choices made in the query

- **Outcomes are not searched for.** Abstracts often omit attendance or
  dropout even when the paper reports them, so searching for them would
  silently lose eligible trials. Outcomes are checked at screening.
- **The search is wider than the criteria.** "College student" and
  "university student" are included even though trials admitting anyone
  under 18 are excluded. The search has to find a trial before screening
  can exclude it.
- **`app[tiab] OR apps[tiab]`, not `app*`.** `app*` would also match
  "approach", "applied" and "appropriate", which flood the results.
- **Pilot and single-arm terms are included** because single-group trials
  are eligible (criterion 3) and often describe themselves that way rather
  than as randomized trials.
- **Reviews are not excluded in the search.** A `NOT review` rule would also
  drop trials whose abstracts mention a review. Reviews are excluded at
  screening, and their reference lists can be checked for missed trials.
- **General words like "support" and "intervention" are left out** of
  block 3, because almost every paper uses them.
