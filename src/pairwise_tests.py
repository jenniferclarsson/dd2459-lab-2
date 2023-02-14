from unittest import main, TestCase
from allpairspy import AllPairs
from main import *

class test_search(TestCase):

    def setUp(self):
        self.arrays = [[1, 10], [1, 3, 5, 5, 10]]
        self.keys = [1, 0, 10]
        self.parameters =[self.arrays, self.keys]

    def test(self):
        for i, pairs in enumerate(AllPairs(self.parameters)):
            res = member(pairs[0], pairs[1])
            if pairs[1] == 1:
                self.assertTrue(res)
            elif pairs[1] == 10:
                self.assertTrue(res)
            else:
                self.assertFalse(res)


if __name__ == "__main__":
    main()