# Hexacopter Simulation with Human Detection  

This project simulates a hexacopter (UAV) in a PyBullet environment, detecting and counting people dynamically using YOLOv8. The UAV hovers and moves while continuously identifying humans in the scene.  

## 🔹 Features  
✅ Hexacopter UAV simulation in PyBullet  
✅ Dynamic people spawning and movement  
✅ YOLOv8-based human detection  
✅ Automatic logging of detection results in `log.txt`  
✅ Smooth UAV hovering and movement  

## 🔹 Installation  

### 1️⃣ Set Up the Virtual Environment  
```bash
# Create a virtual environment
python -m venv uavenv  

# Activate the environment
# On Windows
uavenv\Scripts\activate  

# On Linux/macOS
source uavenv/bin/activate  
```

### 2️⃣ Install Required Dependencies  
```bash
pip install -r requirements.txt
```
If `ultralytics` (YOLO) is missing, install it manually:  
```bash
pip install ultralytics opencv-python pandas pybullet  
```

### 3️⃣ Run the Simulation  
```bash
python main.py  
```

## 🔹 File Structure  
```
📂 HEX-Simulation/  
├── humanoid.urdf          # URDF model for humanoid (people)  
├── hexacopter.urdf        # URDF model for the hexacopter  
├── main.py                # Main simulation script  
├── hexacopter_env.py      # UAV environment logic  
├── people_simulation.py   # People spawning and movement logic  
├── log.txt                # Stores per-iteration results in tabular format  
├── requirements.txt       # Python dependencies  
├── README.md              # Documentation  
```

## 🔹 Simulation Workflow  
1️⃣ Starts PyBullet GUI and loads the environment.  
2️⃣ Hexacopter takes off and begins hovering and moving.  
3️⃣ People randomly spawn in the environment.  
4️⃣ YOLOv8 detects people and logs their count.  
5️⃣ Results are saved in `log.txt` (Iteration, People Count, UAV Position).  
6️⃣ The simulation runs for 100 iterations (modifiable).  

## 🔹 Expected Output  

### 1️⃣ Log File (`log.txt`) Example:  
```
Iteration   People Count   UAV_X   UAV_Y   UAV_Z  
1           3             0.2     0.5     1.0  
2           5             0.4     0.6     1.2  
3           2             0.3     0.8     1.1  
...
```

### 2️⃣ PyBullet GUI Simulation  
- The UAV hovers and moves around.  
- People dynamically appear and are detected by YOLOv8.  
- The camera view updates as the UAV moves.  

## 🔹 Troubleshooting  

### 1️⃣ `ModuleNotFoundError: No module named 'ultralytics'`  
Run:  
```bash
pip install ultralytics
```
Then retry:  
```bash
python main.py  
```

### 2️⃣ `log.txt` is Missing  
- Ensure the script has write permissions in the directory.  
- Try running the script as Administrator (Windows) or using `sudo` (Linux/macOS).  

### 3️⃣ UAV Not Moving / People Not Detected  
- Ensure `hexacopter_env.py` has the `hover_and_move()` function implemented.  
- Verify that the YOLO model loads correctly in `people_simulation.py`.  
- Try adjusting the confidence threshold in `people_simulation.py`:  
```python
self.model = YOLO("yolov8n.pt")  
self.conf_threshold = 0.3  # Reduce threshold for better detections  
```

## 🔹 Future Improvements 🚀  
✅ Real-time UAV control  
✅ Improved YOLO model accuracy using larger models  
✅ Enhanced movement patterns for spawned people  

---  
💡 **Author:** Aarohi Singh  
📍 **MIT WPU, Pune**  
🚀 **AI & ML | UAV Simulations | Robotics**
