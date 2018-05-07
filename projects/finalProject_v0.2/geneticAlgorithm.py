### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import random
from individual import INDIVIDUAL
from population import POPULATION
from environments import ENVIRONMENTS
import constants as c

#---ENVIRONMENTS---#
envs = ENVIRONMENTS()

#---PARENTS---#
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, False, pp = True)
parents.Print()

"""
#---CHILDREN---#
for g in range (0,c.numGens):
	
	children = POPULATION(c.popSize)
	children.Fill_From(parents)
	children.Evaluate(envs, True)
	print("\n")
	print(g),
	children.Print()

	#---REPLACE---#
	parents.ReplaceWith(children)

#---SHOW BEST ROBOT IN ALL ENVIRONMENTS---#
for e in range(c.numEnvs):
	parents.p[0].Start_Evaluation(envs.envs[e], False)
	parents.p[0].Compute_Fitness()
"""