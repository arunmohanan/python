'''
Created on Mar 6, 2016

@author: anu
'''

import time
from time import sleep

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self
    
    
    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        print ('Time: {!r}'.format(str(self.interval)))
        return self
        
    

def testTimer():
    t = Timer()
    t.__enter__()
    sleep(1)
    t.__exit__()


if __name__ == '__main__':
    testTimer()