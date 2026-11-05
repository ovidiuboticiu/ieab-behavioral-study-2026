# IEAB — Independent Evidence Aggregation Boundary
## DESIGN_IEAB_v0.4.1

**Status: REVISED DESIGN DRAFT — NOT FROZEN — NOT PREREGISTERED — NO DATA COLLECTION AUTHORIZED**

This clarification revision preserves the scientific structure of DESIGN_IEAB_v0.4 and prospectively
incorporates the accepted Claude/Codex v0.4 delta-review findings recorded in
`external_audit/delta_v0.4/EXTERNAL_DELTA_REVIEW_RECONCILIATION_v0.4.md`.

No IEAB behavioral data have been collected. DESIGN_IEAB_v0.4 remains preserved as the externally
reviewed predecessor.

---

## 1. Research purpose

IEAB is a descriptive behavioral instrument-characterization study motivated by the IAER program.

Primary question:

> On these eight frozen fictional items, under an explicitly stated binary evidence model, what
> realized finite-grid choice patterns appear as multiple independent sources of known reliability
> accumulate?

Secondary questions:

1. Is the realized choice trace monotonic as same-direction independent evidence increases?
2. Where do realized finite-grid switches occur relative to the normative switching positions?
3. How do exactly matched FIRST/LAST evidence-order presentations differ?
4. How do matched INDEPENDENT/DEPENDENT prompts differ when lineage is represented explicitly?
5. Which prespecified descriptive rules agree with the realized choices on the cells where those
   rules make distinct predictions?

IEAB does **not** test IAER itself.

---

## 2. Claim boundary

IEAB v0.4 may support claims only about:

- these 8 frozen fictional items;
- the finite frozen prompt set generated from them;
- the exact pinned model configurations;
- one frozen realized run per configuration.

It may describe:

- normative-choice agreement;
- realized n=1..5 choice traces;
- finite-grid switching patterns;
- nonmonotonic reversals;
- exactly matched evidence-order differences;
- local responsiveness to explicit lineage fields;
- descriptive prediction agreement with prespecified behavioral rules.

It does **not** establish:

- internal Bayesian or log-odds computation;
- a unique internal heuristic;
- arithmetic versus attention versus integration mechanism;
- general dependence competence;
- stable response probabilities or repeatability across reruns;
- a continuous boundary outside the tested grid;
- generalization beyond these eight items;
- pure model-family, architecture, parameter-count, or training effects;
- IAER replication, non-replication, eligibility, or effect size.

The study is a purposive **model-configuration comparison**.

---

## 3. Formal generative semantics

For every behavioral prompt there are exactly two mutually exclusive and exhaustive hypotheses:

`CLAIM_A` and `CLAIM_B`.

Prior probabilities are equal:

```
P(CLAIM_A) = P(CLAIM_B) = 0.5
```

### 3.1 Independent observation source

An observation source with reliability `r` is symmetric:

```
P(report = true claim | either claim is true) = r
P(report = false claim | either claim is true) = 1-r
```

Conditional on the true claim, distinct sources that make their own observations are independent.

### 3.2 Copied report

A copied report does not arise from a new observation of the hidden truth. It reproduces the
`reported_claim` of a specified originating record.

Copy lineage is factual task information. The prompt must not say that a copy:

- "adds no evidence";
- "should be ignored";
- "counts once";
- "should be discounted";

or otherwise state the normative consequence.

### 3.3 Analysis-only terminology

The following terms are analysis-only and must not appear as labels for the two claims in
model-facing prompts:

- repeated side;
- single-0.80 side;
- expected;
- correct;
- baseline;
- counter.

---

## 4. Verbatim model-facing semantic statement

The following text is part of the common frozen prompt and must be presented verbatim, apart from
mechanical insertion of the two claim texts and evidence records:

