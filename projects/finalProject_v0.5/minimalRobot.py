### created by Max Marder

###############
# ROBOT CLASS #
###############

class MINROBOT:
	def __init__(self, sim, wts):

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
	
		#---POSITION SENSORS---#
		# tracks robots position in the x,y,z coordinate plane
		
		# attach position sensor P4 to red object
		self.P4 = sim.send_position_sensor(body_id = redObject)

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
		
		#---NEURONS---#

		# sensor neuron SN0 captures data from T0
		SN0 = sim.send_sensor_neuron(sensor_id = T0)
		
		# sensor neuron SN1 captures data from T1
		SN1 = sim.send_sensor_neuron(sensor_id = T1)

		# sensor neuron SN2 captures data from P2
		SN2 = sim.send_sensor_neuron(sensor_id = P2)
		
		# sensor neuron SN3 captures data from R3
		SN3 = sim.send_sensor_neuron(sensor_id = R3)
		
		# motor neuron MN4 captures value from joint
		MN4 = sim.send_motor_neuron(joint_id = joint)
		
		#---SENSOR NEURON DICTIONARY---#
		
		sensorNeurons = {}
		
		sensorNeurons[0] = SN0
		sensorNeurons[1] = SN1
		sensorNeurons[2] = SN1
		sensorNeurons[3] = SN3
		
		#---MOTOR NEURON DICTIONARY---#
		
		motorNeurons = {}
		
		motorNeurons[0] = MN4
		
		############
		# SYNAPSES #
		############
	
		# creates a synapse that connects sensor neurons SN to motor neuron MN
		for s in sensorNeurons:
			for m in motorNeurons:
				sim.send_synapse(source_neuron_id = sensorNeurons[s], target_neuron_id = motorNeurons[m], weight = wts[s][m])


