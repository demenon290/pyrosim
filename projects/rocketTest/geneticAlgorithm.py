### created by Max Marder

###########
# IMPORTS #
###########
import pickle
import time

import constants as c
import matplotlib.pyplot as plt
import numpy as np
from environments import ENVIRONMENTS
from population import POPULATION

################
# ENVIRONMENTS #
################
envs = ENVIRONMENTS()

###########
# PARENTS #
###########
# ---NEW POPULATION---#
if (c.newMode):
    # initialize parents
    parents = POPULATION(c.popSize)
    parents.Initialize()

# ---LOAD POPULATION---#
if (c.loadMode):
    # open population myFile
    myFile = open('pop.p', 'rb')
    # load in parents
    parents = pickle.load(myFile)
    # close population myFile
    myFile.close()

# ---EVALUATE PARENTS---#

# evaulate parents in respective environments types
parents.Evaluate(envs, True, pp=False)

# print results for each parent population
print("\nfitness of parents:"),
parents.Print()

###################
# EVOLVE CHILDREN #
###################
startTime = time.time()
g = 0
while (time.time() - startTime < c.runTime):
    # initialize children
    children = POPULATION(c.popSize)
    children.Fill_From(parents)

    # evaluate children
    children.Evaluate(envs, True)

    # print generation and time
    print("\n results of generation: ", g)
    print("\n evaluation time:", time.time() - startTime)
    print("\n remaining time:", c.runTime - (time.time() - startTime))

    # print results for each parent population
    print("\n fitness of children:"),
    children.Print()
    print("\n")

    # ---REPLACE---#
    parents.ReplaceWith(children)

    # ---TABULATE FITNESS---#
    # add fitness of best individual at current generation to
    # tabulated fitness list for plotting
    parents.Tabulate_Fitness()

    # ---INCREMENT GENS---#
    g += 1

###############
# PICKLE SAVE #
###############
myFile = open('pop.p', 'wb')
pickle.dump(parents, myFile)
myFile.close()

#############
# SHOW BEST #
#############		
# ---SHOW BEST ROBOT IN EACH ENVIRONMENT---#
for e in range(c.numEnvs):
    parents.p[0].Start_Evaluation(envs.envs[e], False, pp=True)
    parents.p[0].Compute_Fitness()

############
# PLOTTING #
############
# ---FIGURE---#
# instantiate plot figure as f
f = plt.figure()
# ---PLOT DATA--#
# add drawing panel to figure
panel = f.add_subplot(111)
# get fitness data
fitnessData = np.asarray(parents.fitnessList)
# plot sensorData in panel
plt.plot(fitnessData, "b--")  # control
plt.title('Fitness vs. Generation')
plt.xlabel('generation')
plt.ylabel('fitness')
plt.grid(True)

# ---DISPLAY PLOT---#
plt.show()
