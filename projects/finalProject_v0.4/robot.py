### created by Max Marder

###########
# IMPORTS #
###########

import constants as c
import random

###############
# ROBOT CLASS #
###############

class ROBOT:
	
	###############
	# CONSTRUCTOR #
	###############
	
	def __init__(self, sim, wts):
		
		#---INITIALIZE COMPONENTS---#		
		self.send_objects(sim)	
		self.send_joints(sim)
		self.send_sensors(sim)
		self.send_neurons(sim)
		self.send_synapses(sim, wts)

		#---DELETE DICTIONARIES---#
		del self.O
		del self.J
		del self.S
		del self.SN
		del self.MN		
			
	###########
	# METHODS #
	###########
	
	def send_objects(self, sim):
		
		#---OBJECTS---#		
		# gray base
		self.O0 = sim.send_box(x=0, y=0, z=c.Z, length=c.L, width=c.L, height=c.R*2, r=0.5, g=0.5, b=0.5)		
		# red leg y>0; r2>0
		self.O1 = sim.send_cylinder(x=0.0, y=c.L, z=c.Z,	 
								   length=c.L, radius=c.R, 	
								   r1=0, r2=1, r3=0, 		
								   r=1, g=0, b=0)			
		# green leg x>0; r1>0
		self.O2 = sim.send_cylinder(x=c.L, y=0.0, z=c.Z, 
								   length=c.L, radius=c.R, 
								   r1=1, r2=0, r3=0, 
								   r=0, g=1, b=0)
		# blue leg y<0; r2<0
		self.O3 = sim.send_cylinder(x=0.0, y=-c.L, z=c.Z, 
								   length=c.L, radius=c.R, 
								   r1=0, r2=-1, r3=0, 
								   r=0, g=0, b=1)
		# purple leg x<0; r1<0
		self.O4 = sim.send_cylinder(x=-c.L, y=0.0, z=c.Z, 
								   length=c.L, radius=c.R, 
								   r1=-1, r2=0, r3=0,
								   r=1, g=0, b=1)
		
		# red leg y>0; r3<0
		self.O5 = sim.send_cylinder(x=0.0, y=(c.L+c.L/2), z=c.Z-(c.L/2), 
								   length=c.L, radius=c.R, 
								   r1=0, r2=0, r3=-1, 
								   r=1, g=0, b=0)
		# green leg x>0; r3<0
		self.O6 = sim.send_cylinder(x=(c.L+c.L/2), y=0.0, z=c.Z-(c.L/2), 
								   length=c.L, radius=c.R, 
								   r1=0, r2=0, r3=-1, 
								   r=0, g=1, b=0)
		# blue leg y<0; r30
		self.O7 = sim.send_cylinder(x=0.0, y=-(c.L+c.L/2), z=c.Z-(c.L/2), 
								   length=c.L, radius=c.R, 
								   r1=0, r2=0, r3=-1, 
								   r=0, g=0, b=1)
		# purple leg x<0; r3<0
		self.O8 = sim.send_cylinder(x=-(c.L+c.L/2), y=0.0, z=c.Z-(c.L/2), 
								   length=c.L, radius=c.R, 
								   r1=0, r2=0, r3=-1, 
								   r=1, g=0, b=1)
		
		#---OBJECTS DICTIONARY---#		
		self.O = {}
		
		self.O[0] = self.O0
		self.O[1] = self.O1
		self.O[2] = self.O2
		self.O[3] = self.O3
		self.O[4] = self.O4
		self.O[5] = self.O5
		self.O[6] = self.O6
		self.O[7] = self.O7
		self.O[8] = self.O8

	def send_joints(self,sim):
		
		#---JOINTS---#
		# connect base O0 to legs O1-O4
 		self.J0 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O1, 
									 	x=0, y=c.L/2, z=c.Z,
										n1=-1, n2=0, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J1 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O2, 
									 	x=c.L/2, y=0, z=c.Z,
										n1=0, n2=-1, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J2 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O3, 
									 	x=0, y=-c.L/2, z=c.Z,
										n1=-1, n2=0, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J3 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O4, 
									 	x=-c.L/2, y=0, z=c.Z,
										n1=0, n2=-1, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		
		# connect legs O1-O4 to legs O5-O8
		self.J4 = sim.send_hinge_joint(first_body_id = self.O1, second_body_id = self.O5, 
									 	x=0, y=(c.L+c.L/2), z=c.Z,
										n1=-1, n2=0, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J5 = sim.send_hinge_joint(first_body_id = self.O2, second_body_id = self.O6, 
									 	x=(c.L+c.L/2), y=0, z=c.Z,
										n1=0, n2=-1, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J6 = sim.send_hinge_joint(first_body_id = self.O3, second_body_id = self.O7, 
									 	x=0, y=-(c.L+c.L/2), z=c.Z,
										n1=-1, n2=0, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		self.J7 = sim.send_hinge_joint(first_body_id = self.O4, second_body_id = self.O8, 
									 	x=-(c.L+c.L/2), y=0, z=c.Z,
										n1=0, n2=-1, n3=0,
										lo=-3.14159/2, hi=3.14159/2)
		
		#---JOINTS DICTIONARY---#	
		self.J = {}
		
		self.J[0] = self.J0
		self.J[1] = self.J1
		self.J[2] = self.J2
		self.J[3] = self.J3
		self.J[4] = self.J4
		self.J[5] = self.J5
		self.J[6] = self.J6
		self.J[7] = self.J7
		
	def send_sensors(self,sim):

		#---TOUCH SENSORS---#
		# reports a value of one if that object is in contact with another object, and zero otherwise
		
		# T0-T3 placed in O5-O8
		self.T0 = sim.send_touch_sensor(body_id = self.O5)
		self.T1 = sim.send_touch_sensor(body_id = self.O6)
		self.T2 = sim.send_touch_sensor(body_id = self.O7)
		self.T3 = sim.send_touch_sensor(body_id = self.O8)
		
		#---LIGHT SENSORS---#
		self.L4 = sim.send_light_sensor(body_id = self.O0)	
		
		#---POSITION SENSORS---#
		# tracks robots position in the x,y,z coordinate plane
		# attach position sensor P4 to gray base O0
		#self.P5 = sim.send_position_sensor(body_id = self.O0)
		
		#---PROPRIOCEPTIVE SENSORS---#
		self.P0 = sim.send_proprioceptive_sensor(joint_id = self.J0)
		self.P1 = sim.send_proprioceptive_sensor(joint_id = self.J1)
		self.P2 = sim.send_proprioceptive_sensor(joint_id = self.J2)
		self.P3 = sim.send_proprioceptive_sensor(joint_id = self.J3)
		
		self.P4 = sim.send_proprioceptive_sensor(joint_id = self.J4)
		self.P5 = sim.send_proprioceptive_sensor(joint_id = self.J5)
		self.P6 = sim.send_proprioceptive_sensor(joint_id = self.J6)
		self.P7 = sim.send_proprioceptive_sensor(joint_id = self.J7)
		
		
		#---SENSOR DICTIONARY---#
		
		self.S = {}
		
		self.S[0] = self.T0
		self.S[1] = self.T1
		self.S[2] = self.T2
		self.S[3] = self.T3
		self.S[4] = self.L4
		
		self.S[5] = self.P0
		self.S[6] = self.P1
		self.S[7] = self.P2
		self.S[8] = self.P3
		self.S[9] = self.P4
		self.S[10] = self.P5
		self.S[11] = self.P6
		self.S[12] = self.P7

	def send_neurons(self, sim):
		
		#---SENSOR NEURON DICTIONARY---#	
		self.SN = {}
		
		#---SENSOR NEURONS---#		
		# SN0-SN12 connected to T0-T3,L4 and P0-P7
		for s in self.S:
			self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
		
		#---MOTOR NEURON DICTIONARY---#		
		self.MN = {}		
		
		#---MOTOR NEURONS---#		
		# MN0-MN7 connnected to J0-J7
		for j in self.J:
			self.MN[j] = sim.send_motor_neuron(joint_id = self.J[j], tau = 0.3)
		
	def send_synapses(self,sim,wts):
		
		# wire SN0-SN12 to MN0-MN7
		for j in self.SN:
			for i in self.MN:
				sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j,i] )
		
