### created by Max Marder

###########
# IMPORTS #
###########

import pickle
import copy
import random
from individual import INDIVIDUAL

#---PARENT---#
#spawn single parent
parent = INDIVIDUAL()
parent.Evaluate(False)

# spawn 10 children
for i in range(0,10):
	
	#---CHILD---#
	child = copy.deepcopy(parent)
	child.Mutate()
	child.Evaluate(False)
	print "[g: ", i+1,"]", "[p: ", parent.fitness, "]", "[c: ", child.fitness, "]"
	
	# if the child's fitness is better than the parent:
	# replace parent with child
	# load new best into robot.p
	if (child.fitness > parent.fitness):
		parent = child
		#child.Evaluate(False)
		
		#---FILE I/O---#
		# open robot.p and insert the parent as best robot
		f = open('robot.p','w')
		pickle.dump(parent, f )
		f.close()