> Exactly one of CLAIM_A and CLAIM_B is true. Before considering the evidence records, each claim
> has probability 0.5. A record with made_own_observation = YES comes from an observation source
> that made its own observation. If that record's originating_observation_reliability is r, the
> source reports the true claim with probability r and the false claim with probability 1-r,
> symmetrically whichever claim is true. Conditional on the true claim, distinct observation
> sources that made their own observations are independent. A record with
> made_own_observation = NO did not make a new observation; its reported_claim was copied from the
> record named in copied_from_record. Only the evidence model and evidence records stated in this
> prompt should be used to judge which claim is more likely. Return only the required structured
> choice.

This wording makes IEAB an explicit probability/evidence-model application task. It does not claim
to measure spontaneous discovery of the probability model.

---

## 5. Core normative model

For a core INDEPENDENT trajectory:

- one side receives `n` mutually independent observations, each reliability `r`;
- the opposite side receives one independent observation of reliability `c=.80`.

With prior odds 1:1:

```
O_repeated = (r/(1-r))^n * ((1-c)/c)
```

with `c=.80`.

The normative choice is:

- repeated-source side if `O_repeated > 1`;
- single-.80 side if `O_repeated < 1`.

No planned core cell is tied.

For DEPENDENT matched trajectories, copied reports have no new random observation in the stated
generative model. The analysis therefore uses only the unique originating observations.

---

## 6. Core grid

The core grid remains:

- `r ∈ {.60, .65, .70}`;
- `n ∈ {1,2,3,4,5}`;
- opposing single source `c=.80`;
- evidence order `COUNTER_FIRST` or `COUNTER_LAST`.

### 6.1 Normative posterior table

| r | n | P(repeated side) | Normative choice |
|---:|---:|---:|---|
| .60 | 1 | .2727 | single-.80 |
| .60 | 2 | .3600 | single-.80 |
| .60 | 3 | .4576 | single-.80 |
| .60 | 4 | .5586 | repeated |
| .60 | 5 | .6550 | repeated |
| .65 | 1 | .3171 | single-.80 |
| .65 | 2 | .4630 | single-.80 |
| .65 | 3 | .6156 | repeated |
| .65 | 4 | .7484 | repeated |
| .65 | 5 | .8467 | repeated |
| .70 | 1 | .3684 | single-.80 |
| .70 | 2 | .5765 | repeated |
| .70 | 3 | .7605 | repeated |
| .70 | 4 | .8811 | repeated |
| .70 | 5 | .9453 | repeated |

Normative finite-grid switch positions:

- r=.60 -> n=4
- r=.65 -> n=3
- r=.70 -> n=2

The design does not interpret agreement with these positions as uniquely Bayesian because B7 below
shares the same non-tied switching positions on this grid.

---

## 7. Base items, claim text, labels, and assignment balancing

Use exactly **8 new fictional base items**.

Each item contains two neutral competing claim texts:

- `TEXT_X`
- `TEXT_Y`

The mapping from content text to `CLAIM_A/CLAIM_B` is a separately frozen factor.

### 7.1 Assignment factors

For each `base_item × r` unit, freeze three binary factors:

1. **content-label mapping**
   - X_TO_A
   - X_TO_B
2. **repeated-side label**
   - CLAIM_A
   - CLAIM_B
3. **claim-presentation order**
   - A_FIRST
   - B_FIRST

There are 8 possible three-factor combinations.

Within each r stratum, the 8 base items must receive all 8 combinations exactly once.

Across the three r values, every base item must receive:

- both content-label mappings at least once;
- both repeated-side labels at least once;
- both claim-presentation orders at least once;
- TEXT_X on the repeated side at least once;
- TEXT_Y on the repeated side at least once.

The exact allocation is generated before any behavioral call and must be machine-checked.

### 7.2 Mirroring rule

For a fixed `base_item × r`, the three-factor assignment is identical across:

- all n=1..5;
- COUNTER_FIRST and COUNTER_LAST;
- matched DEPENDENT controls.

Thus evidence-order pairs differ only in record position.

### 7.3 Interpretation limit

