from unittest import TestCase, main
from main import maxNegativeRepr

class TestMaxNegativeRepr(TestCase):
    def test_several_reprs(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, -1, -4, -100]), 100)
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, -4, 100, -1]),4)   
        
    def test_one_repr(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, -1]),1)
        
    def test_none_repr(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, 1]),-1) 
        
    def test_none_wirh_zero_repr(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, 1, 0, 0]),-1)   
if __name__ == "__main__" :
    main()      