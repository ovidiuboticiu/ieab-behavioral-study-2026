# IEAB v1.0.0 — final experimental research release

**Technical report and reproducibility corpus — 2026**

Human author and experiment operator: **Ovidiu Boticiu**, Independent Researcher, Romania.

This release fixes the publicly available descriptive research package for Independent Evidence Aggregation Boundary (IEAB), covering v0.4.3 (exploratory) and v0.4.4 (prospectively fixed operational predictions in Git).

## Included

- The approved final 19-page Romanian report: `paper/IEAB_Raport_Stiintific_Final.pdf` and its Markdown source.
- Five original JSONL result exports with 360 valid entries per selected configuration (1,800 responses in total).
- Experimental stimuli, fixed schedule and assignments, normative design and preregistration documents.
- Python execution reference and deterministic P1–P5 analyzer.
- Independent AI-assisted Codex audit and numerical recalculation; this is **not human peer review**.
- Human authorship, substantial AI-assistance disclosure, provenance, reproduction instructions, SHA-256 manifest and explicit dual licenses (CC BY 4.0 for research content/data; MIT for Python code).

## Research timeline and status

The original IEAB repository was created on **6 October 2026**, after research work begun approximately on 5 October. The original execution infrastructure was closed on **31 October 2026** after the human operator identified disproportionate operational and audit complexity; the same scientific core continued in `ieab-restart`. Behavioral collection began on **2 November 2026**.

The research is **experimentally closed**. No reruns or new model calls are part of this release. This is a descriptive technical report, not a peer-reviewed article, a validation of internal mechanisms or a generalizable claim about all language models.

## Key observation

The examined model configurations did not show uniform improvement in normative reliability decisions and sensitivity to explicitly copied observations. For Gemma 4 12B, 85/96 copied-evidence pairs showed a normative switch, but its CORE choices agreed with counting in 45/48 cases where counting contradicted the probabilistic norm. Conclusions are restricted to the specified stimuli and selected runs.

## Reproduction and citation

See `REPRODUCERE.md`, `SHA256SUMS.txt` and `CITATION.cff`. GitHub offers a download of the source archive at the pinned `v1.0.0` tag once the Release is published.

No DOI has been registered. The report's citation is provided in `CITATION.cff`.

**Release intent:** freeze the public descriptive evidence package for archival reference. No change to original experimental data or frozen design.
