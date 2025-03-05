Hexacopter Simulation with Human Detection
This project simulates a hexacopter (UAV) hovering and detecting people in a PyBullet environment using YOLOv8 for human detection. The UAV hovers and moves around while detecting and counting people dynamically.

🔹 Features
✅ Hexacopter UAV Simulation using PyBullet
✅ Dynamic People Spawning and movement
✅ YOLOv8-based Human Detection
✅ Automatic Logging of per-iteration results (log.txt) in a tabular format
✅ Smooth UAV Hovering & Movement

🔹 Installation
1️⃣ Set Up the Virtual Environment
bash
Copy
Edit
# Create a virtual environment
python -m venv uavenv

# Activate the environment
# Windows
uavenv\Scripts\activate

# Linux/macOS
source uavenv/bin/activate
2️⃣ Install Required Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If ultralytics (YOLO) is missing, install it manually:

bash
Copy
Edit
pip install ultralytics opencv-python pandas pybullet
3️⃣ Run the Simulation
bash
Copy
Edit
python main.py
🔹 File Structure
bash
Copy
Edit
📂 HEX-Simulation/
 ├── humanoid.urdf              # URDF model for humanoid (people)
 ├── hexacopter.urdf            # URDF model for the hexacopter
 ├── main.py                    # Main simulation script
 ├── hexacopter_env.py          # UAV environment logic
 ├── people_simulation.py       # People spawning and movement logic
 ├── log.txt                    # Stores per-iteration results in tabular format
 ├── requirements.txt           # Python dependencies
 ├── README.md                  # This documentation
🔹 Simulation Workflow
1️⃣ Starts PyBullet GUI and loads the environment.
2️⃣ Hexacopter takes off and starts hovering & moving.
3️⃣ People randomly spawn in the environment.
4️⃣ YOLOv8 detects people and logs their count.
5️⃣ Results are saved in log.txt (Iteration, People Count, UAV Position).
6️⃣ Simulation runs for 100 iterations (can be modified).

🔹 Expected Output
1️⃣ Log File (log.txt) Example
python-repl
Copy
Edit
Iteration   People Count    UAV_X   UAV_Y   UAV_Z
1           3              0.2     0.5     1.0
2           5              0.4     0.6     1.2
3           2              0.3     0.8     1.1
...
2️⃣ PyBullet GUI Simulation
The UAV should be hovering and moving around.
People should be dynamically appearing and being detected by YOLOv8.
The camera view should update as the UAV moves.
🔹 Troubleshooting
1️⃣ ModuleNotFoundError: No module named 'ultralytics'
Run:

bash
Copy
Edit
pip install ultralytics
Then retry:

bash
Copy
Edit
python main.py
2️⃣ log.txt is missing
Ensure the script has write permissions in the directory.
Try running the script as Administrator (Windows) or using sudo (Linux/macOS).
3️⃣ UAV Not Moving / People Not Detected
Ensure hexacopter_env.py has the hover_and_move() function implemented.
Check YOLO model is loading correctly in people_simulation.py.
Try adjusting confidence threshold in people_simulation.py:
python
Copy
Edit
self.model = YOLO("yolov8n.pt")
self.conf_threshold = 0.3  # Reduce threshold for better detections
🔹 Future Improvements
🚀 Add real-time UAV control
🚀 Improve YOLO model accuracy using larger models
🚀 Implement better person movement patterns

💡 Author
Aarohi Singh
📍 MIT WPU, Pune
🚀 AI & ML | UAV Simulations | Robotics

