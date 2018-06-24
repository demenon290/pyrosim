### created by Max Marder

###########
# IMPORTS #
###########

from individual import INDIVIDUAL
import copy
import random
from environment import ENVIRONMENT
import constants as c

######################
# ENVIRONMENTS CLASS #
######################

class ENVIRONMENTS:
	
	#---CONSTRUCTOR---#
	def __init__ (self):

		self.envs = {}
		for e in range(0, c.numEnvs):
			self.envs[e] = ENVIRONMENT(e)

	