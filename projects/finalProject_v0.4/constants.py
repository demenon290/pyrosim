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
discreteTime = 0.015

# population
popSize = 8

# environment
numEnvs = 4

# new/load population modes
newMode = False
loadMode = True

# generation based evaluation mode
genMode = False
numGens = 100

# time based evaluation mode
timeMode = True
seconds = 0		
minutes = 5		
hours = 0		
runTime = (hours*(60*60))+(minutes*60)+seconds

