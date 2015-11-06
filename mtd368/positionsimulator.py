import numpy as np

class dailypositionanalyzer(object):
    def __init__(self):
        self = self
        # self.validinput = re.match(r'[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\041-\053]|\0|\v|\f|\a|\n|\r|\t|\s',self.userinput) #robust regex expression to make sure the User Input is really clean.
        # if self.validinput != None or not(self.userinput): # also accounting for the user just hitting return here.
        # raise ValueError('Invalid Intervals. found a character that does not belong or there was nothing entered.')random_outcome_per_position(position_value_calculator(x))

# def day_of_trading_simulator(position, num_trails):
#     cumu_ret = range(num_trails)
#     daily_ret = range(num_trails)
#     position = position
#     for trial in range(num_trails):
#         print trial, position, position_value_calculator(position)
#         cumu_ret[trial] = float(random_outcome_per_position(position_value_calculator(position)))
#         daily_ret[trial] = (cumu_ret[trial]/10000) - 1
#     return cumu_ret, daily_ret

def day_of_trading_simulator(positions, num_trails):
    cumu_ret = range(num_trails)
    # count = len(positions)
    daily_ret = [list(xrange(num_trails)) for _ in xrange(num_trails)]
    counter = -1
    for x in positions:
        counter += 1
        print "x in positions %d" % x
        i = position_value_calculator(x)
        for trial in range(num_trails):
            print trial, i
            cumu_ret[trial] = float(random_outcome_per_position(i))
            # need to get the indexing correct for list in list.
            daily_ret[trial] = (cumu_ret[trial]/10000) - 1
    # print cumu_ret
    return cumu_ret, daily_ret

def random_outcome_per_position(position_value):
    doubleOrLooseDayValue = random_number_generator()
    if doubleOrLooseDayValue == 1:
        return position_value*2
    else:
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

def random_number_generator():
    randomlistZeroToOne = np.random.random()
    if (randomlistZeroToOne > 0.51):
        return 1
    else:
        return 0

def position_value_calculator(position):
    listOfPositionValues = 1000/int(position)
    return listOfPositionValues
