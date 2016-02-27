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