Even with this balancing, item, r, and assignment factors are not a fully crossed inferential
population design.

Label/order summaries are finite-grid descriptive compositions, not estimates of population-level
label or order effects.

---

## 8. Neutral identifiers and nested record invariants

### 8.1 Opaque IDs

All `record_id` and `observation_source_id` values must be opaque non-ordinal tokens.

They must not encode:

- position;
- reliability;
- claim label;
- item number;
- expected answer;
- dependence condition.

Sequential patterns such as R1/R2/R3 or S1/S2/S3 are forbidden.

IDs are allocated before outcomes and frozen.

The ID generator uses fixed-length 8-character tokens drawn only from the frozen alphabet:

```
k m n p r t v x z
```

No digits, separators, ordinal prefixes, claim letters A/B, reliability strings, or semantic words
are permitted. The checker must also reject any generated ID that appears as a substring of either
claim text for its item.

### 8.2 n-prefix nesting

For each fixed:

```
base_item × r
```

construct one canonical five-record repeated-side sequence plus the single .80 record.

The same canonical record objects are reused across both evidence orders and all n values. The
base_item × r assignment factors are already frozen by section 7.1 and therefore do not define a
second record sequence.

The n=k+1 prompt must preserve byte/field identity of:

- the single .80 record;
- all k repeated-side records already present;

and add exactly one new repeated-side observation record.

The new record is appended at the **end of the repeated-side block**.

Within-block repeated-side record order remains fixed.

A checker must verify normalized record diffs for every adjacent n pair.

### 8.3 Evidence-order matching

COUNTER_FIRST and COUNTER_LAST contain the exact same record objects.

Only the position of the single .80 record relative to the repeated-side block changes.

Record and source identifiers do not change with presentation position.

---

## 9. Evidence-record schema

Every evidence record uses:

```
record_id
observation_source_id
originating_observation_reliability
copied_from_record
made_own_observation
reported_claim
```

Independent record:

```
copied_from_record = NONE
made_own_observation = YES
```

Copied record:

```
copied_from_record = <opaque record_id>
made_own_observation = NO
```

For an independent record, `originating_observation_reliability` belongs to its own observation
source.

For a copied record, it is the reliability of the ultimate originating observation source.

### 9.1 Frozen copy topology

DEPENDENT repeated-side records use a **star topology**:

- the root is the first canonical repeated-side record (the record already present at n=1);
- the root keeps its canonical record_id and observation_source_id and made_own_observation=YES;
- every additional copied record preserves the record_id of its matched INDEPENDENT counterpart;
- every copy sets observation_source_id to the root's observation_source_id;
- every copy sets copied_from_record to the root's record_id;
- every copy sets made_own_observation=NO;
- no copy makes its own observation.

All copied records reproduce the root's `reported_claim`.

The lineage checker must verify:

- exactly one repeated-side root;
- every copy points to that root;
- no cycles;
- no orphan references;
- reported claims agree with the root;
- no copied record is assigned a new observation source.

---

## 10. Minimal anchor block

Anchors are non-core descriptive sanity checks. They do not create an eligibility gate.

### A1 — single-source reading sanity

Per base item:

- exactly one independent record;
- reliability .80;
- no opposing evidence record;
- normative choice = that record's reported claim.

Use 8 trajectories: one per base item.

Across the 8 anchor trajectories, content-label mapping, supported label, and claim-presentation
order are exactly balanced across their 8 possible combinations.

### A2 — strongest-side sanity

Per base item:

- one independent record on one side, reliability .90;
- one independent opposing record, reliability .80;
- both evidence orders;
- normative choice = .90 side.

Use:

```
8 items × 2 evidence orders = 16 trajectories
```

Across the 8 A2 base-item assignments, content-label mapping, .90-supported label, and
claim-presentation order must cover all 8 three-factor combinations exactly once.

The A2 assignment is frozen and mirrored across both evidence orders.

### 10.1 Anchor interpretation

Anchors are reported before the core map.

