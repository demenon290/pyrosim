### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import copy
import random
from population import 
#---PARENT---#
# spawn single parent
parent = INDIVIDUAL()
parent.Evaluate(True)

# spawn 500 children and choose who's best
for i in range(0,500):
	
	#---CHILD---#
	child = copy.deepcopy(parent)
	geneToMutate = child
	child.Mutate()
	child.Evaluate(True)
	print "[g: ", i+1,"]", "[pw: ", parent.genome, "]" "[p: ", parent.fitness, "]", "[c: ", child.fitness, "]"
	
	# if the child's fitness is better than the parent:
	# replace parent with child
	# load new best into robot.p
	if (child.fitness > parent.fitness):
		parent = child
		child.Evaluate(True)
		
		#---FILE I/O---#
		# open robot.p and insert the parent as best robot
#		f = open('robot.p','w')
#		pickle.dump(parent, f )
#		f.close()