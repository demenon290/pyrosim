### created by Max Marder

###########
# IMPORTS #
###########

from individual import INDIVIDUAL
import copy
import random
from environment import ENVIRONMENT_1
from environment import ENVIRONMENT_2
from environment import ENVIRONMENT_3
import constants as c

#--------------------------------------------------------------------------------------------#

######################
# ENVIRONMENTS CLASS #
######################

class ENVIRONMENTS_1:
	
	#---CONSTRUCTOR---#
	def __init__ (self):

		self.envs = {}
		for e in range(0, c.numEnvs):
			self.envs[e] = ENVIRONMENT_1(e)
			
#--------------------------------------------------------------------------------------------#

class ENVIRONMENTS_2:
	
	#---CONSTRUCTOR---#
	def __init__ (self):

		self.envs = {}
		for e in range(0, c.numEnvs):
			self.envs[e] = ENVIRONMENT_2(e)

#--------------------------------------------------------------------------------------------#

class ENVIRONMENTS_3:
	
	#---CONSTRUCTOR---#
	def __init__ (self):

		self.envs = {}
		for e in range(0, c.numEnvs):
			self.envs[e] = ENVIRONMENT_3(e)