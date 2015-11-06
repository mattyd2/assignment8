import numpy as np

class dailypositionanalyzer(object):
    def __init__(self):
        self = self
        # self.validinput = re.match(r'[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\041-\053]|\0|\v|\f|\a|\n|\r|\t|\s',self.userinput) #robust regex expression to make sure the User Input is really clean.
        # if self.validinput != None or not(self.userinput): # also accounting for the user just hitting return here.
        # raise ValueError('Invalid Intervals. found a character that does not belong or there was nothing entered.')random_outcome_per_position(position_value_calculator(x))

def trading_simluator(numberOfSharesOfSinglePosition, num_trials):
    dayOfTrading = np.empty((num_trials, numberOfSharesOfSinglePosition))
    cumu_ret = np.empty((num_trials))
    for x in np.nditer(t, op_flags=['readwrite']):
        positionValue


def day_of_trading_simulator(positions, num_trials):
    a = positions
    cumu_ret = np.empty((num_trials))
    iteratorationTracker = 0
    for x in np.nditer(a[0,:], flags=['external_loop']):
        if iteratorationTracker < num_trials:
            dayOfTrading = np.empty((num_trials, x))
        iteratorationTracker +=
    return cumu_ret, daily_ret




def position_value_calculator(position):
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

# def random_number_generator():
#     randomlistZeroToOne = np.random.random(size=10000)
#     sumBelow = (randomlistZeroToOne <= 0.51).sum()
#     sumAbove = (randomlistZeroToOne > 0.51).sum()
#     print randomlistZeroToOne, sumBelow, sumAbove
#     if sumBelow > 5100:
#         return 1
#     else:
#         return 0

# def day_of_trading_simulator(position, num_trials):
#     cumu_ret = range(num_trials)
#     daily_ret = range(num_trials)
#     position = position
#     for trial in range(num_trials):
#         print trial, position, position_value_calculator(position)
#         cumu_ret[trial] = float(random_outcome_per_position(position_value_calculator(position)))
#         daily_ret[trial] = (cumu_ret[trial]/10000) - 1
#     return cumu_ret, daily_ret

# def day_of_trading_simulator(positions, num_trials):
#     cumu_ret = range(num_trials)
#     # count = len(positions)
#     daily_ret = [list(xrange(num_trials)) for _ in xrange(num_trials)]
#     counter = -1
#     for x in positions:
#         counter += 1
#         print "x in positions %d" % x
#         i = position_value_calculator(x)
#         for trial in range(num_trials):
#             print trial, i
#             cumu_ret[trial] = float(random_outcome_per_position(i))
#             # need to get the indexing correct for list in list.
#             daily_ret[trial] = (cumu_ret[trial]/10000) - 1
#     # print cumu_ret
#     return cumu_ret, daily_ret

