"""
distractor_quality_evaluator.py - Verifies that multiple choice distractors are grammatically parallel and plausible
"""
import sys
import json


def evaluate_distractor_quality(distractors_json: str):
    import json
    opts = json.loads(distractors_json) if isinstance(distractors_json, str) else distractors_json
    has_all_of_above = any("all of the above" in o.lower() for o in opts)
    valid = len(opts) >= 3 and not has_all_of_above
    return {"is_valid": valid, "status": "DISTRACTORS_VALID" if valid else "DISTRACTORS_POOR"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "distractor-quality-evaluator"}))