No post-hoc PASS/FAIL threshold is defined.

If anchor errors occur, they must be reported and any interpretation that specifically attributes
core errors to multi-source aggregation is prohibited.

Anchors diagnose whether simpler reading/label/strongest-side behavior also showed errors.

---

## 11. Explicit-lineage dependence block

The dependence block measures local responsiveness to explicit lineage fields. It does **not**
establish general dependence competence or internal provenance understanding.

### 11.1 Threshold cells

Retain the original threshold cells:

- r=.60, n=4
- r=.65, n=3
- r=.70, n=2

### 11.2 Higher-margin cells

Add:

- r=.60, n=5
- r=.65, n=5
- r=.70, n=5

For every dependence cell, item, and evidence order compare:

- existing INDEPENDENT core trajectory;
- additional DEPENDENT matched trajectory.

There are 6 dependence cell types.

Additional DEPENDENT trajectories:

```
6 cells × 8 items × 2 evidence orders = 96
```

### 11.3 Exact pair matching

Matched INDEPENDENT/DEPENDENT prompts must share:

- base item;
- content-label mapping;
- repeated-side label;
- claim-presentation order;
- r;
- n;
- single-.80 record;
- evidence order;
- response schema;
- field names;
- total record count.

Prespecified differences are limited to the lineage/source-origin values required to encode
distinct independent roots versus copied records. For non-root repeated records, record_id,
originating_observation_reliability, and reported_claim are preserved from the matched INDEPENDENT
record; observation_source_id, copied_from_record, and made_own_observation change exactly as
specified in section 9.1.

Prompt character, word, and tokenizer-specific token-count differences are archived for each pair.

### 11.4 Informative-pair reporting

For M6 report:

1. all matched pairs;
2. the subset where the INDEPENDENT member chose the repeated side.

If the informative subset is empty, lineage responsiveness for that configuration is reported as
**not evaluable from informative pairs**.

No arbitrary minimum-k threshold is imposed.

---

## 12. Planned trajectory counts

### Core

```
8 × 3 r × 5 n × 2 evidence orders = 240
```

### Additional DEPENDENT

```
6 dependence cells × 8 × 2 orders = 96
```

### Anchors

```
A1 = 8
A2 = 16
anchors total = 24
```

### Total per model configuration

```
240 + 96 + 24 = 360
```

Across three complete primary configurations:

```
1080 behavioral trajectories
```

All 360 keys are generated and frozen before the first model call.

---

## 13. Prompt-length and record-count scope

In the core grid, n, record count, prompt length, and cumulative independent evidence necessarily
covary.

v0.4 does not claim to isolate these factors.

Requirements:

- rigid fixed-field record templates;
- constant non-evidence instructions;
- no neutral filler solely to equalize length;
- record rendered character count;
- record word count;
- record model-specific prompt token count where available.

The DEPENDENT contrast is count-matched but still differs in lineage-field values and tokenization.

---

## 14. Response contract and strict parsing

The only accepted model response is one JSON object containing exactly:

```json
{"chosen_claim":"CLAIM_A"}
```

or:

```json
{"chosen_claim":"CLAIM_B"}
```

No rationale.
No confidence.
No additional fields.

Parser policy:

- surrounding whitespace: allowed;
- exactly one JSON object: required;
- duplicate keys: invalid;
- extra keys: invalid;
- missing key: invalid;
- multiple JSON objects: invalid;
- trailing non-whitespace text: invalid;
- chosen_claim outside the two allowed enums: invalid;
- forbidden reasoning/reasoning_content under reasoning-OFF policy: invalid.
- valid JSON Unicode escapes are accepted only when they decode exactly to the required key and one of the two allowed enum values.

The same structured-output enforcement mechanism must be used for all three primary configurations.

---

## 15. Primary model configurations and permitted execution differences

Planned primary configurations:

1. IEAB-Qwen3.5-4B
2. IEAB-Gemma-4-E4B
3. IEAB-Ministral-3-8B-Instruct-2512

