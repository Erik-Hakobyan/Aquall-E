import RPi.GPIO as GPIO
import time
import tkinter as tk

# Initialize the ESCs with the correct channel numbers
ESC1_CHANNEL = 13
ESC2_CHANNEL = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(ESC1_CHANNEL, GPIO.OUT)
GPIO.setup(ESC2_CHANNEL, GPIO.OUT)

esc1 = GPIO.PWM(ESC1_CHANNEL, 50)
esc2 = GPIO.PWM(ESC2_CHANNEL, 50)

esc1.start(0)
esc2.start(0)

# Create a tkinter window and set its properties
window = tk.Tk()
window.title("T200 Thruster Control")
window.geometry("400x300")

# Create two labels to display the current speed of each thruster
speed1_label = tk.Label(window, text="Thruster 1: 0%")
speed2_label = tk.Label(window, text="Thruster 2: 0%")
speed1_label.pack()
speed2_label.pack()

# Create two sliders to control the speed of each thruster
speed1_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Thruster 1 Speed")
speed2_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Thruster 2 Speed")
speed1_slider.pack()
speed2_slider.pack()

# Create six buttons to control the direction of each thruster
def set_speed1(speed):
    duty_cycle = speed * 2 + 50
    esc1.ChangeDutyCycle(duty_cycle)
    speed1_label.config(text="Thruster 1: {:.0f}%".format(speed))

def set_speed2(speed):
    duty_cycle = speed * 2 + 50
    esc2.ChangeDutyCycle(duty_cycle)
    speed2_label.config(text="Thruster 2: {:.0f}%".format(speed))

speed1_slider.bind("<B1-Motion>", lambda event: set_speed1(speed1_slider.get()))
speed2_slider.bind("<B1-Motion>", lambda event: set_speed2(speed2_slider.get()))

forward1_button = tk.Button(window, text="Thruster 1 Forward", command=lambda: set_speed1(100))
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=lambda: set_speed1(0))
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=lambda: set_speed1(50))
forward2_button = tk.Button(window, text="Thruster 2 Forward", command=lambda: set_speed2(100))
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=lambda: set_speed2(0))
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=lambda: set_speed2(50))
forward1_button.pack()
backward1_button.pack()
stop1_button.pack()
forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Start the tkinter event loop
window.mainloop()
