import positionsimulator
import sys
import re
from positionsimulator import day_of_trading_simulator

# This try/except design I discussed with Sida because I was struggling with how to start the program. I tride mimicking what was in Adventure and failed.

if __name__ == '__main__':
    try:
        while True:
            positions = raw_input('Number of shares to buy in parrallel? ')
            positions = positions.strip("[]")
            positions = map(int, positions.split(","))
            print positions
            num_trials = raw_input('How many times to randomly repeat the test? ')
            num_trials = int(num_trials)
            print num_trials
            try:
                values = day_of_trading_simulator(positions,num_trials)
                print values
                break
            except Exception as e: raise
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"
