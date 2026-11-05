# IEAB — Independent Evidence Aggregation Boundary
## DESIGN_IEAB_v0.4.2 — PROSPECTIVE AMENDMENT (DRAFT)

**Status:** NOT FROZEN · NOT PREREGISTERED · NO BEHAVIORAL DATA · NO MODEL SEND AUTHORIZED  
**Date:** 2026-11-01  
**Base document:** `research/DESIGN_IEAB_v0.4.1.md` (Git blob `2d320a2b99d52e0781452797f28b4b7b77291278`), preserved byte-for-byte.  
**Change authority:** the operator explicitly approved the proportional error-handling policy in IEAB Restart before any behavioral data collection.

### 1. Scope and precedence

This document is a **prospective scientific amendment**, not a technical incident report. For candidate **IEAB v0.4.2**, read **v0.4.1 plus this amendment**. The numbered overrides below **supersede only** the named v0.4.1 clauses; all other provisions remain in force. Neither document is a frozen protocol. Before a scientific freeze, this pair must be named together in one versioned freeze manifest; no results from v0.4.1 are silently carried forward as behavioral observations.

**Unchanged:** the research purpose and claim boundary (§§1–2); the binary evidence model and normative posterior/grid (§§3–6); eight fictional items, label assignments, records, anchors, dependence controls and 360-key schedule per model (§§7–13,16); the strict JSON **response contract** (§14); three primary configurations and common-setting rules (§15); no-retry principle (§17.2, §17.4); definitions of descriptive rules B1–B7 (§§20–22); preflight and pre-collection requirements (§§24–26). No stimuli, ordering, probability, models, API settings or analysis rules are adapted after any model response.

**One substantive policy change:** a fully received, durably archived **individual response-contract failure** no longer stops the rest of that model's planned 360-key schedule when the experimental configuration and execution integrity remain sound. It is permanently invalid **for that key**, without retry. Systemic faults and uncertain sends still stop.

### 2. Overrides to §17 — state, resumption, stopping

**§17.1 — states:** retain all original durable attempt states, and add:
- `INVALID_RESPONSE_COMMITTED`: terminal disposition for one fully received, durably archived response that fails the frozen response contract but whose model, request, endpoint and critical metadata were verified.
- `UNRESOLVED_IN_FLIGHT`: a possibly sent request with no complete durable receipt. This is **not** equivalent to a returned invalid response.

Store the raw HTTP response first; classification and next-key release must occur in a durable atomic transaction. A key is attempted through the controlled transport **at most once** per version, regardless of final status. A valid choice that disagrees with normative probability is **not** a contract failure: it is a legitimate study observation.

**§17.3 — clean between-call resumption:** where the original text required all earlier results to be `RESULT_COMMITTED`, permit either `RESULT_COMMITTED` **or** `INVALID_RESPONSE_COMMITTED` as terminal for each earlier planned key, with no unresolved request, no critical integrity mismatch and unchanged approved settings. Resume at precisely the next not-yet-attempted scheduled key. Neither a valid nor an invalid finalized key is resent. Pre-send typing, missing-file and path mistakes are corrected locally; a reservation already made in the journal may be released only after safe proof that no send was possible, never by deleting/resetting the journal.

**§17.5 — individual invalid response (replaces automatic STOP):** if the entire HTTP response is preserved durably, the requested/returned model identity and other critical binding metadata are valid, the request and runtime match the approved configuration, the prompt is intact and the journal is consistent, then malformed JSON, duplicate/extra/missing choice fields, an invalid `chosen_claim` enum, trailing extra text, prohibited reasoning content or a non-`stop` finish reason are classified as an **individual response violation**. Write `INVALID_RESPONSE_COMMITTED` plus exact cause, release the gate atomically, and continue with the next scheduled key **without resending** the invalid key.

This classification is **not available** if the invalid response reveals or plausibly indicates a **systemic** defect. Wrong/unverified model identity, altered/truncated stimulus, incompatible or changed critical parameters/schema mechanism, corrupted journal/receipt, or other substantive departures from the prospective protocol cause STOP for the affected collection, with raw evidence preserved. A non-`stop` finish reason caused by a demonstrated global output-budget/configuration failure is systemic, not automatically an individual anomaly. No unplanned numerical threshold for recurrent malformed responses is introduced; recurrent anomalies are recorded and evaluated for concrete systemic evidence, without changing prompts or settings mid-collection.

**§17.2 and §17.4 — uncertain send unchanged:** after `REQUEST_SENT` / `SEND_POSSIBLE`, a timeout/crash without a durable complete response remains `UNRESOLVED_IN_FLIGHT`, gates the shared endpoint, and blocks further sends until an authorized prospective disposition. No retry, no switching directories, model/version aliases or wiping the ledger to bypass it.

An isolated change to an auxiliary Windows component (e.g. `conhost.exe`) is **not by itself** evidence that an IEAB scientific invariant changed. Freeze criteria must bind the actual model/artifact, relevant backend and effective scientific settings, not arbitrary unrelated OS files.

### 3. Override to §17.6 — what "complete" means

Retain the original definition **complete valid map = 360/360 valid responses**, zero missing/duplicate/extra keys and passing identity/metadata checks.

Separately define:
- `SCHEDULE_EXHAUSTED_PARTIAL_COVERAGE`: all 360 scheduled keys have durable terminal dispositions, including one or more `INVALID_RESPONSE_COMMITTED`; this is **not** a complete valid behavioral map.
- `INTERRUPTED_OR_INCONCLUSIVE`: systemic integrity failure, an unresolved send or other stop prevents schedule exhaustion.
- `COMPLETE_VALID_MAP`: 360/360 valid `chosen_claim` decisions under the approved configuration.

