from unittest import TestCase
from ltr_evaluation import PAIRING_ERROR, ltrEvaluation
class TestLtrEvaluation(TestCase):
    
    def test_ltr_eval(self):
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertAlmostEqual(160.0, ltrEvaluation(expr),places=1)
        expr = "10 * (5 - 10.5e-1)"
        self.assertAlmostEqual(10 * (5 - 10.5e-1) , ltrEvaluation(expr),places=1)
        expr = "10 * (5 * 10.5e-1)"
        self.assertAlmostEqual(10 * (5 * 10.5e-1) , ltrEvaluation(expr),places=1)
        expr = "10 * (5 / 10.5e-1)"
        self.assertAlmostEqual(10 * (5 /10.5e-1) , ltrEvaluation(expr),places=1)
        expr = "10 ** (8- 10)"
        self.assertAlmostEqual(0.01 , ltrEvaluation(expr),places=2)
        with self.assertRaises(ValueError):
            ltrEvaluation("4 + 2   5")
        with self.assertRaises(ZeroDivisionError):
            ltrEvaluation("4 + 2  / (20 / 20 - 1)")
    def test_check_pairing(self):
        with self.assertRaises(ValueError, msg=PAIRING_ERROR):
            ltrEvaluation("((9 + (10 ** 2) - 9) * 10 - (7 / 2)) * 10)") 
        with self.assertRaises(ValueError, msg=PAIRING_ERROR):   
            ltrEvaluation("((9 + (10 ** 2) - 9) * (10 - (7 / 2) * 10)") 
        with self.assertRaises(ValueError, msg=PAIRING_ERROR):   
            ltrEvaluation("((9 + (10 ** 2) - 9) * (10 - (7 / 2)) * (10") 