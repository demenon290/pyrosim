


import pyrosim

sim = pyrosim.Simulator(play_paused = True, eval_time = 1000)

whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)
redObject = sim.send_cylinder(x=-0.0, y=0.5, z=1.1, length=1.0, radius=0.1,
							  r1=0, r2=1, r3=0,
							  r=1, g=0, b=0)

sim.start()
whiteObject = sim.send_cylinder(x = 0, y = 0, z = 0.6, length = 1.0, radius = 0.1)