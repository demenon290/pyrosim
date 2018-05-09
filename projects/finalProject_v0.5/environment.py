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

#--------------------------------------------------------------------------------------------#

#######################
# ENVIRONMENT CLASSES #
#######################

# environment 1 is the control environment
# the robot will perform phototaxis in a flat plane with no slope

class ENVIRONMENT_1:
	
	#---CONSTRUCTOR---#	
	def __init__(self, i):
		# environment id
		self.ID = i
		# light box variables
		self.l = c.L
		self.w = c.L
		self.h = c.L
		self.x = 0
		self.y = 0
		self.z = 0

		# set light box and slope location according to environment
		if(self.ID == 0):
			self.Place_Light_Source_To_The_Front()
		elif(self.ID == 1):
			self.Place_Light_Source_To_The_Back()
		elif(self.ID == 2):
			self.Place_Light_Source_To_The_Right()
		elif(self.ID == 3):
			self.Place_Light_Source_To_The_Left()
		else:
			self.Place_Light_Source_To_The_Front()
	
	#---LIGHT SOURCE METHODS---#	
	def Place_Light_Source_To_The_Front(self):
		self.x = 0
		self.y = c.L*25
		self.z = c.L
	def Place_Light_Source_To_The_Back(self):
		self.x = 0
		self.y = -c.L*25
		self.z = c.L
	def Place_Light_Source_To_The_Right(self):
		self.x = c.L*25
		self.y = 0
		self.z = c.L
	def Place_Light_Source_To_The_Left(self):
		self.x = -c.L*25
		self.y = 0
		self.z = c.L
	
	#---SEND BOX TO SIM---#
	# send white box to simulator
	def Send_To(self, sim):
		self.lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, 
										length=self.l, width=self.w, height=self.h,
									    r=1.0, g=1.0, b=1.0) 
		# fix box in place xyz space
		sim.send_hinge_joint(first_body_id=self.lightSource, second_body_id=pyrosim.Simulator.WORLD,
								x=self.x, y=self.y, z=self.z,
								n1=0, n2=0, n3=1,
							    lo=0, hi=0)
		# attatch light source to box
		sim.send_light_source(body_id = self.lightSource)
		
	#---SEND SLOPE TO SIM---#
	def Send_Slope(self, sim):
		pass

	#---PRINT---#	
	def Print(self):
		print("["), 
		print (self.ID),
		print("size:", self.l, self.w, self.h),
		print("position:", self.x, self.y, self.z),
		print("]")

#--------------------------------------------------------------------------------------------#

# environment 2 is the consistent light position environment
# the robot will perform phototaxis on a slope
# the light source will consistantly appear at the top of the slope which changes positions
		
