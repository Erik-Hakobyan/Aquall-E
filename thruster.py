import RPi.GPIO as GPIO
import tkinter as tk

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for the ESCs
esc1_pin = 17
esc2_pin = 18

# Set the frequency for the ESCs
freq = 50

# Initialize the GPIO pins for the ESCs
GPIO.setup(esc1_pin, GPIO.OUT)
GPIO.setup(esc2_pin, GPIO.OUT)

esc1 = GPIO.PWM(esc1_pin, freq)
esc2 = GPIO.PWM(esc2_pin, freq)

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
def set_speed1():
    speed = speed1_slider.get()
    duty_cycle = speed / 10.0 + 5.0
    esc1.start(duty_cycle)
    speed1_label.config(text="Thruster 1: {:.0f}%".format(speed))

def set_speed2():
    speed = speed2_slider.get()
    duty_cycle = speed / 10.0 + 5.0
    esc2.start(duty_cycle)
    speed2_label.config(text="Thruster 2: {:.0f}%".format(speed))

def stop_esc1():
    esc1.stop()
    GPIO.cleanup(esc1_pin)
    speed1_label.config(text="Thruster 1: 0%")

def stop_esc2():
    esc2.stop()
    GPIO.cleanup(esc2_pin)
    speed2_label.config(text="Thruster 2: 0%")

forward1_button = tk.Button(window, text="Thruster 1 Forward", command=set_speed1)
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=set_speed1)
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=stop_esc1)
forward2_button = tk.Button(window, text="Thruster 2 Forward", command=set_speed2)
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=set_speed2)
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=stop_esc2)
forward1_button.pack()
backward1_button.pack()
stop1_button.pack()
forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Start the tkinter event loop
window.mainloop()