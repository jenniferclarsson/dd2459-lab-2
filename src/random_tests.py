from unittest import main, TestCase, TestLoader, TextTestRunner
from numpy.random import seed
from numpy.random import randint
import random
from main import *

class test_member(TestCase):

    def setUp(self):
        self.A = randint(0, 100, 10)
        self.key = random.choice(self.A)
        self.bad_key = random.choice([i for i in range(0, 100) if i not in self.A])

    def test(self):
        print("TEST RUN good key", member(self.A, self.key))
        print("TEST RUN bad key", not(member(self.A, self.bad_key)))

if __name__ == "__main__":
    for i in range(100):
        print("----------------------------------------------------------------------")
        print("TEST RUN",  i)
        suite = TestLoader().loadTestsFromTestCase(test_member)
        TextTestRunner().run(suite)