import pybullet as p
import time

p.connect(p.GUI)
hexacopter_id = p.loadURDF("hexacopter.urdf", basePosition=[0, 0, 1])
humanoid_id = p.loadURDF("humanoid.urdf", basePosition=[2, 2, 0])

time.sleep(5)
