"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitQuizGenerator.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.blooms_taxonomy_tagger import *
from tools.distractor_quality_evaluator import *
from tools.rubric_scale_standardizer import *

class TestGitQuizGeneratorPredictability(unittest.TestCase):
    def test_blooms_taxonomy_tagger(self):
        res = tag_blooms_taxonomy("Compare and contrast relational and NoSQL databases.")
        self.assertEqual(res["blooms_dimension"], "ANALYZING")
        self.assertEqual(res["status"], "BLOOMS_VERIFIED")

    def test_distractor_quality_evaluator(self):
        res = evaluate_distractor_quality('["Index scan", "Full table scan", "Hash join"]')
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["status"], "DISTRACTORS_VALID")

    def test_rubric_scale_standardizer(self):
        res = standardize_rubric_scale("Implement an authenticated REST API")
        self.assertEqual(len(res["tiers"]), 4)
        self.assertEqual(res["status"], "RUBRIC_GENERATED")


if __name__ == "__main__":
    unittest.main()
