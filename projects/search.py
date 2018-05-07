### created by Max Marder

#############
# SIMULATOR #
#############

import pyrosim
import random
from robot import ROBOT
import matplotlib.pyplot as plt

## TEST spawn 3 bots
for i in range(0,10):

	#############
	# SIMULATOR #
	#############

	# simulator starts paused (CTRL + P) runs for 1000ms
	#sim = pyrosim.Simulator(play_paused = False, eval_time = 1000)

	# start the simulator
	sim = pyrosim.Simulator()

	##########
	# ROBOTS #
	##########
	
	# create random wt
	wt = random.random()*2 - 1 
	
	# spawn bot
	robot = ROBOT(sim, wt)

	##############
	# SIMULATION #
	##############

	# start the simulation
	sim.start()

	# cause the simulation to continue as long as it is running
	sim.wait_to_finish()

	# get and print sensor data from P2
	#sensorData = sim.get_sensor_data(sensor_id = R3)
	#print(sensorData)

	#---PLOTTING---#
	# plot data from sensors and display it

	# instantiate figure as f
	#f = plt.figure()

	# add drawing panel to figure
	#panel = f.add_subplot(111)

	# plot sensorData in panel
	#plt.plot(sensorData)

	# set limit of y-axis
	#panel.set_ylim(-10,+20)

	# show figure
	#plt.show()


