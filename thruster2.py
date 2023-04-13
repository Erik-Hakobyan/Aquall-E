import RPi.GPIO as GPIO
import tkinter as tk

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for the ESCs
esc2_pin = 17

# Set the frequency for the ESCs
freq = 1500

# Initialize the GPIO pins for the ESCs
GPIO.setup(esc2_pin, GPIO.OUT)
esc2 = GPIO.PWM(esc2_pin, freq)

# Create a tkinter window and set its properties
window = tk.Tk()
window.title("T200 Thruster 2 Control")
window.geometry("400x300")

# Create two labels to display the current speed of each thruster
speed2_label = tk.Label(window, text="Thruster 2: 0%")
speed2_label.pack()

# Create two sliders to control the speed of each thruster
speed2_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Thruster 2 Speed")
speed2_slider.pack()


def set_speed2():
    speed = speed2_slider.get()
    duty_cycle = speed / 10.0 + 5.0
    esc2.start(duty_cycle)
    speed2_label.config(text="Thruster 2: {:.0f}%".format(speed))

def stop_esc2():
    esc2.stop()
    GPIO.cleanup(esc2_pin)
    speed2_label.config(text="Thruster 2: 0%")

forward2_button = tk.Button(window, text="Thruster 2 Forward", command=set_speed2)
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=set_speed2)
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=stop_esc2)

forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Start the tkinter event loop
window.mainloop()