No missing choice is imputed, no invalid key is rerun, and no partial map is relabeled as complete.

### 4. Override to §17.7 — failure class and repair

| Class | Evidence | Disposition |
| --- | --- | --- |
| **A: pre-send local/operator error** | command, path, model not loaded or missing auxiliary dependency, and no possible send | Correct locally with safe journal reconciliation if needed; no global audit or model-data invalidation |
| **B: individual returned invalid response** | full durable response, valid critical binding, intact configuration | Record invalid for this key, continue next key, never retry |
| **C: systemic scientific/data-integrity error** | wrong model or critical settings, corrupted prompt/request/response binding or ledger, or equivalent demonstrated risk | STOP affected collection; preserve and delimit records; no unapproved settings changes |
| **D: uncertain post-send outcome** | a send may have occurred, but no durable complete receipt | Block the shared endpoint domain; do not retry or route around the block |

Existing prospective repair/versioning controls for a systemic or infrastructure failure remain in force: disclosure of invalid attempts, new version/freeze for any approved restart, same common settings for primary comparisons, no inspection of choices to decide repairs. Class B is **not** repaired to obtain a different decision, and by itself does not imply terminating the configuration. No arbitrary post-hoc error-rate threshold.

### 5. Override to §18 — reporting of each configuration

For **every** planned model configuration, report `360 planned`, `attempted`, `durably finalized`, `valid decisions`, `individual invalid responses` (by cause), `unattempted` and `unresolved`, plus whether it is `COMPLETE_VALID_MAP`, `SCHEDULE_EXHAUSTED_PARTIAL_COVERAGE` or `INTERRUPTED_OR_INCONCLUSIVE`. Supply coverage and denominators by CORE, DEPENDENT, A1 and A2, and references to raw evidence for invalid/uncertain attempts.

An incomplete map cannot be compared, ranked or summarized as if it were a 360/360 map. No missing decisions are treated as agreement, disagreement or zero.

### 6. Override to §19 — M1–M6 with partial coverage

The original measurements **retain their mathematical definitions** wherever their required choices exist. When invalid choices make measurements unavailable:

| Measure | Eligible data and denominator |
| --- | --- |
| **M1** normative-choice agreement | Valid decisions only. Report **both planned and valid** denominators for CORE (240), DEPENDENT (96), A1 (8), A2 (16), every subgroup and pooled results when labeled; report invalid/unobserved counts. DEPENDENT agreement is accompanied by M6 as originally required. |
| **M2** monotonicity | Only five-key sequences with **all five valid** decisions. Report `eligible sequences / 48 planned`, and reversals out of `4 × eligible sequences` (192 only when all 48 are eligible); incomplete sequences are explicitly not evaluable. |
| **M3** switching | Only complete valid five-bit traces; record `eligible / 48`. An incomplete trace is **not** assigned a switching point. The exhaustive testing requirement for all 32 possible five-bit traces remains unchanged. |
| **M4** log-odds summary | Valid CORE choices only, grouped by the unchanged normative L. Report per-L valid/planned counts and exclusions, no imputation. |
| **M5** FIRST/LAST | Only matched CORE pairs with **both** valid answers. Report `eligible / 120 planned` and missing-pair count. Descriptive paired difference is `(FIRST_only-LAST_only)/eligible_pairs`; undefined if `eligible_pairs=0`. |
| **M6** lineage | Only matched INDEPENDENT/DEPENDENT pairs with **both** valid answers. Report `eligible / 96 planned`, missing pairs, threshold/high-margin coverage and informative subset; `eligible=0` means **not evaluable**, not no effect. |

**§§20–22 derived rule agreements:** evaluate only on valid observations; preserve the original B1–B7 predictions, TIE definitions and all prespecified rules. B4 and B6 prediction agreements sum to **the number of valid observed CORE rows**, not automatically 240 if some rows lack a valid choice. Degenerate profile comparisons require the data coverage needed for each full profile; never infer a complete profile by filling invalid outcomes.

**§23 interpretation:** all incomplete-coverage summaries are explicitly descriptive, with **planned / valid** denominators, and are not equivalent to a complete 360/360 map. Missingness can be associated with condition/model and cannot be assumed random. Do not invent a post-hoc significance test, arbitrary PASS/FAIL threshold, or favorable model comparison based on selected complete cases. No behavioral prefix is exposed to guide changes to stimuli, prompts, configurations, model choice or continuation policy.

### 7. Minimal changed implementation criterion (§25)

Preserve the prior tests and recorded passes **as historical evidence**, not as validation of this changed policy. The **single new targeted synthetic acceptance scenario** is:
1. receive an invalid raw reply, write durable receipt, finalize the invalid key atomically;
2. permit **exactly the next** planned key, without repeating the invalid key;
3. demonstrate that a mismatch in model/critical settings still stops, and an uncertain possibly-sent request still blocks.

This is the smallest necessary changed behavior. Do not rebuild stimuli, grids, tokenization results or already documented LM Studio presets merely because of this amendment. A final executable package still requires the existing, proportionate pre-freeze conditions (§§24–26), with no new auditor cycle added solely by this text.

### 8. Decision (§28)

**GO FOR TARGETED SYNTHETIC IMPLEMENTATION DRAFT OF THIS AMENDMENT ONLY.**

This is *not* a design freeze, preregistration, a new generation preflight approval or a behavioral-run authorization. In particular, no live sender/LM Studio model request is authorized by this document. When ready, the freeze will prospectively identify **both** base v0.4.1 and amendment v0.4.2, plus exact runnable artifact hashes, before any behavioral collection.
