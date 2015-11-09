"""This is the main body of the program for Assignment 8"""

#author: Matthew Dunn
#netID: mtd368
#date: 11/10/2015

import positionsimulator
import sys
from positionsimulator import day_of_trading, dailypositionanalyzer

# This try/except design I discussed with Sida because I was struggling with how to start the program. I tride mimicking what was in Adventure and failed.

if __name__ == '__main__':
    try:
        while True:
            # dailypositionanalyzer([1, 10, 100, 1000],10000)
            # day_of_trading([1, 10, 100, 1000],10000)
            try:
                trymore = raw_input('The simulatio has just run 10,000 times for positions 1, 10, 100, and 1000.  Would you try some others? [y/n] ')
                if trymore == 'n':
                    print "Okay. Goodbye."
                    break
                elif trymore == 'y':
                    positions = raw_input('Okay, what number of shares do you wish to buy in parrallel? ')
                else:
                    print "Improper Input. Goodbye."
                    break
                positions = positions.strip("[]")
                try:
                    positions = map(int, positions.split(","))
                    print positions
                except ValueError:
                    print "Improper Input. Goodbye."
                    break
                num_trials = raw_input('How many times to randomly repeat the test? ')
                try:
                    num_trials = int(num_trials)
                except ValueError:
                    print "Improper Input. Goodbye."
                    break
                dailypositionanalyzer(positions,num_trials)
                day_of_trading(positions,num_trials)
                break
            except ValueError:
                print "Improper Input. Let's take it from the top! :-)"
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"
    except ZeroDivisionError:
        print "\n Math Error"
    except TypeError:
        print "\n Type Wrong!"
    except OverflowError:
        print "\n OverflowError!"