class ENVIRONMENT_2:
	
	#---CONSTRUCTOR---#	
	def __init__(self, i):
		# environment id
		self.ID = i
		# light box variables
		self.l = c.L
		self.w = c.L
		self.h = c.L
		self.x = 0
		self.y = 0
		self.z = 0
		# slope variables
		self.slopeL = c.L*55
		self.slopeW = c.L*55
		self.slopeH = c.L
		self.slopeX = 0
		self.slopeY = 0
		self.slopeZ = (c.L+c.R)*5
		self.slopeR1 = 0
		self.slopeR2 = 0
		self.slopeR3 = 0		
		self.slopeN1 = 0
		self.slopeN2 = 0
		self.slopeN3 = 0
	
		# set light box and slope location according to environment
		if(self.ID == 0):
			self.Place_Light_Source_To_The_Front()
			self.Place_Slope_Front()
		elif(self.ID == 1):
			self.Place_Light_Source_To_The_Back()
			self.Place_Slope_Back()
		elif(self.ID == 2):
			self.Place_Light_Source_To_The_Right()
			self.Place_Slope_Right()
		elif(self.ID == 3):
			self.Place_Light_Source_To_The_Left()
			self.Place_Slope_Left()
		else:
			self.Place_Light_Source_To_The_Front()
			self.Place_Slope_Front()
	
	#---LIGHT SOURCE METHODS---#	
	def Place_Light_Source_To_The_Front(self):
		self.x = 0
		self.y = c.L*25
		self.z = c.Z+c.L
	def Place_Light_Source_To_The_Back(self):
		self.x = 0
		self.y = -c.L*25
		self.z = c.Z+c.L
	def Place_Light_Source_To_The_Right(self):
		self.x = c.L*25
		self.y = 0
		self.z = c.Z+c.L
	def Place_Light_Source_To_The_Left(self):
		self.x = -c.L*25
		self.y = 0
		self.z = c.Z+c.L	
	
	#---SEND BOX TO SIM---#
	# send white box to simulator
	def Send_To(self, sim):
		self.lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, 
										length=self.l, width=self.w, height=self.h,
									    r=1.0, g=1.0, b=1.0) 
		# fix box in place xyz space
		sim.send_hinge_joint(first_body_id=self.lightSource, second_body_id=pyrosim.Simulator.WORLD,
								x=self.x, y=self.y, z=self.z,
								n1=0, n2=0, n3=1,
							    lo=0, hi=0)
		# attatch light source to box
		sim.send_light_source(body_id = self.lightSource)
		
	#---SLOPE METHODS---#
	def Place_Slope_Front(self):
		self.slopeR1 = 0
		self.slopeR2 = -0.2
		self.slopeR3 = 1	
		self.slopeN1 = 0
		self.slopeN2 = 1
		self.slopeN3 = 0
	def Place_Slope_Back(self):
		self.slopeR1 = 0
		self.slopeR2 = 0.2
		self.slopeR3 = 1
		self.slopeN1 = 0
		self.slopeN2 = 1
		self.slopeN3 = 0	
	def Place_Slope_Right(self):
		self.slopeR1 = -0.2
		self.slopeR2 = 0
		self.slopeR3 = 1	
		self.slopeN1 = 1
		self.slopeN2 = 0
		self.slopeN3 = 0
	def Place_Slope_Left(self):
		self.slopeR1 = 0.2
		self.slopeR2 = 0
		self.slopeR3 = 1
		self.slopeN1 = 1
		self.slopeN2 = 0
		self.slopeN3 = 0
		
	#---SEND SLOPE TO SIM---#
	def Send_Slope(self, sim):
		# send slope to simulator with configurated parameters
		self.slope = sim.send_box(x=self.slopeX, y=self.slopeY, z=self.slopeZ, 
								  length=self.slopeL, width=self.slopeW, height=self.slopeH,
								  r1=self.slopeR1, r2=self.slopeR2, r3=self.slopeR3,
								  r=0.7, g=0.2, b=0.3)
		# fix slope in place xyz space
		sim.send_hinge_joint(first_body_id=self.slope, second_body_id=pyrosim.Simulator.WORLD,
								x=self.slopeX, y=self.slopeY, z=self.slopeZ,
								n1=self.slopeN1, n2=self.slopeN2, n3=self.slopeN3,
								lo=0, hi=0)
	
	#---PRINT---#	
	def Print(self):
		print("["), 
		print (self.ID),
		print("size:", self.l, self.w, self.h),
		print("position:", self.x, self.y, self.z),
		print("]")
		
#--------------------------------------------------------------------------------------------#

# environment 3 is the consistent slope environment
# the robot will perform phototaxis on a slope
# the light source will appear at different places on the slope which stays consistent
		
