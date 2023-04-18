import os
import time
os.system ("sudo pigpiod")
time.sleep(1)
import pigpio
import tkinter as tk

ESC1 = 12
ESC2 = 13

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 1500)
pi.set_servo_pulsewidth(ESC2, 1500)

max_value = 1700
min_value = 1300
base_value = 1500
# 
# def stop():
#     pi.set_servo_pulsewidth(ESC1, 1500)
#     pi.set_servo_pulsewidth(ESC2, 1500)
#     pi.stop()
#     os.system ("sudo killall pigpiod")
# 
# 
# def control():
#     speed1 = base_value
#     speed2 = base_value
#     print("Controls - w to go forward, s to go backward, d to turn right, a to turn left, x to stop, stop to abort")
#     while True:
#         pi.set_servo_pulsewidth(ESC1, speed1)
#         pi.set_servo_pulsewidth(ESC2, speed2)
#         inp = input()
#         
#         if inp == "w":
#             speed1 = max_value
#             speed2 = max_value
#         elif inp == "s":
#             speed1 = min_value
#             speed2 = min_value
#         elif inp == "a":
#             speed1 = max_value
#             speed2 = min_value
#         elif inp == "d":
#             speed1 = min_value
#             speed2 = max_value
#         elif inp == "x":
#             speed1 = base_value
#             speed2 = base_value
#         elif inp == "stop":
#             stop()
#             break
# 
# control()

def forward():
    speed1 = max_value
    speed2 = max_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)
    
def backward():
    speed1 = min_value
    speed2 = min_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)
    
def left():
    speed1 = max_value
    speed2 = min_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)

def right():
    speed1 = min_value
    speed2 = max_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)
    
def pause():
    speed1 = base_value
    speed2 = base_value
    pi.set_servo_pulsewidth(ESC1, speed1)
    pi.set_servo_pulsewidth(ESC2, speed2)
    
def stop():
    pi.set_servo_pulsewidth(ESC1, 1500)
    pi.set_servo_pulsewidth(ESC2, 1500)
    pi.stop()
    os.system ("sudo killall pigpiod")
    root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", stop)
root.geometry("400x300")

forward_button = tk.Button(root, text="Forward ", command=forward)
forward_button.pack()

backward_button = tk.Button(root, text="Backward", command=backward)
backward_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause)
pause_button.pack()

root.mainloop()