import pybullet as p
import numpy as np

class HexacopterEnv:
    def __init__(self):
        self.hexacopter = p.loadURDF("hexacopter.urdf", basePosition=[0, 0, 1])
    
    def hover_and_move(self):
        """ Makes UAV hover and move around randomly """
        x, y, z = p.getBasePositionAndOrientation(self.hexacopter)[0]
        x += np.random.uniform(-0.1, 0.1)  # Small random movement
        y += np.random.uniform(-0.1, 0.1)
        p.resetBasePositionAndOrientation(self.hexacopter, [x, y, z], [0, 0, 0, 1])
        return x, y, z  # Return UAV position
