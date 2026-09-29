# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitQuizGenerator** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitQuizGenerator Automation Engine`
* **Responsibilities**:
  * Drafts assessment questions, formulates plausible distractors, and establishes grading criteria.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitQuizGenerator Verification & Policy Enforcer`
* **Responsibilities**:
  * Evaluates readability grade levels and verifies question alignment with syllabus learning objectives.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Curriculum Director / Department Academic Chair (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
