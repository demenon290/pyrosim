### created by Max Marder

###########
# IMPORTS #
###########

import random
import math
import pyrosim
from robot import ROBOT
import numpy
import matplotlib.pyplot as plt

####################
# INDIVIDUAL CLASS #
####################

class INDIVIDUAL:
	
	#---CONSTRUCTOR---#
	
	def __init__(self, i):
		
		self.ID = i
		self.genome = numpy.random.random_sample((4,8)) * 2 - 1
		self.fitness = 0
	
	#---EVALUTATE---#
	
	# set pb to False to display the bot
	def Evaluate(self, pb, pp = False):
		self.Start_Evaluation(pb, pp)
		self.Compute_Fitness()
		
	def Start_Evaluation(self, pb, pp):
		
		#---SIMULATOR---#

		# start the simulator
		self.sim = pyrosim.Simulator(eval_time = 1000, play_paused = pp, play_blind = pb)

		#---ROBOTS---#

		# spawn bot
		self.robot = ROBOT(self.sim, self.genome)		
		
		#---SIMULATION---#

		# start the simulation
		self.sim.start()
	
	def Compute_Fitness(self):
		
		#---SIMULATION---#
		
		# cause the simulation to continue as long as it is running
		self.sim.wait_to_finish()
		
		#---DATA---#
		
		# get sensor data from P2 with sensor value index 0
#		x = self.sim.get_sensor_data(sensor_id = robot.P4, svi = 0)
		
		# get sensor data from P2 with sensor value index 1
		y = self.sim.get_sensor_data(sensor_id = self.robot.P4, svi = 1)
		
		# get sensor data from P2 with sensor value index 2
#		z = self.sim.get_sensor_data(sensor_id = robot.P4, svi = 2)

		##TEST
#		sensorData = self.sim.get_sensor_data(sensor_id = robot.P4)
#		sensorData = y[-1]
#		print(sensorData)
		
		# set fitness to depth into sim
		self.fitness = y[-1]

		#---PLOTTING---#

		# instantiate figure as f
#		f = plt.figure()

		# add drawing panel to figure
#		panel = f.add_subplot(111)

		# plot sensorData in panel
#		plt.plot(sensorData)

		# set limit of y-axis
#		panel.set_ylim(-10,+20)

		# show figure
#		plt.show()
		
		#---DELETE SIM---#
		
		del self.sim
	
	#---MUTATE---#

	def Mutate(self):
		geneToMutate = (random.randint(0,3), random.randint(0,7))
		self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], 2)
		if (self.genome[geneToMutate] > 1):
			self.genome[geneToMutate] = 1
		elif (self.genome[geneToMutate]):
			self.genome[geneToMutate] = -1
	
	#---PRINT---#
	
	def Print(self):
		print('['),
		print(self.ID),
		print(self.fitness),
		print('] '),

	
	