import RPi.GPIO as GPIO
import tkinter as tk

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for the ESCs
esc1_pin = 17

# Set the frequency for the ESCs
freq = 1500

# Initialize the GPIO pins for the ESCs
GPIO.setup(esc1_pin, GPIO.OUT)

esc1 = GPIO.PWM(esc1_pin, freq)

# Create a tkinter window and set its properties
window = tk.Tk()
window.title("T200 Thruster 1 Control")
window.geometry("400x300")

# Create two labels to display the current speed of each thruster
speed1_label = tk.Label(window, text="Thruster 1: 0%")
speed1_label.pack()

# Create two sliders to control the speed of each thruster
speed1_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Thruster 1 Speed")
speed1_slider.pack()

# Create six buttons to control the direction of each thruster
def set_speed1():
    speed = speed1_slider.get()
    duty_cycle = speed / 10.0 + 5.0
    esc1.start(duty_cycle)
    speed1_label.config(text="Thruster 1: {:.0f}%".format(speed))


def stop_esc1():
    esc1.stop()
    GPIO.cleanup(esc1_pin)
    speed1_label.config(text="Thruster 1: 0%")



forward1_button = tk.Button(window, text="Thruster 1 Forward", command=set_speed1)
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=set_speed1)
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=stop_esc1)

forward1_button.pack()
backward1_button.pack()
stop1_button.pack()


# Start the tkinter event loop
window.mainloop()