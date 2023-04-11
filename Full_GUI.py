import RPi.GPIO as GPIO
from time import sleep
import tkinter as tk
import subprocess

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)

def forward():
    global temp1
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    temp1 = 1

def backward():
    global temp1
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    temp1 = 0

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def set_speed(slider_value):
    p.ChangeDutyCycle(slider_value)

def start_sensors():
    subprocess.Popen(["python", "sensor1.py"])
    subprocess.Popen(["python", "sensor2.py"])
    subprocess.Popen(["python", "sensor3.py"])

def start_camera():
    subprocess.Popen(["python", "camera.py"])

root = tk.Tk()
root.title("Thruster, Motor, Sensor and Camera GUI")

thruster_frame = tk.Frame(root)
thruster_frame.pack(side="left", fill="both", expand=True)

motor_frame = tk.Frame(root)
motor_frame.pack(side="left", fill="both", expand=True)

sensor_frame = tk.Frame(root)
sensor_frame.pack(side="right", fill="both", expand=True)

camera_frame = tk.Frame(root)
camera_frame.pack(side="right", fill="both", expand=True)

# Thruster GUI
thruster_label = tk.Label(thruster_frame, text="Thruster Control", font=("Arial", 14))
thruster_label.pack(side="top", pady=20)

thruster_forward_button = tk.Button(thruster_frame, text="Forward", command=forward)
thruster_forward_button.pack(side="top", pady=10)

thruster_backward_button = tk.Button(thruster_frame, text="Backward", command=backward)
thruster_backward_button.pack(side="top", pady=10)

thruster_stop_button = tk.Button(thruster_frame, text="Stop", command=stop)
thruster_stop_button.pack(side="top", pady=10)

# Motor GUI
motor_label = tk.Label(motor_frame, text="Motor Control", font=("Arial", 14))
motor_label.pack(side="top", pady=20)
motor_slider = tk.Scale(motor_frame, 0, to=100, orient="horizontal", command=set_speed)
motor_slider.pack(side="top", pady=10)

# Sensor and Camera GUI
sensor_label = tk.Label(sensor_frame, text="Sensor Control", font=("Arial", 14))
sensor_label.pack(side="top", pady=20)

sensor_button = tk.Button(sensor_frame, text="Start Sensors", command=start_sensors)
sensor_button.pack(side="top", pady=10)

camera_label = tk.Label(camera_frame, text="Camera Control", font=("Arial", 14))
camera_label.pack(side="top", pady=20)

camera_button = tk.Button(camera_frame, text="Start Camera", command=start_camera)
camera_button.pack(side="top", pady=10)

root.mainloop()

GPIO.cleanup()