import pybullet as p
import random
import time

class PeopleSimulation:
    def __init__(self, physics_client):
        self.physics_client = physics_client
        self.people = []  # Store people object IDs
        self.max_people = 10  # Maximum people at a time

    def reset(self):
        """Resets and spawns people at random positions"""
        # Remove existing people
        for person in self.people:
            p.removeBody(person, physicsClientId=self.physics_client)
        self.people.clear()

        # Generate new random people count
        num_people = random.randint(5, self.max_people)

        for _ in range(num_people):
            x, y = random.uniform(-2, 2), random.uniform(-2, 2)
            person = p.loadURDF("humanoid.urdf", basePosition=[x, y, 0.1], physicsClientId=self.physics_client)
            self.people.append(person)

        return num_people  # Return the count of people added
