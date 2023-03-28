import tkinter as tk
import subprocess

def start_sensors():
    subprocess.Popen(["python", "Thermo.py"])
    subprocess.Popen(["python", "Ultrasonic.py"])
    subprocess.Popen(["python", "Battery_Sensor.py"])


def start_camera():
    subprocess.Popen(["python", "camera.py"])

root = tk.Tk()
root.title("Sensor and Camera GUI")

sensor_frame = tk.Frame(root)
sensor_frame.pack(side="left", fill="both", expand=True)

camera_frame = tk.Frame(root)
camera_frame.pack(side="right", fill="both", expand=True)

sensor_button = tk.Button(sensor_frame, text="Start Sensors", command=start_sensors)
sensor_button.pack()

camera_button = tk.Button(camera_frame, text="Start Camera", command=start_camera)
camera_button.pack()

root.mainloop()