The Qwen candidate is a newly pinned configuration motivated by IAER v0.4.3, not a
cryptographically verified rerun of the exact historical artifact.

### 15.1 Must be common across primary configurations

Unless a candidate is withdrawn before collection:

- LM Studio/runtime build;
- endpoint protocol;
- context limit;
- temperature = 0;
- seed = 42 where the backend honors it;
- reasoning/thinking = OFF;
- structured-output JSON schema enforcement;
- response schema;
- maximum output-token budget;
- timeout policy;
- retry policy;
- stop policy;
- 360-key schedule;
- prompt semantics and templates;
- analysis code.

### 15.2 Inherently model-specific and permitted

- API model identifier;
- model filename;
- model SHA-256;
- quantization/artifact;
- tokenizer;
- model-native chat template.

Every model environment sheet must record all effective settings.

Any additional model-specific difference discovered before collection requires explicit prospective
disposition. After collection begins, no new exception may be introduced into the common design.

Primary interpretation is configuration-specific and cannot attribute differences uniquely to
weights or model family.

---

## 16. Execution schedule

Before collection:

- generate exactly 360 planned keys;
- verify uniqueness and factorial counts;
- apply one frozen deterministic pseudorandom permutation;
- freeze the ordered key list.

Use the same ordered key list for all primary model configurations.

Collection:

- sequential only;
- fresh context every trajectory;
- no regrouping by condition;
- no adaptive prompt change;
- no behavioral outcome printed to the operator during collection.

Only technical progress and failure-class information may be shown live.

---

## 17. Durable runner state and stopping rules

### 17.1 Attempt state machine

Every call has a unique `attempt_id`.

Durable ledger states must distinguish at least:

- PLANNED;
- REQUEST_PREPARED;
- REQUEST_SENT;
- RESPONSE_RECEIVED;
- RESULT_COMMITTED;
- TERMINAL_FAILURE.

State transitions are append-only and flushed durably.

A response received but not durably committed must never be silently treated as a proven
no-decision transport failure.

### 17.2 Transport retry

**Prospective implementation clarification adopted 2026-10-08: zero retries in the same frozen
v0.4.1 run/version.**

Any transport exception after `REQUEST_SENT` terminates the model run. If the runner cannot prove
that no model decision occurred, classify the attempt as:

`INVALID/INCONCLUSIVE FOR BEHAVIORAL MAP — UNRESOLVED IN-FLIGHT CALL`

No key is retried in the same version. A technical repair, if later justified under section 17.7,
requires a new version/freeze and restart from key 1.

This conservative clarification supersedes the earlier one-retry wording and removes the need to
infer whether a remote decision was returned. It is prospective: no IEAB behavioral data exist.

### 17.3 Clean between-call resumption

If a run is interrupted with all earlier results durably committed, no unresolved REQUEST_SENT
attempt, and no terminal failure, the same frozen version may resume at the exact next uncommitted
planned key under unchanged settings.

No completed key is rerun.

### 17.4 Unknown in-flight outcome

If interruption occurs after REQUEST_SENT and the runner cannot prove that no response was returned:

`INVALID/INCONCLUSIVE FOR BEHAVIORAL MAP — UNRESOLVED IN-FLIGHT CALL`

No rerun of that key is allowed in the same version.

### 17.5 Returned invalid response

Malformed output, schema violation, forbidden extra content, non-stop finish reason, forbidden
reasoning content, or frozen-metadata mismatch:

- raw content preserved;
- terminal failure written;
- decision not rerun;
- model run stops.

### 17.6 Technical completeness

A configuration is complete only with:

- 360/360 valid planned rows;
- zero terminal failure rows;
- zero missing keys;
- zero extra keys;
- zero duplicate valid keys;
- all metadata checks passing.

Otherwise it is INVALID/INCONCLUSIVE FOR BEHAVIORAL MAP.

### 17.7 Post-invalid disposition

Every invalid attempt remains permanently reported.

