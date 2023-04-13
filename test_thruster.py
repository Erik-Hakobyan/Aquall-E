import RPi.GPIO as GPIO
import time
import tkinter as tk

# Initialize the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Initialize the PWM signals
esc1_pwm = GPIO.PWM(11, 50)
esc2_pwm = GPIO.PWM(13, 50)
esc1_pwm.start(0)
esc2_pwm.start(0)

# Create a function to set the speed of a thruster
def set_speed(esc_pwm, duty_cycle):
    esc_pwm.ChangeDutyCycle(duty_cycle)

# Create a tkinter window and set its properties
window = tk.Tk()
window.title("T200 Thruster Control")
window.geometry("400x300")

# Create six buttons to control the direction of each thruster
forward1_button = tk.Button(window, text="Thruster 1 Forward", command=lambda: set_speed(esc1_pwm, 1900))
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=lambda: set_speed(esc1_pwm, 1100))
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=lambda: set_speed(esc1_pwm, 1500))
forward2_button = tk.Button(window, text="Thruster 2 Forward", command=lambda: set_speed(esc2_pwm, 1900))
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=lambda: set_speed(esc2_pwm, 1100))
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=lambda: set_speed(esc2_pwm, 1500))
forward1_button.pack()
backward1_button.pack()
stop1_button.pack()
forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Start the tkinter event loop
window.mainloop()

# Clean up the GPIO pins
GPIO.cleanup()