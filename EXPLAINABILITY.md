# Explainability, Auditability & Decision Logic: GitQuizGenerator

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitQuizGenerator**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitQuizGenerator** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Academic**: Academic course syllabus learning outcomes and textbook reading excerpts.
- **Bloom's**: Bloom's Revised Taxonomy cognitive framework descriptors.
- **Flesch-Kincaid**: Flesch-Kincaid readability standards for target educational grade bands.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **tag_blooms_taxonomy**: Uses `blooms-taxonomy-tagger` to calculate categorizes question prompt into bloom's revised taxonomy cognitive dimensions.
   - **evaluate_distractor_quality**: Uses `distractor-quality-evaluator` to calculate verifies that multiple choice distractors are grammatically parallel and plausible.
   - **standardize_rubric_scale**: Uses `rubric-scale-standardizer` to calculate generates 4-tier rubric grading criteria scale for assignment evaluation.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When assessment items are generated, the agent runs blooms_taxonomy_tagger, distractor_quality_evaluator, and rubric_scale_standardizer. If cognitive depth is balanced and distractors are high-quality, it issues APPROVED. If distractors require linguistic polish, it issues NEEDS_REVIEW. If items contain factual errors or trivial recall bias on advanced topics, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on pedagogical taxonomies.
- **Does**: Does not auto-grade subjective open-ended essays without human instructor moderation.
- **Complies**: Complies with universal design for learning (UDL) accessibility guidelines.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
