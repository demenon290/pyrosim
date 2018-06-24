### created by Max Marder
import time

#############
# CONSTANTS #
#############

# robot size
L = 0.08
R = L/5
Z = L*13

# rocket constants
MAIN_HEIGHT = 1.0
MAIN_WIDTH = MAIN_HEIGHT/5.0
NUM_THRUSTERS = 4

# simulator evaluation time
evalTime = 1500
discreteTime = 0.05

# population
popSize = 5
# environment
numEnvs = 4

# new/load population modes
newMode = False
loadMode = True

# time based evaluation mode
seconds = 30		
minutes = 0	
hours = 0 	
runTime = (hours*(60*60))+(minutes*60)+seconds