The repair policy is frozen by failure class before collection.

**Transport/infrastructure failure only:** one repair attempt may be proposed if the failure can be
corrected without changing scientific semantics. The proposal must be made without inspecting
behavioral prefix choices.

**Returned response-contract failure:** no technical repair/rerun is permitted merely to obtain a
complete primary map under that interface. The configuration remains incomplete/invalid. Any later
scientifically revised interface is a new design.

Any permitted repair attempt requires:

- a new version identifier;
- a new prospective freeze before rerun;
- disclosure of the prior invalid attempt;
- the complete schedule restarted from key 1;
- an explicit statement of the failure-causing technical parameter being changed.

If a permitted repair changes any section-15.1 setting that is designated common across primary
configurations, then either:

- all primary configurations are rerun from key 1 under the same new common setting and new
  version/freeze; or
- the repaired configuration is classified **NON-COMMON** and excluded from the primary
  cross-configuration comparison.

If the repair changes scientific semantics, stimuli, evidence structure, scoring, or analysis rather
than only a documented technical execution/interface parameter, it is a new scientific design
version and must receive design review before execution.

Before deciding whether to make a technical repair, behavioral choices from the invalid prefix must
not be inspected.

The runner therefore suppresses behavioral outputs during collection and preserves them in the
append-only result artifact. After the repair/no-repair decision is frozen, the invalid prefix may
be opened for audit reporting.

Behavioral prefixes from invalid attempts must never be used to tune prompts, stimuli, scoring, or
model selection.

---

## 18. Completion disposition table

Every planned primary configuration must appear in the final study disposition, including invalid
ones.

For each configuration report:

- complete/incomplete status;
- completed-key count;
- first terminal key if any;
- failure class;
- transport/configuration vs response-contract failure;
- finish metadata;
- raw failure artifact reference.

Incomplete prefixes are audit trails only.

They must not be ranked against complete behavioral maps and must not have missing choices imputed.

---

## 19. Descriptive measurements

No row-independent p-values, confidence intervals, or conventional independent-row significance
tests are used.

### M1 — normative-choice agreement

Report separately:

- core: denominator 240;
- additional DEPENDENT: denominator 96;
- A1 single-source anchor: denominator 8;
- A2 strongest-side anchor: denominator 16, also reported by evidence order (8/8);
- anchors pooled: denominator 24, only as a secondary composition-weighted summary;
- pooled total only if explicitly labeled as a composition-weighted summary.

Additional DEPENDENT normative agreement is never interpreted in isolation; it is reported only
alongside the matched M6 outcome categories.

Every rate must display its denominator.

### M2 — within-sequence monotonicity

For each:

```
base_item × r × evidence_order
```

encode:

- 1 = repeated-side choice;
- 0 = single-.80 choice.

There are 48 five-bit core traces.

Report:

- each complete five-bit trace;
- total adjacent 1->0 reversals out of 192;
- number of sequences with at least one reversal.

### M3 — finite-grid switch summaries

For every five-bit trace:

- `first_switch`: first n with value 1, if any;
- `stable_within_grid_switch`: the inclusive value
  `min{k in 1..5 : x_j = 1 for every j = k..5}`, if that set is non-empty;
- `NO_STABLE_WITHIN_GRID_SWITCH` if absent;
- reversal count;
- `terminal_only_switch = YES` **iff** `stable_within_grid_switch == 5` (earlier transient 1 values do not change this definition).

All 32 possible five-bit traces and their scorer outputs must be exhaustively unit-tested before
freeze. Mandatory edge cases include:

- 00000 -> no stable switch;
- 10100 -> no stable switch;
- 00001 -> stable_within_grid_switch=5;
- 10101 -> stable_within_grid_switch=5;
- 11111 -> stable_within_grid_switch=1.

A switch at n=5 is stable only within the observed grid and does not imply persistence beyond n=5.

### M4 — normative log-odds summary

For every core row:

```
L = n*log(r/(1-r)) + log(.20/.80)
```

