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


#####################
# ENVIRONMENT CLASS #
#####################

class ENVIRONMENT:
	
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
		self.slopeL = c.L*20
		self.slopeW = c.L*20
		self.slopeH = c.L
		self.slopeX = 0
		self.slopeY = 0
		self.slopeZ = c.L+c.R+c.L
	
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
		self.y = c.L*30
		self.z = c.L+c.R
	def Place_Light_Source_To_The_Back(self):
		self.x = 0
		self.y = -c.L*30
		self.z = c.L+c.R
	def Place_Light_Source_To_The_Right(self):
		self.x = c.L*30
		self.y = 0
		self.z = c.L+c.R
	def Place_Light_Source_To_The_Left(self):
		self.x = -c.L*30
		self.y = 0
		self.z = c.L+c.R	
	
	#---SEND BOX TO SIM---#
	def Send_To(self, sim):
		self.lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h) 
		sim.send_light_source(body_id = self.lightSource)
		
	#---SEND SLOPE TO SIM---#
	def Send_Slope(self, sim):
		self.slope = sim.send_box(x=self.slopeX, y=self.slopeY, z=self.slopeZ, 
								  length=self.slopeL, width=self.slopeW, height=self.slopeH,
								  r1=0, r2=1, r3=1) 
	#---PRINT---#	
	def Print(self):
		print("["), 
		print (self.ID),
		print("size:", self.l, self.w, self.h),
		print("position:", self.x, self.y, self.z),
		print("]")

	
	
