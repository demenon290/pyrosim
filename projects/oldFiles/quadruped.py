### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import copy
import random
from individual import INDIVIDUAL
from population import POPULATION

#---PARENTS---#

# create population of size 1
parents = POPULATION(10)
parents.Evaluate(True)

#---CHILDREN---#
for g in range (0,200):
	
	children = copy.deepcopy(parents)
	children.Mutate()
	children.Evaluate(True)

	#---REPLACE---#

	parents.ReplaceWith(children)
	print("\n")
	print(g),
	parents.Print()

#---SHOW BEST ROBOTS---#
parents.Evaluate(False, True)