Report chosen-repeated rate by unique L and complete item-level traces.

A logistic curve is **omitted from the primary analysis** to avoid discretionary separation handling.
If desired later, it may appear only as explicitly post-primary exploratory analysis.

### M5 — evidence-order matched differences

Across 120 matched core pairs report:

- identical choice count;
- FIRST-only repeated count;
- LAST-only repeated count;
- descriptive paired risk difference:
  `(FIRST_only - LAST_only)/120`.

No inferential p-value.

Order effects are observed matched differences in one realized run; repeatability is unmeasured.

### M6 — explicit-lineage matched differences

Across 96 matched INDEPENDENT/DEPENDENT pairs classify:

- normative-direction switch:
  INDEPENDENT repeated, DEPENDENT single-.80;
- reverse-direction switch;
- same repeated;
- same single-.80.

Report separately:

- threshold-cell pairs;
- high-margin pairs;
- all pairs;
- informative subset where INDEPENDENT chose repeated.

M6 measures local responsiveness to the explicit lineage manipulation, not general dependence
competence.

---

## 20. Prespecified individual-trajectory rules

Rules predict the repeated side (1), single-.80 side (0), or where specified TIE.

### B1 — normative log-odds rule

Predict sign of L.

### B2 — strongest-single-source rule

Predict single-.80 side for every core cell.

### B3 — statement-count rule with n=1 strongest-source tie-break

- n=1 -> single-.80 side;
- n>=2 -> repeated side.

### B4 — recency rule

- COUNTER_FIRST -> repeated;
- COUNTER_LAST -> single-.80.

### B6 — primacy rule

- COUNTER_FIRST -> single-.80;
- COUNTER_LAST -> repeated.

### B7 — linear-excess rule

Compute with **exact decimal/rational arithmetic**, never binary floating-point thresholding:

```
D = n*(r-.5) - (.80-.5)
```

- D>0 -> repeated;
- D<0 -> single-.80;
- D=0 -> TIE / no directional prediction.

On the present core grid, B7 has exactly 32 TIE rows:
- r=.60, n=3: 16 rows;
- r=.65, n=2: 16 rows.

B7 is directional on 208 rows and agrees with B1 on all 208.

Therefore B1 agreement cannot uniquely identify log-odds aggregation over this linear alternative.
B7 prediction agreement must always report its directional coverage denominator (208), and TIE rows
must not be scored as correct or incorrect directional predictions.

---

## 21. Relational rule B5

### B5 — independence-insensitive repetition compatibility

B5 predicts only a relation:

> matched INDEPENDENT and DEPENDENT prompts tend to yield the same final choice.

Report:

- same-choice count/rate;
- different-choice count/rate;
- normative-direction switch count/rate;
- reverse-direction switch count/rate.

B5 same-choice agreement is compatibility evidence only.

It cannot affirmatively identify a repetition mechanism because many other rules can also produce
same-choice pairs.

---

## 22. Rule disagreement and degenerate-profile specification

Before collection, automatically generate pairwise disagreement matrices for:

- B1;
- B2;
- B3;
- B4;
- B6;
- B7 where B7 is directional.

For each pair report:

- comparable rows;
- agreement rows;
- disagreement rows;
- exact diagnostic cell types.

No unique "winning mechanism" is declared.

B4 and B6 are exact complements on all 240 core rows. Their prediction agreements therefore sum to
240 and are also reported jointly as one order-preference summary together with M5.

### 22.1 Degenerate-profile table

Before collection, the analyzer must generate expected core summaries for:

- ALWAYS_SINGLE;
- ALWAYS_REPEATED;
- RECENCY;
- PRIMACY;
- FIXED_CLAIM_A;
- FIXED_CLAIM_B.

At minimum record for each profile:

- core normative agreement;
- reversal count;
- sequence-with-reversal count;
- stable-within-grid-switch distribution;
- evidence-order discordance pattern;
- rule-prediction agreements.

