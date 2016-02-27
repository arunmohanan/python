import pdb

testNumber = 1330

class PracticeUtils:

	def convertNumberToString(self, testNumber):
		strNumber = []
			numberDict =  ['zero', 'one','two','three']
			teenDict = ['eleven','twelve','thirteen']
			tensDict = ['ten','twenty','thirty']
			decimalPlaceDict = ['hundred', 'thousand']
			decimalPosition = 0
			#pdb.set_trace()
			numberDecimals = len(str(testNumber))
			if(numberDecimals>2):
				decimalPlace = 10**(numberDecimals-1)
				value = testNumber // (decimalPlace)
				strNumber.append(numberDict[value])
				strNumber.append(decimalPlaceDict[numberDecimals -3])
				if testNumber % decimalPlace == 0:
					return strNumber
				return convertNumberToString(testNumber % decimalPlace)
			elif len(str(testNumber)) == 2:
				tens = testNumber // 10
				nextDecimal = testNumber % 10
				if tens == 1 and nextDecimal != 0:
					strNumber.append(teenDict[nextDecimal -1])
					return strNumber
				else:
					strNumber.append(tensDict[tens - 1])
					if testNumber % 10 == 0:
						return strNumber
					return convertNumberToString(testNumber % 10)
			else:
				strNumber.append(numberDict[testNumber])
				return strNumber
		myStrNumber = convertNumberToString(testNumber)
		print ('String number : {0}'.format(myStrNumber))