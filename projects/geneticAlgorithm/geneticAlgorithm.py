### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import random
from individual import INDIVIDUAL
from population import POPULATION

#---PARENTS---#
parents = POPULATION(10)
parents.Initialize()
parents.Evaluate(True)
print("0"),
parents.Print()

#---CHILDREN---#
for g in range (1,201):
	
	children = POPULATION(5)
	children.Fill_From(parents)
	children.Evaluate(True)
	print("\n")
	print(g),
	children.Print()

	#---REPLACE---#

	parents.ReplaceWith(children)


#---SHOW BEST ROBOT---#
parents.p[0].Evaluate(False, True)