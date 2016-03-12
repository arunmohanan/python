'''
Created on Mar 6, 2016

@author: arun
'''
import unittest
from Exercise.Practice import PrimeNumber

class Test(unittest.TestCase):


    def testPrimeNumber(self):
        primeNumberTester = PrimeNumber()
        primeNumbers = [x for x in range(100) if primeNumberTester.isPrimeNumber(x)]
        print (primeNumbers) 
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrimeNumber']
    unittest.main()