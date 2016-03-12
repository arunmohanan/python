import unittest
from Util import Timer

from Exercise.Practice import FibanocciNumberGenerator

class FibanocciNumberGeneratorTests(unittest.TestCase):
    expectedTenFibanocciNumbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    
    def testFibanocciNumberGenerator(self):
        with Timer() as t:
            fibanocciNumberGenerator = FibanocciNumberGenerator()
            fibanocciNumbers = fibanocciNumberGenerator.getFibanocciUsingForLoop(10)
            self.assertEqual(self.expectedTenFibanocciNumbers,fibanocciNumbers)
            print (t.interval)

    
        
    def testFibanocciNumberGeneratorUsingRecursion(self):
        fibanocciNumberGenerator = FibanocciNumberGenerator()
        fibanocciNumbers = [fibanocciNumberGenerator.getFibanocciNumberUsingRecursion(n) for n in range(10)]
        self.assertEqual(self.expectedTenFibanocciNumbers, fibanocciNumbers)
        print (fibanocciNumbers)

def main():
    unittest.main()

if __name__ == '__main__':
    main()