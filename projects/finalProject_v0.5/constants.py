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
evalTime = 2000
discreteTime = 0.01

# population
popSize = 8
# environment
numEnvs = 4

# new/load population modes
newMode = False
loadMode = True

# time based evaluation mode
seconds = 0		
minutes = 0	
hours = 2		
runTime = (hours*(60*60))+(minutes*60)+seconds