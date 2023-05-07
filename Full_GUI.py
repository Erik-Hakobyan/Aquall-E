import os
import tkinter as tk
import RPi.GPIO as GPIO
import time
os.system ("sudo pigpiod")
time.sleep(1)
import pigpio
import subprocess

in1 = 24
in2 = 23
en = 18
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)

ESC1 = 12
ESC2 = 13

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC1, 1500)
pi.set_servo_pulsewidth(ESC2, 1500)

max_value = 1700
min_value = 1300
base_value = 1500

def forward_motor():
    global temp1
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    temp1=1
    print("forward motor")

def backward_motor():
    global temp1
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    temp1=0
    print("backward motor")

def low_motor():
    p.ChangeDutyCycle(25)
    print("low")

def medium_motor():
    p.ChangeDutyCycle(50)
    print("medium")

def high_motor():
    p.ChangeDutyCycle(75)
    print("high")

def stop_motor():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    print("stop")

def exit_motor():
    GPIO.cleanup()
    root.destroy()

def start_sensors():
    subprocess.Popen(["python", "Thermo.py"])
    subprocess.Popen(["python", "Ultrasonic.py"])
    subprocess.Popen(["python", "Battery_Sensor.py"])
    subprocess.Popen(["python", "GPS.py"])

def start_camera():
    subprocess.Popen(["python", "camera.py"])

def forward_thruster():
    speed1 = max_value
    speed2 = max_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)

def backward_thruster():
    speed1 = min_value
    speed2 = min_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)

def left_thruster():
    speed1 = max_value
    speed2 = 1550
    pi.set_servo_pulsewidth(ESC1, speed2)
    pi.set_servo_pulsewidth(ESC2, speed1)

def right_thruster():
    speed1 = max_value
    speed2 = 1550
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)

def pause_thruster():
    speed1 = base_value
    speed2 = base_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)

def stop_thruster():
    pi.set_servo_pulsewidth(ESC1, 1500)
    pi.set_servo_pulsewidth(ESC2, 1500)
    pi.stop()
    os.system ("sudo killall pigpiod")
    root.destroy()

root = tk.Tk()
root.title("Sensor and Camera GUI")
root.protocol("WM_DELETE_WINDOW", stop_thruster)
root.geometry("800x800")

# Create three frames, one for each column
sensor_frame = tk.Frame(root)
sensor_frame.pack(side="left", fill="both", expand=True)

motor_frame = tk.Frame(root)
motor_frame.pack(side="left", fill="both", expand=True)

thruster_frame = tk.Frame(root)
thruster_frame.pack(side="left", fill="both", expand=True)

# Put the sensor and camera buttons in the first frame
sensor_button = tk.Button(sensor_frame, text="Start Sensors", command=start_sensors)
sensor_button.pack()

camera_button = tk.Button(sensor_frame, text="Start Camera", command=start_camera)
camera_button.pack()

# Put the motor buttons in the second frame
forward_button = tk.Button(motor_frame, text="Forward Motor", command=forward_motor)
forward_button.pack(pady=10)

backward_button = tk.Button(motor_frame, text="Backward Motor", command=backward_motor)
backward_button.pack(pady=10)

low_button = tk.Button(motor_frame, text="Low Motor", command=low_motor)
low_button.pack(pady=10)

medium_button = tk.Button(motor_frame, text="Medium Motor", command=medium_motor)
medium_button.pack(pady=10)

high_button = tk.Button(motor_frame, text="High Motor", command=high_motor)
high_button.pack(pady=10)

stop_button = tk.Button(motor_frame, text="Stop Motor", command=stop_motor)
stop_button.pack(pady=10)

exit_button = tk.Button(motor_frame, text="Exit Motor", command=exit_motor)
exit_button.pack(pady=10)

# Put the thruster buttons in the third frame
forward_button = tk.Button(thruster_frame, text="Forward ", command=forward_thruster)
forward_button.pack()

backward_button = tk.Button(thruster_frame, text="Backward Thruster", command=backward_thruster)
backward_button.pack()

left_button = tk.Button(thruster_frame, text="Move Left", command=left_thruster)
left_button.pack()

right_button = tk.Button(thruster_frame, text="Move Right", command=right_thruster)
right_button.pack()

stop_button = tk.Button(thruster_frame, text="Stop Thruster", command=stop_thruster)
stop_button.pack()

pause_button = tk.Button(thruster_frame, text="Pause Thruster", command=pause_thruster)
pause_button.pack()

root.mainloop()

