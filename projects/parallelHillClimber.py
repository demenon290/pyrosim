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

parents = POPULATION(3)
parents.Evaluate(False)

#---CHILDREN---#
for g in range (1,20):
	
	children = copy.deepcopy(parents)
	children.Mutate()
	children.Evaluate(True)

	#---REPLACE---#

	parents.ReplaceWith(children)
	print("\n")
	print(g)
	parents.Print()
	
parents.Evaluate(False)
