### created by Max Marder

###########
# IMPORTS #
###########

from individual import INDIVIDUAL
import pickle

############
# FILE I/O #
############
		
# open robot.p
f = open ('robot.p', 'r')

# load the best robot into best and evaluate
best = pickle.load(f)
best.Evaluate(False)
print "[best: ", best.fitness, "]"

# close robot.p
f.close()
