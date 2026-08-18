class IntelligentAgent:
    def __init__(self, name, performance, environment, actuators, sensors):
        self.name = name
        self.performance = performance
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors

    def display_peas(self):
        print("\n----- PEAS Representation -----")
        print("Agent:", self.name)
        print("Performance Measure:", self.performance)
        print("Environment:", self.environment)
        print("Actuators:", self.actuators)
        print("Sensors:", self.sensors)


# Different Intelligent Agents
vacuum = IntelligentAgent(
    "Vacuum Cleaner Agent",
    "Clean all rooms with minimum energy",
    "Rooms with dirt",
    "Move Left, Move Right, Suck",
    "Dirt Sensor, Location Sensor"
)

self_driving = IntelligentAgent(
    "Self Driving Car",
    "Reach destination safely and quickly",
    "Roads, Traffic, Pedestrians",
    "Steering, Brake, Accelerator",
    "Camera, GPS, Radar, LiDAR"
)

medical = IntelligentAgent(
    "Medical Diagnosis Agent",
    "Correct diagnosis with high accuracy",
    "Hospital",
    "Display diagnosis and treatment",
    "Patient symptoms, Medical reports"
)

# Menu
print("Choose an Intelligent Agent")
print("1. Vacuum Cleaner")
print("2. Self Driving Car")
print("3. Medical Diagnosis")

choice = int(input("Enter your choice: "))

if choice == 1:
    vacuum.display_peas()
elif choice == 2:
    self_driving.display_peas()
elif choice == 3:
    medical.display_peas()
else:
    print("Invalid Choice")