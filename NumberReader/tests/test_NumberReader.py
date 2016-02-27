'''
Created on Dec 31, 2015

@author: arun
'''
import unittest

from NumberReader.Practice import PracticeUtils


class Test(unittest.TestCase):
    def setUp(self):
        self.numberReader = PracticeUtils()

    def test_number_reader_reading_single_digit(self):
        stringNumber = self.numberReader.convertNumberToString(2)
        self.assertEqual(['two'], stringNumber)

    def test_read_zero(self):
        self.assertEquals(['zero'], self.numberReader.convertNumberToString(0))

    def test_read_one_hundred(self):
        self.assertEquals(['one', 'hundred'], self.numberReader.convertNumberToString(100))

    def test_read_one_thousand(self):
        self.assertEquals(['one', 'thousand'], self.numberReader.convertNumberToString(1000))

    @unittest.skip
    def test_read_ten_thousand_one_hundred(self):
        self.assertEquals(['ten', 'thousand', 'one', 'hundred'], self.numberReader.convertNumberToString(10100))


if __name__ == "__main__":
    unittest.main()
