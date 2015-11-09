# test case

"""This runs tests on the program to confirm intended functionality is occur."""

#author: Matthew Dunn
#netID: mtd368
#date: 11/10/2015
import os
from unittest import TestCase
from positionsimulator import dailypositionanalyzer, single_position, results_printer

"""test function in positionsimulator.py"""

class dailypositionanalyzer(unittest.TestCase):

    def setUp(self):
        pass

    # position simulator test

    def test_single_position1(self):
        a = single_position(1000,10)        #test for number of trials equal to 10 and there is a single position of $1000
        self.assertEquals(a.shape,(10,))    #confirming the returned array is the correct shape

    def test_single_position2(self):
        a = single_position(1,10)           #test for number of trials equal to 10 and there are 1000 positions each for $1
        self.assertEquals(a.shape,(10,))    #confirming the returned array is the correct shape

    # test of file creation. couldn't get the modules import when I moved it to another directory so the test didn't interfere with real results.

    # def test_results_printer(self):                 #tests whether results file was generated.
    #     dayOfTradingMean = '[1,2,3,4,5]'
    #     dayOfTradingStandardDeviation = '[8,7,5,4,3,1]'
    #     numberOfSharesOfSinglePosition = 10
    #     x = results_printer(dayOfTradingMean, dayOfTradingStandardDeviation, numberOfSharesOfSinglePosition)
    #     a = open('results.txt','r')
    #     self.assertEquals(a.name, 'results.txt')
    #     os.remove('results.txt')

if __name__ == '__main__':
    unittest.main()
