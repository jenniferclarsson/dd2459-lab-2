from unittest import main, TestCase
from main import *

class test_member(TestCase):

    def setUp(self):
        self.key = 0
        self.bad_key = 2
        self.n = 10
        self.numArrays = self.n**2+self.n+1
        self.arrays = [[0 for i in range(self.n)] for j in range(self.numArrays)]
        for i in range(1, self.n+1):
            self.arrays[i][i-1] = 1

        i = self.n+1
        a = 0
        for k in range(self.n):
            for j in range(i+k*self.n, i+(k+1)*self.n):
                self.arrays[j][k] = 1
                self.arrays[j][a] = -1
                a += 1
            a = 0

    def test_key_exists(self):
        for i in range(self.numArrays):
            print("TEST RUN good key",  i, member(self.arrays[i], self.key))
            print("TEST RUN bad key",  i, not(member(self.arrays[i], self.bad_key)))

if __name__ == "__main__":
    main()