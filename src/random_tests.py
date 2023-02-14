from unittest import main, TestCase
from numpy.random import seed
from numpy.random import randint
import random
from main import *

class test_search(TestCase):

    def setUp(self):
        seed(1)
        self.A = randint(0, 100, 20)
        self.A = insertion_sort(self.A)    
        self.key = random.choice(self.A)
        self.bad_key = random.choice([i for i in range(0, 100) if i not in self.A])

    def test_key_exists(self):
        res = member(self.A, self.key)
        self.assertTrue(res)

    def test_key_does_not_exist(self):
        res = member(self.A, self.bad_key)
        self.assertFalse(res)
    

if __name__ == "__main__":
    main()