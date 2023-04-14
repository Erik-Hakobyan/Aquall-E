import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

left = GPIO.PWM(12, 50) # GPIO pin 12, 50Hz frequency
left.start(7.5) # start PWM at 0% duty cycle

right = GPIO.PWM(16, 50) # GPIO pin 16, 50Hz frequency
right.start(7.5) # start PWM at 0% duty cycle

def forward_left():
    left.ChangeDutyCycle(9.5)
def backward_left():
    left.ChangeDutyCycle(5.5)
def stop_left():
    left.ChangeDutyCycle(7.5)

def forward_right():
    right.ChangeDutyCycle(9.5)
def backward_right():
    right.ChangeDutyCycle(5.5)
def stop_right():
    right.ChangeDutyCycle(7.5)

def on_closing():
    stop_left()
    stop_right()
    time.sleep(1)
    root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("400x300")

forward1_button = tk.Button(root, text="Forward Left", command=forward_left)
forward1_button.pack()

backward1_button = tk.Button(root, text="Backward Left", command=backward_left)
backward1_button.pack()

stop1_button = tk.Button(root, text="Stop Left", command=stop_left)
stop1_button.pack()

forward2_button = tk.Button(root, text="Forward Right", command=forward_right)
forward2_button.pack()

backward2_button = tk.Button(root, text="Backward Right", command=backward_right)
backward2_button.pack()

stop2_button = tk.Button(root, text="Stop Right", command=stop_right)
stop2_button.pack()

root.mainloop()

left.stop() 
right.stop() 
GPIO.cleanup() 