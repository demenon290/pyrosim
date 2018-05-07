### created by Max Marder

###########
# IMPORTS #
###########

from individual import INDIVIDUAL
import copy
import random

####################
# POPULATION CLASS #
####################

class POPULATION:
	
	#---CONSTRUCTOR---#
	
	def __init__ (self, popSize):
		
		self.popSize = popSize
		self.p = {}
		
	#---INITIALIZE--#
	
	def Initialize(self):
				
		for i in range(0, self.popSize):
			self.p[i] = INDIVIDUAL(i)
	
	#---EVALUATE POPULATION---#
	
	def Evaluate(self, pb = True, pp = False):
			for i in self.p:
				self.p[i].Start_Evaluation(pb, pp)
			for i in self.p:
				self.p[i].Compute_Fitness()
				
	#---FILL FROM POPULATION---#
	
	def Fill_From(self, other):
		self.Copy_Best_From(other)
		self.Collect_Children_From(other)
		
	#---COPY BEST FROM POPULATION---#
	
	def Copy_Best_From(self, other):
		best_index = 0
		for i in range(0, len(other.p)):
			if (other.p[best_index].fitness < other.p[i].fitness):
				best_index = i
		self.p[0] = copy.deepcopy(other.p[best_index])
		
	#---COLLECT CHILDREN FROM POPULATION---#
	
	def Collect_Children_From(self, other):
		for i in range (1, len(other.p)):
			winner = other.Winner_Of_Tournament_Selection()
			self.p[i] = copy.deepcopy(winner)
			self.p[i].Mutate()
		
	#---TOURNAMENT WINNER---#
	
	def Winner_Of_Tournament_Selection(other):
		p1 = random.randint(0, len(other.p)-1)
		p2 = random.randint(0, len(other.p)-1)
		while (p1 == p2):
			p2 = random.randint(0, len(other.p)-1)
		if (other.p[p1].fitness >= other.p[p2].fitness):
			return other.p[p1]
		elif (other.p[p1].fitness < other.p[p2].fitness):
			return other.p[p2]
		else:
			print("OoPsie P00p$ie!! UwU dis is en ewror ^o^'")
	
	#---REPLACE POPULATION---#
	
	def ReplaceWith(self, other):
		for i in range(0, len(self.p)):
			if (self.p[i].fitness < other.p[i].fitness):
				self.p[i] = other.p[i]
	
	#---MUTATE POPULATION---#

	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()
					
	#---PRINT---#
	
	def Print(self):
		for i in range(0, len(self.p)):
			if (i in self.p):
				self.p[i].Print()


		
		


		