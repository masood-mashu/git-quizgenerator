"""
blooms_taxonomy_tagger.py - Categorizes question prompt into Bloom's Revised Taxonomy cognitive dimensions
"""
import sys
import json


def tag_blooms_taxonomy(question_text: str):
    lower = question_text.lower()
    if any(k in lower for k in ["create", "design", "formulate"]):
        dim = "CREATING"
    elif any(k in lower for k in ["analyze", "compare", "differentiate"]):
        dim = "ANALYZING"
    elif any(k in lower for k in ["apply", "solve", "execute"]):
        dim = "APPLYING"
    else:
        dim = "UNDERSTANDING"
    return {"blooms_dimension": dim, "status": "BLOOMS_VERIFIED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "blooms-taxonomy-tagger"}))
