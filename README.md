Hexacopter Simulation with Human Detection
A sophisticated simulation system combining robotics and computer vision to detect humans using a simulated hexacopter in a PyBullet environment. The system leverages YOLOv8 for accurate human detection while maintaining smooth UAV movement and logging capabilities.

Key Features
Realistic hexacopter simulation using PyBullet physics engine
Dynamic human spawning and movement patterns
Advanced YOLOv8-based human detection system
Comprehensive logging system with tabular data storage
Smooth UAV hovering and navigation algorithms
Installation

1
Set up virtual environment

python -m venv uavenv
# Windows
uavenv\Scripts\activate
# Linux/macOS
source uavenv/bin/activate

2
Install dependencies

pip install -r requirements.txt
pip install ultralytics opencv-python pandas pybullet
Project Structure
HEX-Simulation/
├── humanoid.urdf      # Humanoid robot definition
├── hexacopter.urdf    # Hexacopter drone definition
├── main.py           # Primary simulation controller
├── hexacopter_env.py # UAV environment logic
├── people_simulation.py # Human simulation handling
├── log.txt          # Simulation results log
├── requirements.txt  # Project dependencies
└── README.md        # Documentation
Simulation Workflow

1
Initialize PyBullet environment

2
Load hexacopter model and begin hovering sequence

3
Spawn human entities with random movement patterns

4
Activate YOLOv8 detection system

5
Record simulation metrics in log.txt

6
Continue for configurable iterations (default: 100)
Expected Output
Log Format (log.txt):


Iteration People Count UAV_X UAV_Y UAV_Z
1       3           0.2     0.5     1.0
2       5           0.4     0.6     1.2
3       2           0.3     0.8     1.1
PyBullet Visualization:

Active hexacopter with camera feed
Dynamic human entities moving in environment
Real-time detection overlays
Smooth UAV movement visualization
Troubleshooting Guide
1. Missing Dependencies:


pip install ultralytics
2. Logging Issues:

Verify write permissions in project directory
Run script with elevated privileges if needed
3. Detection Problems:

Confirm hover_and_move() implementation
Validate YOLO model loading
Adjust confidence threshold (default: 0.3)
Future Development Opportunities
Implement real-time manual UAV control
Enhance detection accuracy with larger YOLO models
Develop more sophisticated human movement patterns
Add obstacle avoidance algorithms
About the Author
Aarohi Singh
MIT WPU, Pune
Specializing in AI, Machine Learning, UAV Systems, and Robotics Applications