Observed metrics matching a degenerate profile must not be described as evidence of sophisticated
aggregation merely because they appear monotonic or order-stable.

---

## 23. Descriptive interpretation policy

v0.4 does not invent arbitrary numerical cutoffs for words such as "frequent", "persistent", or
"systematic".

Primary reporting uses exact counts, denominators, traces, switch locations, and prediction
agreements.

The report must not assign a post-hoc PASS/FAIL label to:

- cumulative evidence behavior;
- strongest-source behavior;
- statement-count behavior;
- recency;
- primacy;
- lineage responsiveness.

Narrative interpretation must be tied to the exact prespecified descriptive quantities.

---

## 24. Technical preflight

Before behavioral collection, each model/runtime receives a non-study technical preflight only.

It may verify:

- endpoint/model identity;
- structured-output enforcement;
- exact parser contract;
- context capacity;
- reasoning OFF;
- runtime metadata capture;
- timeout/transport path;
- append-only ledger behavior.

It must not use IEAB base items or generate a study outcome.

Any behavioral-looking preflight is prohibited.

---

## 25. Required implementation checks before freeze

The frozen package must include machine checks for:

1. normative posterior table and 4/3/2 switch positions;
2. 8-item content/label/order assignment balance;
3. per-item coverage of both levels of all three assignment factors across r, plus both TEXT_X and
   TEXT_Y appearing on the repeated side across r;
4. opaque/nonordinal IDs generated from the frozen alphabet and substring rejection rule;
5. canonical base_item × r record generation, n-prefix nesting, and append-at-end rule;
6. FIRST/LAST exact record identity apart from position;
7. INDEPENDENT/DEPENDENT exact matching invariants;
8. lineage star topology and acyclicity;
9. anchor counts/balance;
10. exact 360-key schedule;
11. rule disagreement matrices including exact B7 arithmetic, exactly 32 B7 TIE rows, and
    208-row B1/B7 directional coverage;
12. degenerate-profile expected outputs;
13. exhaustive 32-sequence M3 scorer tests including the five mandatory edge cases in section 19;
14. strict JSON parser edge cases;
15. durable runner state-machine fault tests, including clean between-call resume, lost response,
    and post-response/pre-commit interruption.

---

## 26. Pre-collection artifacts

Before any behavioral model call:

- `DESIGN_IEAB_v0.4.1.md`;
- internal v0.4 delta audit;
- external Claude/Codex v0.4 delta reviews and reconciliation;
- exact prompt specification containing section 4 verbatim text;
- 8-item stimulus specification;
- assignment file and checker;
- record-template specification;
- anchor specification;
- dependence-control specification;
- normative checker;
- rule/degenerate-profile checker;
- analysis specification;
- common 360-key schedule;
- schedule/integrity checker;
- strict parser tests;
- runner and runner fault tests;
- analyzer and exhaustive sequence tests;
- three model-environment sheets;
- freeze manifest with SHA-256 hashes;
- immutable pre-outcome repository commit;
- external/public timestamp commitment for the frozen package.

No behavioral collection is authorized before all artifacts pass audit.

---

## 27. Version and audit discipline

v0.3 remains preserved as the externally audited predecessor.

v0.4 remains preserved as the externally reviewed artifact. v0.4.1 is the prospective
clarification revision that incorporates the reconciled delta-review findings before implementation
freeze.

If the external delta review identifies a design blocker, create v0.5 rather than silently editing a
frozen or already-executed version.

No behavioral outcome may be used to justify a design change within the same frozen version.

---

## 28. Current decision

**GO TO IMPLEMENTATION DRAFT — CLARIFICATION REVISION NOT FROZEN.**

Prompt, stimulus, checker, schedule, runner, parser, ledger, analyzer, and environment-sheet
artifacts may now be drafted and audited against v0.4.1.

Freeze, preregistration, public pre-outcome commitment, behavioral model calls, and outcome
collection remain unauthorized until all section-25/26 artifacts pass audit.
