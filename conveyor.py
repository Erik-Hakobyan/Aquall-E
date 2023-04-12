import RPi.GPIO as GPIO          
from time import sleep
import tkinter as tk

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
    temp1=1
    print("forward")

def backward():
    global temp1
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    temp1=0
    print("backward")

def low():
    p.ChangeDutyCycle(25)
    print("low")

def medium():
    p.ChangeDutyCycle(50)
    print("medium")

def high():
    p.ChangeDutyCycle(75)
    print("high")

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    print("stop")

def exit():
    GPIO.cleanup()
    window.destroy()

window = tk.Tk()
window.title("Motor Control")
window.geometry("300x300")

forward_button = tk.Button(window, text="Forward", command=forward)
forward_button.pack(pady=10)

backward_button = tk.Button(window, text="Backward", command=backward)
backward_button.pack(pady=10)

low_button = tk.Button(window, text="Low", command=low)
low_button.pack(pady=10)

medium_button = tk.Button(window, text="Medium", command=medium)
medium_button.pack(pady=10)

high_button = tk.Button(window, text="High", command=high)
high_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=exit)
exit_button.pack(pady=10)

window.mainloop()