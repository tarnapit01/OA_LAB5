import unittest
import os,sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from source.CountClump import CountClump

class TestCountClump (unittest.TestCase):
    
    def setUp(self):
        self.countClump = CountClump()
        self.nums = []
        
    def tearDown(self):
        print("\n\nEnd of Testing")
        
    def test_null(self):
        print("CALLING TEST NULL")
        self.nums = None
        self.assertEqual(self.countClump.count_clumps(self.nums),0)
        print("\nTEST NULL CALLED")
        
    def test_blank_set(self):
        print("\nCALLING TEST BLANK SET")
        self.nums = []
        self.assertEqual(self.countClump.count_clumps(self.nums),0)
        print("\nTEST BLANK SET CALLED")
        
    def test_not_the_same(self):
        print("\nCALLING TEST NOT THE SAME")
        self.nums = [1,2,3]
        self.assertEqual(self.countClump.count_clumps(self.nums),0)
        print("\nTEST NOT THE SAME CALLED")
        
    def test_got_one(self):
        print("\nCALLING TEST GOT ONE")
        self.nums = [1,1,2]
        self.assertEqual(self.countClump.count_clumps(self.nums),1)
        print("\nTEST GOT ONE CALLED")
        
    def test_got_two(self):
        print("\nCALLING TEST GOT TWO")
        self.nums = [1,1,2,3,3,4]
        self.assertEqual(self.countClump.count_clumps(self.nums),2)
        print("\nTEST GOT TWO CALLED")
        
if __name__ == "__main__" :
    unittest.main()