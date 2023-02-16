from unittest import main, TestCase, TestLoader, TextTestRunner
from numpy.random import seed
from numpy.random import randint
import random
from main import *

class test_search(TestCase):

    def setUp(self):
        self.A = randint(0, 100, 20)
        self.key = random.choice(self.A)
        self.bad_key = random.choice([i for i in range(0, 100) if i not in self.A])
        print(self.A, self.key, self.bad_key)

    def test_key_exists(self):
        res = member(self.A, self.key)
        self.assertTrue(res)

    def test_key_does_not_exist(self):
        res = member(self.A, self.bad_key)
        self.assertFalse(res)

if __name__ == "__main__":
    for i in range(10):
        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("TEST RUN",  i)
        suite = TestLoader().loadTestsFromTestCase(test_search)
        TextTestRunner().run(suite)