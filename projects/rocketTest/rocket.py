### created by Max Marder

import math

###########
# IMPORTS #
###########
import constants as c


###############
# ROBOT CLASS #
###############

class ROCKET:

    # ---CONTRUCTOR---#
    def __init__(self, sim, wts):

        # Initialize components
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

        # Delete dictionaries
        del self.thrusters
        del self.S
        del self.SN
        del self.MN

    # ---METHODS---#
    def send_objects(self, sim):
        # set up fuselage
        self.main_body = sim.send_cylinder(x=0, y=0, z=c.MAIN_HEIGHT + c.MAIN_WIDTH,
                                           r=1, g=0, b=0,
                                           r1=0, r2=0, r3=1,
                                           length=c.MAIN_HEIGHT, radius=c.MAIN_WIDTH,
                                           mass=100)
        # make thruster cylinders
        self.side_cyls = [0] * c.NUM_THRUSTERS
        for i in range(c.NUM_THRUSTERS):
            x = math.cos(2 * math.pi / float(c.NUM_THRUSTERS) * i) * c.MAIN_WIDTH
            y = math.sin(2 * math.pi / float(c.NUM_THRUSTERS) * i) * c.MAIN_WIDTH

            self.side_cyls[i] = sim.send_cylinder(x, y, c.MAIN_HEIGHT / 3.0 + c.MAIN_WIDTH,
                                                  r1=0, r2=0, r3=1,
                                                  length=c.MAIN_HEIGHT / 3.0,
                                                  radius=c.MAIN_WIDTH / 3.0)

    def send_joints(self, sim):
        # make thrusters dictionary
        self.thrusters = {}
        for i in range(c.NUM_THRUSTERS):
            # thrusters are attached to a body and apply a
            # directional force (x,y,z) based on the value of
            # the attached motor neuron. The effect of the force
            # on the body depends on the lo and hi parameters
            # and the total mass of the bodies attached.
            # Currently the thrusters only apply force to the
            # center of mass of the attached body.
            self.thrusters[i] = sim.send_thruster(self.side_cyls[i],
                                                  x=0, y=0, z=-1,
                                                  lo=0, hi=40)
            # fix side cylinders to fuselage
            sim.send_fixed_joint(self.main_body, self.side_cyls[i])

    def send_sensors(self, sim):
        # central light sensor
        self.lightSensor = sim.send_light_sensor(body_id=self.main_body)
        # vestibular sensor
        self.vestSensor = sim.send_vestibular_sensor(body_id=self.main_body)
        # position sensor
        self.posSensor = sim.send_position_sensor(body_id=self.main_body)
        # touch sensors
        self.T0 = sim.send_touch_sensor(body_id=self.thrusters[0])
        self.T1 = sim.send_touch_sensor(body_id=self.thrusters[1])
        self.T2 = sim.send_touch_sensor(body_id=self.thrusters[2])
        self.T3 = sim.send_touch_sensor(body_id=self.thrusters[3])

        # create sensor dictionary
        self.S = {}
        # fill sensor dictionary
        self.S[0] = self.lightSensor
        self.S[1] = self.T0
        self.S[2] = self.T1
        self.S[3] = self.T2
        self.S[4] = self.T3


    def send_neurons(self, sim):
        ## SENSOR NEURONS
        # create sensor neuron dictionary
        self.SN = {}
        # add sensor neurons to sensors
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])

        ## MOTOR NEURONS
        # create motor neuron dictionary
        self.MN = {}
        for t in self.thrusters:
            self.MN[t] = sim.send_motor_neuron(joint_id=self.thrusters[t], tau=0.3)

    def send_synapses(self, sim, wts):
        # wire SN0 and T0-T3 to MN0-MN3
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j, i])


'''
REFERENCE CODE

# network consists of sin input neuron connected to thrusters
fnueron = sim.send_function_neuron(math.sin)

for i in range(NUM_THRUSTERS):
    x = math.cos(2*math.pi/float(NUM_THRUSTERS)*i)*MAIN_WIDTH
    y = math.sin(2*math.pi/float(NUM_THRUSTERS)*i)*MAIN_WIDTH

    self.side_cyls[i] = sim.send_cylinder(x, y, MAIN_HEIGHT/3.0+MAIN_WIDTH,
                                     r1=0, r2=0, r3=1,
                                     length=MAIN_HEIGHT/3.0,
                                     radius=MAIN_WIDTH/3.0)
    sim.send_fixed_joint(main_body, side_cyls[i])

    # thrusters are attached to a body and apply a
    # directional force (x,y,z) based on the value of
    # the attached motor neuron. The effect of the force
    # on the body depends on the lo and hi parameters
    # and the total mass of the bodies attached.
    # Currently the thrusters only apply force to the
    # center of mass of the attached body.
    thrusters[i] = sim.send_thruster(side_cyls[i],
                                     x=0, y=0, z=-1,
                                     lo=0, hi=40)

    mneuron[i] = sim.send_motor_neuron(thrusters[i])
    sim.send_synapse(fnueron, mneuron[i], 1.0)
'''
