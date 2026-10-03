# Evidence table — exercise interventions and attention outcomes

**Compiled:** 2026-09-15
**Status:** 5 papers read in full text. All numbers below verified against the source document, not against abstracts or search summaries.
**Intended destination:** `notes/literature/evidence-table.md` in the project repository, and the `Reading` page of the project wiki.

---

## How to read this file

Every claim here is tagged:

- **[VERIFIED]** — the full text was read and the number was taken from the document itself.
- **[UNVERIFIED]** — came from a search result summary or abstract. Not citable. Must be opened before use.

Do not move an **[UNVERIFIED]** line into the paper, a presentation, or a wiki page without opening the source first.

---

## 1. Zhu et al. (2023) — network meta-analysis, children/adolescents with ADHD

**Citation.** Zhu, F., Zhu, X., Bi, X., Kuang, D., Liu, B., Zhou, J., Yang, Y., & Ren, Y. (2023). Comparative effectiveness of various physical exercise interventions on executive functions and related symptoms in children and adolescents with attention deficit hyperactivity disorder: A systematic review and network meta-analysis. *Frontiers in Public Health*, 11, 1133727. https://doi.org/10.3389/fpubh.2023.1133727
PMID 37033046 · PMCID PMC10080114 · PROSPERO CRD42022365188

**Population.** Children and adolescents under 18 with a diagnosis of ADHD, any subtype. Ages across included studies span 4–18. Male:female approximately 4:1. Mixed medication status.

**Scale.** 59 studies in the systematic review (39 RCTs, 5 quasi-RCTs, 15 self-controlled). 44 studies / 1,757 participants in the meta-analysis. Executive-function network: 33 studies, 1,289 participants. Median therapy length 12 weeks, median session 45 min, mostly moderate to moderate-vigorous intensity.

