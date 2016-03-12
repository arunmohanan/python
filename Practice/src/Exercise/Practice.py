from math import sqrt
from Util import Timer
class PracticeUtils:
    numberDict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'severn', 'eight', 'nine']
    teenDict = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tensDict = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    decimalPlaceDict = ['hundred', 'thousand', 'hundred thousand', 'million']

    def convertNumberToString(self, testNumber):
        strNumber = []
        # pdb.set_trace()
        numberDecimals = len(str(testNumber))
        if (numberDecimals > 2):
            decimalPlace = 10 ** (numberDecimals - 1)
            value = testNumber // (decimalPlace)
            strNumber.append(self.numberDict[value])
            strNumber.append(self.decimalPlaceDict[numberDecimals - 3])
            if testNumber % decimalPlace == 0:
                return strNumber
            return self.convertNumberToString(testNumber % decimalPlace)
        elif len(str(testNumber)) == 2:
            tens = testNumber // 10
            nextDecimal = testNumber % 10
            if tens == 1 and nextDecimal != 0:
                strNumber.append(self.teenDict[nextDecimal - 1])
                return strNumber
            else:
                strNumber.append(self.tensDict[tens - 1])
                if testNumber % 10 == 0:
                    return strNumber
                return self.convertNumberToString(testNumber % 10)
        else:
            strNumber.append(self.numberDict[testNumber])
            return strNumber
        
class FibanocciNumberGenerator:
    def getFibanocciUsingForLoop(self, maxCountOfFibanocciNumber):
        n0 = 0
        n1 = 1
        fibanocciNumbers = []
        fibanocciNumbers.append(n0)
        for n in range(maxCountOfFibanocciNumber - 1):
            fibanocciNumbers.append(n1)
            n0, n1 = n1, n0 + n1
        return fibanocciNumbers

    def getFibanocciNumberUsingRecursion(self, maxCountOfFibanocciNumber):
        if(maxCountOfFibanocciNumber == 0):
            return 0
        elif(maxCountOfFibanocciNumber == 1):
            return 1
        else:
            nextFibanocciNumber = self.getFibanocciNumberUsingRecursion(maxCountOfFibanocciNumber - 1) + self.getFibanocciNumberUsingRecursion(maxCountOfFibanocciNumber - 2)
            return nextFibanocciNumber

class PrimeNumber:
    def isPrimeNumber(self, number):
        with Timer():
            if number == 2:
                return True
            if number < 2:
                return False
            if number > 2 and number % 2 == 0:
                return False
            for value in range(3, int(sqrt(number)) + 1, 2):
                if number % value == 0:
                    return False
                return True 