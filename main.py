import pybullet as p
import pybullet_data
import time
import pandas as pd
from people_simulation import PeopleSimulation
from hexacopter_env import HexacopterEnv

# Logging storage
log_data = []

def run_simulation():
    # Start PyBullet simulation
    physics_client = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # Initialize UAV and People simulation
    env = HexacopterEnv()
    people_sim = PeopleSimulation(physics_client)

    # Set physics step time
    time_step = 1.0 / 240.0
    p.setTimeStep(time_step)

    print("Simulation started.")

    try:
        for episode in range(100):  # Run for 100 iterations
            print(f"Iteration {episode+1} started.")

            # Reset and spawn people
            num_people = people_sim.reset()
            print(f"People detected: {num_people}")

            # Simulate UAV hovering and movement
            uav_position = env.hover_and_move()
            print(f"UAV Position: {uav_position}")

            # Log data (ensure values are captured correctly)
            log_data.append([episode+1, num_people, *uav_position])

            # Slow down for visualization
            time.sleep(0.1)

    except Exception as e:
        print(f"Simulation Error: {e}")

    finally:
        print("Simulation ended.")
        p.disconnect()

        # **Ensure log is saved even if the script crashes**
        try:
            df = pd.DataFrame(log_data, columns=["Iteration", "People Count", "UAV_X", "UAV_Y", "UAV_Z"])
            df.to_csv("log.txt", sep="\t", index=False)
            print("log.txt successfully generated.")
        except Exception as e:
            print(f"Error saving log.txt: {e}")

if __name__ == "__main__":
    run_simulation()
