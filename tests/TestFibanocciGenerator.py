import unittest
from NumberReader.Practice import FibanocciNumberGenerator

class FibanocciNumberGeneratorTests(unittest.TestCase):
    def testFibanocciNumberGenerator(self):
        fibanocciNumberGenerator = FibanocciNumberGenerator()
        fibanocciNumberGenerator.print_fibanocci(10)


def main():
    unittest.main()

if __name__ == '__main__':
    main()