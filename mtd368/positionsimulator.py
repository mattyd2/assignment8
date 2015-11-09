"""This is the primary class for the program for Assignment 8 that simulates trading."""

#author: Matthew Dunn
#netID: mtd368
#date: 11/10/2015

import numpy as np
import matplotlib.pyplot as plt

class dailypositionanalyzer(object):
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials

def day_of_trading(positions, num_trials):

    """This function accepts two parameters a list called positions that represent the trades,
    and integer value, num_trials, representing the number of times the simulation
    should be run."""

    indexLog = len(positions)
    cumu_ret = np.zeros((0, num_trials),dtype=int)
    for x in range(indexLog):
        cumu_ret = np.insert(cumu_ret, [x], single_position(positions[x],num_trials), axis=0)  #this is an array with the result of each day
    daily_ret = (cumu_ret/1000.) - 1                                                            #normalizing results of daily trading
    image_creation(daily_ret, positions)

def image_creation(daily_ret, numberOfSharesOfSinglePosition):

    """This function accepts two parameters, an array contianing the cumulative returns for each
    simulated day of trading and an integer value, numberOfSharesOfSinglePosition,
    representing the number shares purchased for a single position. It generates a
    historgram for the daily return of the positions and saves it to the project file."""

    for i in range(daily_ret.shape[0]):
        plt.figure()
        title = 'Number of Shares Purchased in Parallel: '+str(numberOfSharesOfSinglePosition[i])
        plt.title(title)
        plt.ylabel('Number of Results')
        plt.xlabel('Results of Position Type')
        plt.hist(daily_ret[i],100,range=[-1,1])
        nameOfFile = 'histogram_'+str(numberOfSharesOfSinglePosition[i]).zfill(4)+'_.pos.png'
        plt.savefig(nameOfFile)

def single_position(numberOfSharesOfSinglePosition, num_trials):

    """This function accepts two integer parameters, numberOfSharesOfSinglePosition and num_trials.
    numberOfSharesOfSinglePosition indicates how many shares will be purchased based of a position
    and the num_trials is the number of times the simulation will be run. This function returns
    an array that contains the values for each day of trading."""

    dayOfTrading = np.empty((num_trials, numberOfSharesOfSinglePosition))
    for x in np.nditer(dayOfTrading, op_flags=['readwrite']):
        x[...] = daily_position_value(numberOfSharesOfSinglePosition)     #iterating over all the values in the ndarray and returning the randomized return.
    cumu_ret = np.sum(dayOfTrading, axis=1)                               #summing for each row which is a num_trial
    dayOfTradingMean = str(np.mean(dayOfTrading, axis=1))
    dayOfTradingStandardDeviation = str(np.std(dayOfTrading, axis=1))
    results_printer(dayOfTradingMean, dayOfTradingStandardDeviation, numberOfSharesOfSinglePosition)
    return cumu_ret

def results_printer(dayOfTradingMean, dayOfTradingStandardDeviation, numberOfSharesOfSinglePosition):

    """This function accepts three parameters, the dayOfTradingMean, dayOfTradingStandardDeviation, and
    numberOfSharesOfSinglePosition. dayOfTradingMean and dayOfTradingStandardDeviation are both
    both strings and the numberOfSharesOfSinglePosition is a integer value.  The function generates
    a text file containing the results for each day of trading."""

    concateOutputPerDay = ''
    concateOutputPerDay = 'Number of Shares: ' + str(numberOfSharesOfSinglePosition) + '\n' + '\n' + 'Expected Value: ' + str(dayOfTradingMean) + '\n' + 'Standard Deviation: ' + str(dayOfTradingStandardDeviation) + '\n' + '\n'
    with open('results.txt','a') as myfile:
        myfile.write(concateOutputPerDay)
    myfile.close()

def daily_position_value(position):

    """This function accepts one parameter, an integer representing the position and calculates
    the value of the position returning the value of that position as either twice it's initial
    value or zero, based on the random_outcome_per_position function."""

    positionValue = 1000/int(position)
    return random_outcome_per_position(positionValue)

def random_outcome_per_position(position_value):

    """This function accepts one parameter, an integer representing a position's value
    and then calls a random number generator to determine whether it will return
    twice input parameter's value or zero."""

    doubleOrLooseDayValue = random_number_generator()
    if doubleOrLooseDayValue == 1:
        return position_value*2
    return 0

def random_number_generator():

    """This function accepts no parameters and returns a one or zero base on a
    random number generator set to be slighly biased towards return a value of
    one, at 0.51 frequency"""

    randomlistZeroToOne = np.random.random()
    if (randomlistZeroToOne > 0.51):
        return 1
    return 0
