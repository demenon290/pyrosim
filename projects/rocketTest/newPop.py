### created by Max Marder

###########
# IMPORTS #
###########

import pickle

from population import POPULATION

###########
# PARENTS #
###########
# initialize parents
parents = POPULATION(c.popSize)
parents.Initialize()

###############
# PICKLE SAVE #
###############
myFile = open('pop.p', 'wb')
pickle.dump(parents, myFile)
myFile.close()