class ENVIRONMENT_3:
	
	#---CONSTRUCTOR---#	
	def __init__(self, i):
		# environment id
		self.ID = i
		# light box variables
		self.l = c.L
		self.w = c.L
		self.h = c.L
		self.x = 0
		self.y = 0
		self.z = 0
		# slope variables
		self.slopeL = c.L*55
		self.slopeW = c.L*55
		self.slopeH = c.L
		self.slopeX = 0
		self.slopeY = 0
		self.slopeZ = (c.L+c.R)*5
		self.slopeR1 = 0
		self.slopeR2 = 0
		self.slopeR3 = 0		
		self.slopeN1 = 0
		self.slopeN2 = 0
		self.slopeN3 = 0
	
		# set light box and slope location according to environment
		if(self.ID == 0):
			self.Place_Light_Source_To_The_Front()
			self.Place_Slope_Front()
		elif(self.ID == 1):
			self.Place_Light_Source_To_The_Back()
			self.Place_Slope_Front()
		elif(self.ID == 2):
			self.Place_Light_Source_To_The_Right()
			self.Place_Slope_Front()
		elif(self.ID == 3):
			self.Place_Light_Source_To_The_Left()
			self.Place_Slope_Front()
		else:
			self.Place_Light_Source_To_The_Front()
			self.Place_Slope_Front()
	
	#---LIGHT SOURCE METHODS---#	
	def Place_Light_Source_To_The_Front(self):
		self.x = 0
		self.y = c.L*25
		self.z = c.Z+c.L
	def Place_Light_Source_To_The_Back(self):
		self.x = 0
		self.y = -c.L*25
		self.z = c.L+c.L
	def Place_Light_Source_To_The_Right(self):
		self.x = c.L*25
		self.y = 0
		self.z = c.Z/2+c.L
	def Place_Light_Source_To_The_Left(self):
		self.x = -c.L*25
		self.y = 0
		self.z = c.Z/2+c.L
	
	#---SEND BOX TO SIM---#
	def Send_To(self, sim):
		# send white box to simulator
		self.lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, 
										length=self.l, width=self.w, height=self.h,
									    r=1.0, g=1.0, b=1.0) 
		# fix box in place xyz space
		sim.send_hinge_joint(first_body_id=self.lightSource, second_body_id=pyrosim.Simulator.WORLD,
								x=self.x, y=self.y, z=self.z,
								n1=0, n2=0, n3=1,
							    lo=0, hi=0)
		# attatch light source to box
		sim.send_light_source(body_id = self.lightSource)
		
	#---SLOPE METHODS---#
	def Place_Slope_Front(self):
		self.slopeR1 = 0
		self.slopeR2 = -0.2
		self.slopeR3 = 1	
		self.slopeN1 = 0
		self.slopeN2 = 1
		self.slopeN3 = 0
	def Place_Slope_Back(self):
		self.slopeR1 = 0
		self.slopeR2 = 0.2
		self.slopeR3 = 1
		self.slopeN1 = 0
		self.slopeN2 = 1
		self.slopeN3 = 0	
	def Place_Slope_Right(self):
		self.slopeR1 = -0.2
		self.slopeR2 = 0
		self.slopeR3 = 1	
		self.slopeN1 = 1
		self.slopeN2 = 0
		self.slopeN3 = 0
	def Place_Slope_Left(self):
		self.slopeR1 = 0.2
		self.slopeR2 = 0
		self.slopeR3 = 1
		self.slopeN1 = 1
		self.slopeN2 = 0
		self.slopeN3 = 0
		
	#---SEND SLOPE TO SIM---#
	def Send_Slope(self, sim):
		# send slope to simulator with configurated parameters
		self.slope = sim.send_box(x=self.slopeX, y=self.slopeY, z=self.slopeZ, 
								  length=self.slopeL, width=self.slopeW, height=self.slopeH,
								  r1=self.slopeR1, r2=self.slopeR2, r3=self.slopeR3,
								  r=0.2, g=0.6, b=0.3) 
		# fix slope in place xyz space
		sim.send_hinge_joint(first_body_id=self.slope, second_body_id=pyrosim.Simulator.WORLD,
								x=self.slopeX, y=self.slopeY, z=self.slopeZ,
								n1=self.slopeN1, n2=self.slopeN2, n3=self.slopeN3,
							    lo=0, hi=0)
	
	#---PRINT---#	
	def Print(self):
		print("["), 
		print (self.ID),
		print("size:", self.l, self.w, self.h),
		print("position:", self.x, self.y, self.z),
		print("]")

	
	
