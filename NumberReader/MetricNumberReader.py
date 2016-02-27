'''
Created on Dec 31, 2015

@author: arun
'''


class MetricNumberReader(object):
    '''
    classdocs
    '''

    decimal_place_lookup = {
        0: {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
            9: 'Nine'},
        1: {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen',
            7: 'seventeen', 8: 'eighteen', 9: 'nineteen'},
        2: {2: 'twenty', 3: 'thirty'},
        3: 'hundred'
    }

    def __init__(self):
        '''
        Constructor
        '''

    def read_number(self, numberToRead):
        copyOfNumberToRead = numberToRead
        length_of_number = len(str(numberToRead))
        numberString = ''
        for decimal_place in range(length_of_number):
            # decimal_place_str = str(decimal_place)
            number = numberToRead % 10
            numberString = self.decimal_place_lookup[decimal_place[number]] + ' '
            return numberString
