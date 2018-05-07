# created by Max Marder

import pyrosim
import matplotlib.pyplot as plt

#############
# SIMULATOR #
#############

# simulator starts paused (CTRL + P) runs for 1000ms
#sim = pyrosim.Simulator(play_paused = False, eval_time = 1000)

# start the simulator
sim = pyrosim.Simulator()

###########
# OBJECTS #
###########

# white cylinder placed above origin with a length of 1 and radius of 1
# oriented straight up
# colored white
whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)

# cylinder placed left/above origin with a length of 1 and radius of 1
# oriented right and inward
# colored red
redObject = sim.send_cylinder(x=0.0, y=0.5, z=1.1, length=1.0, radius=0.1, 
							  r1=0, r2=1, r3=0, 
							  r=1, g=0, b=0)

##########
# JOINTS #
##########

# joint created at the intersection of the red and white cylinders
joint = sim.send_hinge_joint(first_body_id = whiteObject, second_body_id = redObject, 
							 x=0, y=0, z=1.1,
							n1=-1, n2=0, n3=0,
							lo=-3.14159/2, hi=3.14159/2)

###########
# SENSORS #
###########

#---TOUCH SENSORS---#
# reports a value of one if that object is in contact with another object, and zero otherwise

# touch sensor T0 placed inside the center of white cylinder
T0 = sim.send_touch_sensor(body_id = whiteObject)

# touch sensor T1 placed inside the center of red cylinder
T1 = sim.send_touch_sensor(body_id = redObject)

#---PROPRIOCEPTIVE SENSORS---#
# returns the current angle of the joint

# proprioceptive sensor P2 placed at joint
P2 = sim.send_proprioceptive_sensor(joint_id = joint)

#---RAY SENSORS---#
# emits a ray outward from the object in which its embedded, and returns the length of that ray

# ray sensor R3 placed in red cyllinder
# placed at the tip of the red cylinder
# points ray right and inward
R3 = sim.send_ray_sensor(body_id = redObject, 
						 x = 0, y = 1.1, z = 1.1, 
						 r1 = 0, r2 = 1, r3 = 0)

###########
# NEURONS #
###########

# sensor neuron SN0 captures data from T03
SN0 = sim.send_sensor_neuron(sensor_id = T0)

# motor neuron MN2 captures value from joint
MN2 = sim.send_motor_neuron(joint_id = joint)

# creates a synapse that connects neuron SN1 to neuron MN2 
#sim.send_synapse(source_neuron_id = SN1, target_neuron_id = MN2, weight = 1.0)

##############
# SIMULATION #
##############

# start the simulation
sim.start()

# cause the simulation to continue as long as it is running
sim.wait_to_finish()

# get and print sensor data from P2
sensorData = sim.get_sensor_data(sensor_id = R3)
print(sensorData)

#---PLOTTING---#
# plot data from sensors and display it

# instantiate figure as f
f = plt.figure()

# add drawing panel to figure
panel = f.add_subplot(111)

# plot sensorData in panel
plt.plot(sensorData)

# set limit of y-axis
panel.set_ylim(-10,+20)

# show figure
plt.show()

