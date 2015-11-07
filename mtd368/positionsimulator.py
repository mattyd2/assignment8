import numpy as np
import matplotlib.pyplot as plt

class dailypositionanalyzer(object):
    def __init__(self):
        self = self
        # self.validinput = re.match(r'[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\041-\053]|\0|\v|\f|\a|\n|\r|\t|\s',self.userinput) #robust regex expression to make sure the User Input is really clean.
        # if self.validinput != None or not(self.userinput): # also accounting for the user just hitting return here.
        # raise ValueError('Invalid Intervals. found a character that does not belong or there was nothing entered.')random_outcome_per_position(position_value_calculator(x))

def day_of_trading_simulator(positions, num_trials):
    listOfPositions = positions
    indexLog = len(listOfPositions)
    for x in range(indexLog):
        cumu_ret = single_position_simluator(listOfPositions[x],num_trials)         #this is an array with the result of each day

def single_position_simluator(numberOfSharesOfSinglePosition, num_trials):
    dayOfTrading = np.empty((num_trials, numberOfSharesOfSinglePosition))
    for x in np.nditer(dayOfTrading, op_flags=['readwrite']):
        x[...] = daily_position_value_simulator(numberOfSharesOfSinglePosition)     #iterating over all the values in the ndarray and returning the randomized return.
    cumu_ret = np.sum(dayOfTrading, axis=1)                                         #summing for each row which is a num_trial
    print cumu_ret
    daily_ret = np.empty((num_trials))
    indexLog = len(daily_ret)
    for i in range(indexLog):
        daily_ret[i] = (cumu_ret[i]/1000) - 1
    print daily_ret
    return image_creation(daily_ret[i], numberOfSharesOfSinglePosition)

def image_creation(daily_ret, numberOfSharesOfSinglePosition):
    plt.hist(daily_ret,100,range=[-1,1])
    nameOfFile = 'histogram_'+str(numberOfSharesOfSinglePosition).zfill(4)+'_.pos.png'
    plt.savefig(nameOfFile)


def daily_position_value_simulator(position):
    positionValue = 1000/int(position)
    return random_outcome_per_position(positionValue)

def random_outcome_per_position(position_value):
    doubleOrLooseDayValue = random_number_generator()
    if doubleOrLooseDayValue == 1:
        return position_value*2
    return 0

def random_number_generator():
    randomlistZeroToOne = np.random.random()
    if (randomlistZeroToOne > 0.51):
        return 1
    return 0
