### created by Max Marder

###########
# IMPORTS #
###########

import pickle

import constants as c
import matplotlib.pyplot as plt
import numpy as np
from environments import ENVIRONMENTS

################
# ENVIRONMENTS #
################
envs = ENVIRONMENTS()

###########
# PARENTS #
###########
# open population myFile
myFile = open('pop.p', 'rb')
# load in parents
parents = pickle.load(myFile)
# close population myFile
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

# ---LOAD POPULATION---#
# open population myFile
myFile = open('pop.p', 'rb')
# load in parents
parents = pickle.load(myFile)
# close population myFile
myFile.close()