**Intervention taxonomy (the paper's own definitions, verbatim).**

| Node | Definition |
|---|---|
| Open-skill | "require participants to react in a dynamically changing and **externally paced** environment" — football, table tennis, badminton, tennis |
| Closed-skill | "require participants to perform in a highly consistent, stationary, and **self-paced** environment" — swimming, running, cycle ergometer, rope skipping |
| Multicomponent | combination of open- and closed-skill |
| Exergaming | "the combination of physical and cognitive training in a gamified fashion" |
| Specific technique | HIIT, MICT |

**Results.** [VERIFIED]

| Outcome | Top-ranked | SUCRA | SMD (95% CI) | Significant? |
|---|---|---|---|---|
| Executive function overall | Open-skill | 98.0% | 1.96 (1.15 – 2.77) | Yes |
| Inhibitory control | Open-skill | 99.1% | 1.94 (1.24 – 2.64) | Yes |
| Inattention | Closed-skill | 96.3% | −1.51 (−2.33 – −0.69) | Yes |
| Hyperactivity/impulsivity | Closed-skill | 72.5% | −1.60 (−3.02 – −0.19) | Yes |
| Working memory | Closed-skill | 75.9% | 1.21 (−0.22 – 2.65) | **No — crosses null** |
| Cognitive flexibility | Multicomponent | 70.3% | 1.44 (−0.19 – 3.07) | **No — crosses null** |

Pooled, all exercise vs control: EF SMD 1.15 (0.83 – 1.46); hyperactivity/impulsivity −1.01 (−1.65 – −0.36); inattention −0.65 (−1.11 – −0.20).

**The exergaming result.** [VERIFIED] Exergaming was the only category that did not beat control: *"all types of physical exercise interventions except exergaming were superior to non-physical exercise controls."* Only 3 of 59 studies. No SUCRA or SMD reported for it. HIIT also failed: *"no significant effect of HIIT was observed in our study."*

**Quality problems.**

- Heterogeneity I² = 79.0% (EF), 88.0% (hyperactivity/impulsivity), 81.0% (inattention). The paper's own threshold for "high" is 75%.
- PEDro scores 4–8. No study above 8. None rated excellent. Only one study used allocation concealment. Blinding of participants and outcome assessment generally absent.
- GRADE certainty "high to very low."
- Publication bias assessed by **visual inspection of funnel plots only**. No Egger's test, no trim-and-fill.
- Network is near star-shaped: *"direct comparisons between closed-skill activities and open-skill activities as well as exergaming were lacking."* Rankings rest almost entirely on indirect evidence.
- **The paper never names a single cognitive instrument.** No Stroop, flanker, CPT, digit span, or any other test appears in the text. Outcomes are labelled only "Executive function" and "Core symptom."

**Authors' own caution.** *"Our findings should be interpreted with caution, because limited quality and direct evidence were highly represented among the included studies."* Their Discussion says the paper *"provided little evidence"* that open-skill activities were most promising.

**App relevance.** The top-ranked modality is defined by external pacing — an opponent moving unpredictably in physical space. A phone cannot supply that. The equipment-free closed-skill subset (running, jumping, rope skipping) is the most app-deliverable and is top-ranked for inattention specifically.

---

## 2. Dinu et al. (2023) — adults with ADHD, acute bout, RCT

**Citation.** Dinu, L. M., Singh, S. N., Baker, N. S., Georgescu, A. L., Singer, B. F., Overton, P. G., & Dommett, E. J. (2023). The effects of different exercise approaches on attention deficit hyperactivity disorder in adults: A randomised controlled trial. *Behavioral Sciences*, 13(2), 129. https://doi.org/10.3390/bs13020129
PMID 36829357 · PMCID PMC9952527 · ISRCTN39271564

**Population.** 159 adults: 82 with ADHD, 77 healthy controls. Ages 18–35. ADHD group 83% female. 50 medicated, 32 unmedicated. Diagnosis was **self-reported clinician diagnosis plus ASRS ≥ 14** — not confirmed by the study.

**Design.** Acute single bout. Randomised to 10 min stationary cycling (70–80 RPM, achieved 53–59% HRmax) or 10 min video-led Hatha yoga. **No no-exercise control arm.** Not blinded.

**Instruments.** TOVA (omission errors, hit reaction time, d prime = attention; commission errors = motor impulsivity), Delay Discounting Test (AUC = temporal impulsivity), Iowa Gambling Task (cognitive impulsivity), wrist actigraphy.

**Results on attention.** [VERIFIED] All null in the ADHD group.

| Measure | Result |
|---|---|
| Omission errors | Time F(1,150)=0.20, p=0.653; all interactions p ≥ 0.249 |
| d prime | Time F(1,150)=0.93, p=0.326; all interactions p ≥ 0.075 |
| Hit reaction time | Time × Group p=0.044 — **driven by controls getting worse**; ADHD t(81)=0.85, p=0.396 |

**Verbatim, from the abstract:** *"There were no effects of exercise on attention, cognitive or motor impulsivity, or movement in those with ADHD."*

**Verbatim, from the abstract:** *"Exercise reduced attention and increased movement in controls."*

**The one positive result.** Delay discounting AUC improved — three-way interaction F(1,142)=4.79, p=0.03, ηp²=0.033 (small). Follow-up t-tests uncorrected for multiple comparisons. Note the yoga arm produced this effect **without raising heart rate at all** (pre 70.59 → post 69.94, p=0.405), which makes an expectancy explanation hard to exclude.

**Authors' stated limitations.** No blinding; female-dominated ADHD sample; **no no-exercise control** (*"the cognitive tests... are lengthy and it is possible that some effects observed were not related to exercise but merely fatigue"*); heart rate not measured during exercise; intensity *"only just within the range... associated with moderate exercise"*; diagnosis not confirmed.

**Why this paper matters most.** It is the best-powered adult attention result available and it is **negative**. Any project claiming exercise improves attention in adults has to account for this paper.

---

## 3. Mehren et al. (2019) — adults with ADHD, acute bout, crossover

**Citation.** Mehren, A., Özyurt, J., Lam, A. P., Brandes, M., Müller, H. H. O., Thiel, C. M., & Philipsen, A. (2019). Acute effects of aerobic exercise on executive function and attention in adult patients with ADHD. *Frontiers in Psychiatry*, 10, 132. https://doi.org/10.3389/fpsyt.2019.00132
PMID 30971959 · PMCID PMC6443849

**Population.** 40 analysed (20 ADHD, 20 matched controls) from 46 recruited. Mean age ~29. 16/20 male in ADHD group. Diagnosed by trained psychiatrist per NICE/DSM-IV. Only 4 on stimulants, withdrawn 48 h before each visit. ADHD group had significantly higher BDI (9.3 vs 2.3) and higher self-reported physical activity.

**Design.** Acute single bout, within-subject crossover, counterbalanced. Control condition = watching a movie (MASC-MCk), ~30 min. No true rest arm. Blinding not stated.

**Protocol.** 30 min continuous cycling at 50–70% individual HRmax, HRmax determined by maximal exercise test at visit 1, continuously monitored via Polar RCX5 chest strap and controlled by the experimenter. **Achieved intensity during the bout is not reported.**

**Instruments.** Eriksen flanker task (300 trials): RT congruent/incongruent/neutral, RT variability, error rate, omission rate, interference score. Plus fMRI.

**Results.** [VERIFIED]

| Measure | ADHD Movie | ADHD Exercise | Test |
|---|---|---|---|
| RT congruent | 488 ms | 462 ms | t(19)=3.64, p=0.002, d=0.81 |
| RT incongruent | 565 ms | 545 ms | t(19)=2.89, p=0.009, d=0.65 |
| RT variability (congruent) | 77 ms | 64 ms | t(19)=3.47, p=0.003, d=0.78 |
| **Interference score** | **77 ms** | **83 ms** | **worsened; no condition effect** |

**The critical distinction.** What improved was **speed**, not executive control. The pre-specified executive-function index — the interference score — did not improve in patients and numerically got worse. Verbatim: *"Interference scores, which are typically used to measure interference control in flanker task performance, were not different between the two conditions."*

**Other nulls.** *"No significant effects were obtained for the error rate or omission rate."* Whole-sample fMRI: *"we did not observe exercise-induced changes in brain activation during the flanker task when we examined the whole sample, neither in patients nor in controls."* No benefit in healthy controls.

**DURATION — the most important number in this entire file.** [VERIFIED]

> *"The average time interval between the end of exercising and the beginning of the experimental tasks was as follows: 5.9 min... for the visual task at T1, **9.8 min for the flanker task** (SD = 1.8, range 7–16), and 33.2 min... for the visual task at T2."*

The entire attention result lives in an approximately **7–26 minute window after the bike stopped.** There is no later cognitive measurement. The only ~33-minute probe was negative:

> *"For the visual task at T2, there was no difference in brain activation between the two conditions, **implicating a limited duration of exercise effects**."*

The design assumes effects are gone within 48 h — sessions were spaced *"at least 2 days... to avoid aftereffects."*

**This paper cannot support a claim of lasting improvement.** Its own durability probe pointed the other way.

---

## 4. Svedell et al. (2023) — adults with ADHD, 12-week program, feasibility pilot

**Citation.** Svedell, L. A., Holmqvist, K. L., Lindvall, M. A., Cao, Y., & Msghina, M. (2023). Feasibility and tolerability of moderate intensity regular physical exercise as treatment for core symptoms of attention deficit hyperactivity disorder: A randomized pilot study. *Frontiers in Sports and Active Living*, 5, 1133256. https://doi.org/10.3389/fspor.2023.1133256
PMID 37255729 · PMCID PMC10225649 · NCT05049239

**Population.** n = 14 randomised (9 intervention, 5 control). 3 dropped out before any session → 6 received intervention → 1 excluded for low attendance → **n = 5 for most analyses.** Adults 27–54, mean 37.0. 9 female / 5 male. 8 medicated. 81% overweight, 36% obese.

**Design.** Randomised pilot, 2:1. Control = treatment as usual. **Explicitly not powered for efficacy:** *"The pilot study was neither designed nor adequately powered to evaluate the effects of the intervention."*

**Protocol.** Physiotherapist-led mixed exercise in groups of 4–6. 50 min/session, 3×/week, 12 weeks. Target 60–90% HRmax, verified by Polar H10 chest strap paired to the participant's own smartphone. Session structure: 6 min warm-up, 6 min cardio intervals (3×1 min with 1 min active rest), 23 min resistance (3 rounds of 5×1 min), 10 min flexibility, 5 min cool-down. Goal ≥150 min/week moderate intensity.

**Results.** No effect sizes and no confidence intervals reported anywhere. Mann–Whitney U on n=5 vs n=5.

| Outcome | p |
|---|---|
| ASRS v1.1 total (self-report) | 0.036 * |
| Composite of 5 clinical scales | 0.008 * |
| AX-CPT accuracy | 0.032 * |
| **Go reaction time** | 0.413 |
| **NoGo reaction time** | 0.730 |
| **AY reaction time** | 0.413 |
| **BX reaction time** | 0.413 |
| **All fMRI group analyses** | null |
| **VO2max, BMI, waist, HR, BP, grip, steps** | all null |

Every reaction-time attention measure was null. The one significant attention-task result rests on 5 people per arm with an uninterpretable "+93.3% change" statistic and no raw scores.

**THE FINDING THAT MATTERS — adherence, not efficacy.** [VERIFIED]

- **33% of the intervention group dropped out before attending a single session.** None dropped out after starting. Attrition clustered entirely at the point of initiation.
- Participant quote, verbatim: *"It has not been possible to exercise on my own at all, I have been able to go for walks. **Even though I felt motivated, it didn't work**."*
- *"Participants found it easier to do the training with a group than alone by themselves. For some, the group was said to be a prerequisite for doing the exercises."*
- 67% *"experienced some degree of negative stress trying to catch up with the sessions."* Commonest drop-out reason: lack of time.
- Authors' own diagnosis: *"some participants also expressed difficulties with planning and organization... To find time for physical exercise and to manage the negative stress that this caused in their daily life were reported as major hinders for adherence. Given the impairment in cognitive functioning people with ADHD have, difficulties with planning and organization are expected to be obstacles to achieving sustained participation."*
- **Their fix:** *"We have, therefore, decided to add a third intervention arm to the planned RCT in which participants, besides the mixed exercise program, will also receive cognitive intervention by an occupational therapist with the aim of improving planning, organization and time management skills."*

**No adverse events section at all**, despite "tolerability" in the title.

**Data-quality note.** Multiple table means fall outside their own stated ranges (e.g. ASRS −15.3 ± 14.4 with range −100.0 to +10.0). No multiplicity correction across ~30 tests.

---

## 5. Lim et al. (2019) — children with ADHD, digital attention training, RCT

**Citation.** Lim, C. G., Poh, X. W. W., Fung, S. S. D., Guan, C., Bautista, D., Cheung, Y. B., Zhang, H., Yeo, S. N., Krishnan, R., & Lee, T. S. (2019). A randomized controlled trial of a brain-computer interface based attention training program for ADHD. *PLoS ONE*, 14(5), e0216225. https://doi.org/10.1371/journal.pone.0216225
PMID 31112554 · PMCID PMC6528992 · NCT01344044

**Included as the strongest available comparator for *digitally delivered* attention training.**

**Population.** 172 children randomised, aged 6–12, mean 8.6. 85.5% male. DSM-IV TR diagnosis confirmed by CDISC-IV structured interview. **Unmedicated**, with 4-week washout.

**Design.** Randomised, stratified, third-party allocation, outcome-assessor-blinded, **waitlist-controlled**. No sham, no active control. Randomised comparison exists **only for the first 8 weeks**; everything after is pooled single-arm pre-post.

**Intervention.** "Cogoland" — 3-D game controlled by EEG attention level via a 2-lead dry-electrode Bluetooth headband. 24 sessions over 8 weeks (3×/week), then 3 monthly maintenance sessions. Two 10-min games per session. **Clinic-based and supervised**, not home-based.

**Results.** [VERIFIED]

| Outcome | Rater | Effect at Week 8 |
|---|---|---|
| ADHD-RS Inattention | Clinician (blinded, but **interviewing unblinded parents**) | MD **1.6** (95% CI 0.3 – 2.9), p=0.0177, ~0.4 SD |
| ADHD-RS Inattention | Parent (unblinded) | MD **2.2** (95% CI 0.8 – 3.6), p=0.0024, "moderate" |
| CBCL Internalizing | Parent (unblinded) | MD **3.4** (95% CI 1.0 – 5.7), p=0.005 |
| CBCL Externalizing | Parent | MD 0.8 (95% CI −1.2 – 2.9), **p=0.417 — null** |
| CBCL Attention Problems | Parent | **null, reported with no numbers at all** |

**The pattern to notice.** The effect size grows as the rater becomes less blinded — smallest on the partially-blinded clinician rating, larger on unblinded parent rating, largest on parent-rated *internalizing symptoms*, the outcome least mechanistically related to attention training. This is the canonical signature of expectancy bias.

**Zero objective outcome measures.** No CPT, no reaction-time task, no EEG endpoint, no academic test, no actigraphy — despite the platform already running a Stroop task (for calibration) and academic questions (for generalisation), either of which could have been scored.

**Untreated controls improved 1.9 points on their own** — roughly half the treated improvement, from doing nothing.

**Developer-evaluated.** The system's inventors designed, delivered and rated the trial. Competing interests declared as none.

**Authors' own words on the missing sham:** *"We had originally planned to used a sham-control design, which would greatly improve the quality of the study, but decided against it."*

---

## 6. Xu, Zhao & Hu (2026) — adults with ADHD, acute AND chronic exercise, systematic review

**⚠️ ACCESS CAVEAT — READ FIRST.** This paper is **paywalled**. What was read verbatim: the full structured abstract, all four Highlights, the complete Introduction, first-sentence snippets of Methods/Discussion/Conclusion, and ~30 of 59 references. **Not accessed:** the Methods body, the entire Results section, all forest plots, all heterogeneity/risk-of-bias/publication-bias statistics, and the Limitations section. Do not cite anything from this entry as full-text-verified beyond the quoted lines below.

**Citation.** Xu, S., Zhao, C., & Hu, L. (2026). The effects of acute and chronic exercise on executive functions and core symptoms in adults with ADHD: A systematic review and meta-analysis. *Psychology of Sport and Exercise*, 84, 103088. https://doi.org/10.1016/j.psychsport.2026.103088
PMID 41638541 · PROSPERO CRD42024595524

**Scale.** *"Fourteen studies met the inclusion criteria for systematic review, with eight studies included in the meta-analysis."* From 3,085 initial records.

**ACUTE exercise — the only pooled estimates in the paper.** [VERIFIED from abstract]

| Outcome | Hedges' g | 95% CI | p |
|---|---|---|---|
| Inhibitory control | 0.55 | 0.32 – 0.79 | < 0.001 |
| Core symptoms | 0.23 | 0.03 – 0.43 | 0.024 |

**CHRONIC exercise — THE DECISIVE FINDING. No pooled effect size exists. None could be computed.** [VERIFIED, four separate verbatim quotes]

> Abstract: *"For chronic exercise interventions, qualitative synthesis of existing evidence suggested mixed results, which highlights the need for further research."*

> Highlight #3: *"Evidence for the effects of chronic exercise interventions in adults with ADHD was mixed."*

> Discussion: *"For chronic exercise interventions, the limited number of studies precluded quantitative synthesis, and the available evidence yielded mixed and"* [truncated by paywall]

> Conclusion: *"For chronic exercise interventions, qualitative synthesis of the available evidence suggested mixed and inconclusive results, highlighting the need for further investigation."*

**What this settles.** As of 2026, the published literature on multi-week exercise improving attention or executive function in *adults* with ADHD is too thin to meta-analyse. Only ~4 chronic studies exist and most are feasibility pilots. Any claim of durable adult benefit is not supported by pooled evidence, because there is no pooled evidence.

**Only inhibitory control was pooled.** No pooled estimate for working memory, cognitive flexibility, or attention appears anywhere accessible. Note "attention" is not one of the three EF domains the authors framed — it sits under core symptoms as "inattention."

**Nulls the authors cite in their own Introduction.** [VERIFIED]

> *"despite the promising evidence, some studies have failed to observe significant effects of exercise on executive functions or core symptoms in adults with ADHD. For example, Fritz and O'Connor (2016) implemented a 20 min moderate-intensity cycling intervention but found no significant improvements in attention or hyperactivity compared with a seated rest control condition. Similarly, Converse et al. (2020) reported no significant effects of chronic exercise on cognitive functions or ADHD symptoms."*

> *"The effectiveness of exercise on executive functions and core symptoms in adults with attention-deficit/hyperactivity disorder (ADHD) remains unclear."*

**Durability / follow-up: not stated anywhere accessible.** No statement about how long acute effects last, and no mention of post-intervention follow-up in any included study.

**Lead worth chasing.** [UNVERIFIED] A 2025 open-access review in *Journal of Global Health* (15:04025) reportedly reports a chronic-exercise SMD of −1.77 for inhibitory control in adults. Not read. If chronic adult effects matter to the project, open this.

---

## 7. The START trial (three papers) — adults with ADHD, 12-week exercise, Sweden

This is the same research group as Svedell et al. (#4) — START is the full RCT their pilot was preparing for. **Three papers exist.** All were accessed in full except where noted.

**Protocol.** Arvidsson Lindvall, M., Lidström Holmqvist, K., Axelsson Svedell, L., Philipson, A., Cao, Y., & Msghina, M. (2023). START – physical exercise and person-centred cognitive skills training as treatment for adult ADHD: protocol for a randomized controlled trial. *BMC Psychiatry*, 23(1), 697. https://doi.org/10.1186/s12888-023-05181-1 · PMID 37749523 · NCT05049239

**Primary clinical outcomes.** Axelsson Svedell, L., Arvidsson Lindvall, M., Lidström Holmqvist, K., Cao, Y., & Msghina, M. (2025). Physical exercise as add-on treatment in adults with ADHD – the START study: a randomized controlled trial. *Frontiers in Psychiatry*, 16, 1690216. https://doi.org/10.3389/fpsyt.2025.1690216 · PMID 41244864 · PMCID PMC12614457

**Body awareness / movement quality.** Axelsson Svedell, L., Lidström Holmqvist, K., Msghina, M., & Arvidsson Lindvall, M. (2026). Physical exercise and body awareness/movement quality in adults with ADHD: Results from the START randomized controlled trial. *Complementary Therapies in Medicine*, 98, 103372. https://doi.org/10.1016/j.ctim.2026.103372 · PMID 41903823

**Population.** 122 screened → 63 randomised 2:1 (43 intervention, 20 TAU). Ages 20–62, mean 36.1. 42 female. 63% on ADHD medication. 46.4% sedentary ≥10 h/day. Diagnosis by multidisciplinary neuropsychiatric evaluation per DSM-5.

**Protocol.** Physiotherapist-led group sessions, 2 × 50 min/week supervised, plus self-directed exercise to reach 150 min/week. Target 60–90% HRmax, verified by **Polar H10 chest strap paired to the participant's own phone**. Warm-up, endurance intervals, 5-exercise strength circuit, cool-down with stretching and body-mindfulness prompts. Missed sessions could be made up another day that week or **at home with self-monitored reporting**. Minimum participation floor 50%.

**The headline result — ASRS-v1.1 total, between-group at 12 weeks.** [VERIFIED]

> MD **−6.98**, 95% CI **−12.30 to −1.65**, t = −2.65, df = 39, **p = 0.012, Cohen's d = −0.93** (95% CI −1.65 to −0.21)

Intervention change −7.07 (SD 7.99); control −0.09 (SD 5.71). Strict-ITT sensitivity analysis: MD −4.89, 95% CI −8.28 to −1.49, p = 0.006, d = 0.71.

**This is the strongest chronic adult result located.** It is also the one that needs the most caveats:

- **The primary outcome is an unblinded self-report scale.** Participants cannot be blinded to whether they went to the gym.
- **The inattention subscore has NO published between-group test.** Within-group only: intervention 23.88 → 20.21, MD −3.67, p < 0.001, ES 0.77; control 26.00 → 25.73, p = 0.393. A within-group change in an unblinded arm is not an effect.
- CGI-I d = 2.45 and PGI-I d = 2.26 — effect sizes that large on clinician/patient impression scales in an unblinded trial are an expectancy signal, not a triumph.

### ⚠️ THE FINDING THAT DEFINES THE PROJECT: the cognitive-scaffolding arm was designed, registered, and never delivered

The protocol specified **three arms**: [VERIFIED]

> *"1. Physiotherapist-led structured physical exercise group (n = 40); 2. Physiotherapist-led structured physical exercise group with occupational therapist-led, person-centred cognitive skills training (n = 40); 3. Control group receiving TAU (n = 40)."*

That second arm was to deliver: [VERIFIED]

> *"an occupational therapist-led, person-centred cognitive intervention aiming to improve time management skills, planning and organization"* — *"60 min approximately six times (every second week) during the 12-week period"* — with goals such as *"to arrive on time for training, or to create the space for physical activity in one's everyday life through improved time management."*

**What actually happened,** from the Frontiers paper: [VERIFIED]

> *"In the START intervention, a subset of participants (n=11 of 43) were offered cognitive skills training **to improve adherence to protocol**... However, for the purposes of this study, all participants who received the START intervention, regardless of whether they received cognitive skills training or not, were considered part of the START intervention group."*

And in their limitations: [VERIFIED]

> *"A further limitation of the study is that some participants received cognitive skills training in addition to the exercise intervention. Subgroup analyses was originally intended but, in the end, not feasible due to the small sample size. **The cognitive skills training introduces a confounding factor**, as it may have contributed to changes in the outcome measures that could not be isolated in the results."*

**So: the exact intervention that would test whether executive-function scaffolding improves exercise adherence in adults with ADHD was formally proposed, registered on ClinicalTrials.gov, funded, partially delivered to 11 people as an ad-hoc fix, and then collapsed into the exercise arm as a confound. The question remains open. Nobody has answered it.**

The authors themselves stated the underlying gap in their protocol: [VERIFIED]

> *"there are studies that show that structured cognitive skills training improves the everyday functioning of adults with ADHD. However, **it has not been studied whether such training can contribute to increased physical activity or to maintaining routines for this.**"*

### Adherence — pre-specified, then never reported

The protocol committed to measuring adherence precisely: [VERIFIED]

> *"Group adherence to physical activity will be calculated as the number of patients attending 50% of the sessions. To maintain physical exercise for at least 150 min per week, the HR monitor connected to the participants' mobile phone will gather the time in an HR zone of > 60%. Attendance rate over the intervention period will be calculated as a mean of the individual percentage."*

**None of it was published.** No session-attendance percentage, no mean attendance rate, no proportion meeting the 50% floor, no HR-monitor minutes, no home-session logs — in either results paper. Treat any claim about START adherence rates as unsupported by the published record.

**What is known about dropout:** 35% overall. 22 of 63 had missing data at 12 weeks (11 lost to follow-up, 11 withdrew). Complete primary-outcome data for 41/63 (65%). Reasons, verbatim: *"reasons for dropping out were mainly reported as a lack of time, rather than the intervention being too demanding."* Per-arm attrition timing is only in a figure image and is not extractable.

### Why adherence is hard — the authors' own account [VERIFIED]

> *"One challenge that was seen in the pilot study was that some participants had difficulty in organizing and making time for the 12-week intervention. **To plan, accomplish and evaluate activities, executive functioning is fundamental**, which is also the case when it comes to performing physical activities."*

> *"adherence to the protocol and data collection may be especially challenging because of the symptomatology of adults with ADHD, such as difficulties in managing their time and planning and structuring their everyday life."*

**Scaffolding they actually built in:** make-up session rules; a 50% participation floor rather than strict attendance; automated email reminders plus SMS to the participant's smartphone; paper questionnaire fallback; two physiotherapists present at every session; individualised intensity; the OT cognitive training for 11 participants.

### Other problems worth noting

- **Selective outcome reporting.** The protocol pre-specified AX-CPT, Go/No-Go, IAPS, fMRI, ATMS-S, COPM, SDO-OB, AAQoL, GSES-10, SEE, Ekblom-Bak, Flamingo balance, grip strength, accelerometer and health-economic outcomes. **None are reported in either results paper.** Whether the data exist is not stated.
- **The body-awareness paper used one-tailed tests** (*"A one-tailed significance level was set at p < 0.05 for all tests"*), and five of its seven subscales were null between groups, as was clinician-rated movement quality.
- **Planned 6- and 12-month follow-ups are unpublished.** The protocol committed to them; neither results paper reports beyond 12 weeks.
- **Protocol-to-delivery drift:** 3 arms → 2; 1:1:1 → 2:1; n=120 → 63; 3 × 45 min/week → 2 × 50 min supervised/week; different primary outcome per paper. No paper narrates these amendments.
- Data collectors were **not blinded** — *"It was not possible to blind them because they were employees in the small unit where the intervention was given."*

---

## 8. Yang et al. (2025) — the chronic adult meta-analysis, and why its headline number is hollow

**Citation.** Yang, Y., Wu, C.-H., Sun, L., Zhang, T.-R., & Luo, J. (2025). The impact of physical activity on inhibitory control of adult ADHD: a systematic review and meta-analysis. *Journal of Global Health*, 15, 04025. https://doi.org/10.7189/jogh.15.04025
PMID 40084538 · PMCID PMC11907377 · INPLASY 202490109 (**not** PROSPERO-registered)

**Access: [VERIFIED] — free full text, read in full.** Supplementary figures (S1–S3) are bitmap images and are not text-extractable, so per-study forest-plot rows could not be read.

**Why it was opened.** A secondary source cited this paper's chronic-exercise SMD of −1.77 as a counterweight to Xu et al. (2026), who concluded the adult chronic literature could not be pooled. Determining which was right was the point.

**The headline numbers.** [VERIFIED]

| Subgroup | SMD | 95% CI | p |
|---|---|---|---|
| Overall (all 14 estimates) | −1.14 | −1.72 to −0.56 | 0.0001 |
| **Acute exercise** | −0.65 | −1.10 to −0.20 | 0.005 |
| **Chronic exercise** | **−1.77** | **−2.84 to −0.69** | 0.0001 (abstract) / 0.001 (results) |

Overall I² = 83%. No subgroup-specific I² reported.

### Why the −1.77 does not mean what it appears to mean

**The chronic subgroup is three studies.**

| Study | Design | N | Modality-specific result |
|---|---|---|---|
| Fritz & O'Connor (2022) | **pilot**, 6 wk | 32 | SMD 0.01, p = 0.97 — **null** |
| Converse et al. (2020) | **feasibility trial**, 7 wk | 21 | SMD −2.20, p = 0.25 — **not significant** |
| Kouhbanani et al. (2022) | RCT, 24 wk Pilates, **female only** | 52 | SMD −2.22, p < 0.0001 |

One null, one non-significant with a CI running from −6.25 to **+1.8**, and a single 52-person female-only Pilates trial carrying the entire effect. That trial measured **WCST and AX-CPT** — set-shifting and sustained attention — not inhibition. Its own title describes it as studying "attention switching and sustained attention."

**Total chronic N is 105** by the paper's own Table 1, not the 218 the narrative claims.

**Effect-size implausibility.** Stimulant medication produces executive-function effects around d ≈ 0.3–0.5 in adult ADHD. An exercise effect three to five times larger than methylphenidate, from three small unblinded trials, is the textbook signature of small-study bias.

**Publication bias detected and not addressed.** Verbatim: *"the funnel plot is relatively asymmetric, suggesting that there may be some publication bias in the results of this study."* No Egger's test, no Begg's test, no trim-and-fill — RevMan 5.4 does not perform them.

**Probable unit-of-analysis error.** 8 articles produced **14 effect estimates** in one forest plot. Multiple outcomes from the same participants (Fritz and Converse each contributed Flanker *and* DCCS; Kouhbanani contributed WCST *and* AX-CPT) appear to be treated as independent studies, which inflates precision and distorts random-effects weighting.

**Internal numerical inconsistency throughout.** Participant totals given as 373, 372, 404 and (from Table 1) 353. "Eight included studies" vs "the 11 articles." Acute/chronic split stated as 154/218 vs Table 1's 248/105. Chronic p = 0.0001 in the abstract, 0.001 in the results. A yoga CI printed as "−0.50, −0.48" — lower bound above upper bound. The Tai Chi CI printed as "−6.25, −1.8" in the abstract but "−6.25, 1.8" in the results, which changes it from significant to non-significant.

**No diagnostic criteria stated.** No DSM, ICD, or structured interview anywhere. The yoga study enrolled women *screening positive* for adult ADHD, not diagnosed.

**Medication status: not stated.** Not extracted, not stratified, not in Table 1.

**No adherence or dropout data extracted at all** — from a set where two of three chronic studies were explicitly pilot/feasibility trials whose stated purpose was assessing feasibility.

### Authors' own nulls [VERIFIED]

> *"The yoga group has the smallest effect size (SMD = 0.01, 95% CI = −0.50, −0.48, P = 0.97), the result is not significant."*

> *"The effect size of the Tai Chi group is SMD = −2.20... P = 0.25, and the results are not significant."*

> *"However, this conclusion is limited by the quantity of research evidence and still needs to be substantiated."*

> *"From the perspective of chronic exercise, randomised controlled trials are relatively rare."*

> *"Therefore, it is impossible to determine which sports offer the best improvement in inhibitory control ability for adult ADHD."*

> Conclusions: *"this conclusion remains to be validated due to the limited number of studies. In subgroup analyses, the research literature on chronic exercise and specific physical activity programmes is sparse."*

### Resolution: no conflict with Xu et al.

Both reviews looked at the **same three chronic studies**. Xu et al. said the evidence was too thin and mixed to pool. Yang et al. pooled it anyway and then conceded the same point in their Conclusions. **Xu et al.'s reading is the methodologically defensible one.**

Read carefully, this paper is additional evidence *for* the premise that the adult chronic literature is thin — and a usable example of how a sparse literature gets over-synthesised.

### One lead worth chasing

Kouhbanani et al. (2022) — the Pilates trial driving the chronic effect — had a **6-month post-intervention follow-up**, stated in its own title. **Yang et al. did not extract, pool, or discuss those follow-up data.** It is the only study in anything read so far that measured whether an effect persisted after the intervention ended, which was the original research question. [UNVERIFIED — not yet opened.]

---

## Synthesis

### What the literature actually supports

1. **Acute exercise produces a short-lived speed effect in adults with ADHD**, not a durable attention gain. Mehren: 26 ms faster on congruent trials, d=0.81, measured 7–26 min after the bout, with the ~33-min probe already negative.
2. **The one well-powered adult attention RCT is negative.** Dinu, n=159: no effect on any attention measure in ADHD.
3. **What improves is often speed, not control.** Mehren's interference score — the actual executive-function index — did not improve and numerically worsened.
4. **Chronic adult evidence is thin.** The available 12-week adult trial is a feasibility pilot with n=5 per arm at analysis, no effect sizes, and every reaction-time measure null.
5. **The children's literature is stronger but low quality.** Zhu: large pooled SMDs, but I² 79–88%, no study above 8/10 PEDro, near star-shaped network, funnel-plot eyeballing only, and no cognitive instruments identified.
6. **Digitally delivered attention training performs poorly under scrutiny.** Exergaming was the only failing modality in Zhu. Lim's BCI trial — the best-run digital trial available — yields 1.6 points on one subjective scale with no sham, no objective measure, and an effect size that grows as blinding weakens.

### The gap

> **The best-evidenced modality is the least deliverable by an app. The most app-like modality is the only one that failed.**

Open-skill activity ranks first for executive function (SUCRA 98.0%) and is defined by external pacing, which requires an opponent in physical space. Exergaming — the screen-based, gamified category — is the one intervention in Zhu's network that did not beat control.

### The second gap, which is more useful

Across the adult literature, **the binding constraint is not which exercise. It is adherence.**

- Svedell: 33% dropped out before a single session; none after starting.
- A motivated participant reported that unsupervised exercise was simply not possible.
- The authors attributed this to executive-function impairment — planning, organisation, time management — and responded by **adding an occupational therapist** to the follow-on RCT.

An app cannot supply an externally-paced opponent. An app *can* supply planning, initiation cues, scheduling, catch-up logic, and dose verification via a paired heart-rate monitor — which is precisely the scaffolding the investigators concluded was missing.

### The third gap — and this one is documented, not inferred

The question "does executive-function scaffolding improve exercise adherence in adults with ADHD?" is not a gap somebody has to argue exists. **It was formally proposed, registered, funded, and then abandoned mid-trial.**

- Svedell et al. (#4) hit 33% pre-session attrition in their pilot, diagnosed it as an executive-function problem, and wrote: *"We have, therefore, decided to add a third intervention arm to the planned RCT in which participants... will also receive cognitive intervention by an occupational therapist with the aim of improving planning, organization and time management skills."*
- The START protocol (#7) registered that arm: 40 participants, OT-led, 6 × 60 min sessions, targeting time management, planning and organisation.
- The delivered trial had **two arms.** 11 of 43 intervention participants got the cognitive training as an ad-hoc adherence fix, and were pooled into the exercise group. The authors call it *"a confounding factor... that could not be isolated in the results."*
- The same team wrote, in their own protocol: *"it has not been studied whether such training can contribute to increased physical activity or to maintaining routines for this."*

**That sentence is still true. The field opened this question and left it open.**

### Candidate research question

> Can software substitute for the executive-function scaffolding that exercise-for-ADHD trials currently supply with human staff — and what proportion of the documented adherence failure occurs at a point software could reach?

Measurable without human subjects: code every adult ADHD exercise trial for the scaffolding it provided (supervision, scheduling, group presence, make-up rules, HR verification, reminder systems, human contact hours), code each for attrition rate and attrition timing, and test whether scaffolding intensity predicts adherence independently of exercise dose.

**Note the reporting problem this will hit, and why it is itself a finding.** START pre-specified exactly these adherence metrics and published none of them. If that pattern holds across the literature, the headline result becomes: *the trials that identify adherence as the binding constraint systematically fail to report adherence data.* That is a publishable-shaped observation and it comes free with the screening work.

---

## What has NOT been verified

Do not cite any of these until opened:

- [UNVERIFIED] Meta-analysis reported as 41 studies / 7,316 participants on cognitive vs metabolic demands — Tandfonline 10.1080/1612197X.2025.2510251
- [UNVERIFIED] 16-RCT meta-analysis, school-aged children with ADHD — PMC12487183
- [UNVERIFIED] Second-order meta-analysis on near and far transfer — Collabra: Psychology 5(1), 18
- [UNVERIFIED] 2014 consensus statement signed by 70+ scientists on the brain-training industry
- [UNVERIFIED] Claim that only 1 of 24 mental-health apps cited published literature — PMC6550255
- [UNVERIFIED] Claim that fewer than 40% of scientifically-marketed brain-training programs were peer-reviewed
- [PARTIAL] Xu, Zhao & Hu (2026) — abstract, Highlights and Introduction read verbatim; **Results, statistics and Limitations are behind a paywall.** Everything cited from it above is from an accessible section. Try institutional access through the CSUDH library before citing further.
- ~~[UNVERIFIED] Journal of Global Health 2025;15:04025~~ — **RESOLVED 2026-10-02. Read in full; see section 8 above.** The −1.77 figure is real but rests on three studies (105 participants), one null and one non-significant. It does not overturn Xu et al.
- [UNVERIFIED] **Kouhbanani, Zarenezhad & Arabi (2022)** — "Mind-body exercise affects attention switching and sustained attention in female adults with ADHD: a randomized, controlled trial **with 6-month follow-up**." **High priority.** The single trial driving Yang et al.'s chronic effect, and the only study located with post-intervention follow-up data. Yang et al. did not extract that follow-up.
- [UNVERIFIED] Fritz & O'Connor (2016) — 20 min cycling, no improvement in attention or hyperactivity vs seated rest. Cited as a null by Xu et al.
- [UNVERIFIED] Converse et al. (2020) — Tai Chi feasibility trial in college students, no significant effects on cognition or ADHD symptoms.

## Gaps in the evidence base itself

1. **No pooled evidence exists for chronic exercise improving EF or attention in adults with ADHD.** Xu et al. (2026) could not meta-analyse it — too few studies, mostly feasibility pilots, mixed results.
2. **No study located measures durable attention improvement in adults.** Acute studies measure a ~7–26 minute window. START measured symptoms at 12 weeks by unblinded self-report, and its planned 6- and 12-month follow-ups are unpublished.
3. **No study located tests unsupervised or app-delivered exercise against supervised delivery.**
4. **No study has isolated the adherence-scaffolding component** — the one trial that tried abandoned the arm.
5. **Adherence data is systematically missing.** START pre-specified attendance percentages, HR-monitor minutes and home-session logs, and published none.
6. **Objective cognitive outcomes are collected and not reported.** START pre-specified AX-CPT, Go/No-Go, fMRI and ATMS-S; none appear in either results paper.
7. **Zhu's meta-analysis does not name its own cognitive instruments**, so the construct measured across 44 studies cannot be audited from the published paper.
