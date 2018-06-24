### created by Max Marder
import time

#############
# CONSTANTS #
#############

# robot size
L = 0.08
R = L/5
Z = L*13

# simulator evaluation time
evalTime = 3000
discreteTime = 0.01

# population
popSize = 5
# environment
numEnvs = 4

# new/load population modes
newMode = False
loadMode = True

# time based evaluation mode
seconds = 30		
minutes = 1	
hours = 0		
runTime = (hours*(60*60))+(minutes*60)+seconds

# movie mode (turn on to just watch the best parents)
movieMode = True