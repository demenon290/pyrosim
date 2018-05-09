### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import time
import matplotlib.pyplot as plt
import numpy as np
import constants as c
from individual import INDIVIDUAL
from population import POPULATION
from environments import ENVIRONMENTS_1
from environments import ENVIRONMENTS_2
from environments import ENVIRONMENTS_3

###############
# PICKLE LOAD #
###############

file_1 = open('pop_1.p','rb')
file_2 = open('pop_2.p','rb')
file_3 = open('pop_3.p','rb')

################
# ENVIRONMENTS #
################

envs_1 = ENVIRONMENTS_1()
envs_2 = ENVIRONMENTS_2()
envs_3 = ENVIRONMENTS_3()

###########
# PARENTS #
###########

#---NEW POPULATION---#
if (c.newMode):
	# initialize parents
	parents_1 = POPULATION(c.popSize)
	parents_1.Initialize()
	#--------------------#
	parents_2 = POPULATION(c.popSize)
	parents_2.Initialize()
	#--------------------#
	parents_3 = POPULATION(c.popSize)
	parents_3.Initialize()

#---LOAD POPULATION---#
if (c.loadMode):
	# load in parents
	parents_1 = pickle.load(file_1)
	parents_2 = pickle.load(file_2)
	parents_3 = pickle.load(file_3)
	# close files
	file_1.close()
	file_2.close()
	file_3.close()

# evaulate parents in respective environments types
parents_1.Evaluate(envs_1, True, pp = False)
parents_2.Evaluate(envs_2, True, pp = False)
parents_3.Evaluate(envs_3, True, pp = False)

# print results for each parent population
print("\nfitness of parents 1 in envs 1:"),
parents_1.Print()
print("\nfitness of parents 2 in envs 2:"),
parents_2.Print()
print("\nfitness of parents 3 in envs 3:"),
parents_3.Print()
print("\n")

###################
# EVOLVE CHILDREN #
###################		

startTime = time.time()
g = 0
while (time.time()-startTime < c.runTime):
	# initialize children
	children_1 = POPULATION(c.popSize)
	children_1.Fill_From(parents_1)
	#--------------------#
	children_2 = POPULATION(c.popSize)
	children_2.Fill_From(parents_2)
	#--------------------#
	children_3 = POPULATION(c.popSize)
	children_3.Fill_From(parents_3)

	# evaluate children in respective environment types
	children_1.Evaluate(envs_1, True)
	children_2.Evaluate(envs_2, True)
	children_3.Evaluate(envs_3, True)

	# print generation and time
	print("\n results of generation: ", g)
	print("\n evaluation time:", time.time()-startTime)
	print("\n remaining time:", c.runTime-(time.time()-startTime))

	# print results for each parent population
	print("\n fitness of children 1 in envs 1:"),
	children_1.Print()
	print("\n fitness of children 2 in envs 2:"),
	children_2.Print()
	print("\n fitness of children 3 in envs 3:"),
	children_3.Print()
	print("\n")

	#---REPLACE---#
	parents_1.ReplaceWith(children_1)
	parents_2.ReplaceWith(children_2)
	parents_3.ReplaceWith(children_3)

	#---TABULATE FITNESS---#
	# add fitness of best individual at current generation to
	# tabulated fitness list for plotting
	parents_1.Tabulate_Fitness()
	parents_2.Tabulate_Fitness()
	parents_3.Tabulate_Fitness()

	#---INCREMENT GENS---#
	g+=1

#############
# SHOW BEST #
#############		

#---SHOW BEST ROBOT IN ALL ENVIRONMENTS---#
for e in range(c.numEnvs):
	parents_1.p[0].Start_Evaluation(envs_1.envs[e], False)
	parents_1.p[0].Compute_Fitness()
	#--------------------#
	parents_2.p[0].Start_Evaluation(envs_2.envs[e], False)
	parents_2.p[0].Compute_Fitness()
	#--------------------#
	parents_3.p[0].Start_Evaluation(envs_3.envs[e], False)
	parents_3.p[0].Compute_Fitness()

###############
# PICKLE SAVE #
###############

file_1 = open('pop_1.p', 'wb')
file_2 = open('pop_2.p', 'wb')
file_3 = open('pop_3.p', 'wb')
pickle.dump(parents_1, file_1)
pickle.dump(parents_2, file_2)
pickle.dump(parents_3, file_3)
file_1.close()
file_2.close()
file_3.close()

############
# PLOTTING #
############

#---FIGURE---#
# instantiate plot figure as f
f = plt.figure()

#---PLOT DATA--#
# add drawing panel to figure
panel = f.add_subplot(111)
# get fitness data
fitnessData_1 = np.asarray(parents_1.fitnessList)
fitnessData_2 = np.asarray(parents_2.fitnessList)
fitnessData_3 = np.asarray(parents_3.fitnessList)

# plot sensorData in panel
plt.plot(fitnessData_1, "b--",	# control
		 fitnessData_2, "r--",	# uphill
		 fitnessData_3, "g--")	# wild
plt.title('Fitness vs. Generation')
plt.ylabel('fitness')
plt.grid(True)

#---DISPLAY PLOT---#
plt.show()