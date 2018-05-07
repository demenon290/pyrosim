### created by Max Marder

###########
# IMPORTS #
###########

import random
from individual import INDIVIDUAL

## TEST spawn 3 bots
for i in range(0,10):
	
	###############
	# INDIVIDUALS #
	###############
	
	individual = INDIVIDUAL()	
	individual.Evaluate()
	print(individual.fitness)
	
	