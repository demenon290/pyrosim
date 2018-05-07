### created by Max Marder

###########
# IMPORTS #
###########

import random
import math
import pyrosim
from robot import ROBOT
import constants as c
import numpy
import matplotlib.pyplot as plt

####################
# INDIVIDUAL CLASS #
####################

class INDIVIDUAL:
	
	#---CONSTRUCTOR---#
	def __init__(self, i):
		
		self.ID = i
		self.genome = numpy.random.random_sample((5,8)) * 2 - 1
		self.fitness = 0
	
	#---EVALUTATE---#	
	# set pb to False to display the bot
	def Evaluate(self, env, pb, pp = False):
		self.Start_Evaluation(env, pb, pp)
		self.Compute_Fitness()
		
	def Start_Evaluation(self, env, pb, pp = False):
		
		#---SIMULATOR---#
		# start the simulator
		self.sim = pyrosim.Simulator(eval_time = c.evalTime, play_paused = pp, play_blind = pb)

		#---ROBOTS---#
		# spawn bot
		self.robot = ROBOT(self.sim, self.genome)
		
		#---ENVIRONMENTS---#
		env.Send_To(self.sim)
		
		#---SIMULATION---#
		# start the simulation
		self.sim.start()
	
	def Compute_Fitness(self):
		
		#---SIMULATION---#	
		# cause the simulation to continue as long as it is running
		self.sim.wait_to_finish()
		
		#---DATA---#	
		# set fitness to proximity to light sensor
		self.fitness += self.sim.get_sensor_data(sensor_id = self.robot.L4)[-1]

		#---DELETE SIM---#
		del self.sim
	
	#---MUTATE---#
	def Mutate(self):
		i_gene = random.randint(0,4) 
		j_gene = random.randint(0,7)
		self.genome[i_gene][j_gene] = random.gauss(self.genome[i_gene][j_gene], 1)
		if (self.genome[i_gene][j_gene] > 1):
			self.genome[i_gene][j_gene] = 1
		elif (self.genome[i_gene][j_gene] < -1):
			self.genome[i_gene][j_gene] = -1
	
	#---PRINT---#	
	def Print(self):
		print('['),
		print(self.ID),
		print(self.fitness),
		print('] '),

	
	