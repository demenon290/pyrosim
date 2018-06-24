### created by Max Marder

###########
# IMPORTS #
###########

import constants as c
from environment import ENVIRONMENT


######################
# ENVIRONMENTS CLASS #
######################

class ENVIRONMENTS:

    # ---CONSTRUCTOR---#
    def __init__(self):
        self.envs = {}
        for e in range(0, c.numEnvs):
            self.envs[e] = ENVIRONMENT(e)
