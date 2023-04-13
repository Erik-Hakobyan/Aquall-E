import RPi.GPIO as GPIO
import time
import tkinter as tk

# Initialize the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Initialize the PWM signals
esc1_pwm = GPIO.PWM(12, 50)
esc2_pwm = GPIO.PWM(13, 50)
esc1_pwm.start(0)
esc2_pwm.start(0)

# Create a function to set the speed of a thruster
def set_speed(esc_pwm, speed):
    if speed > 0:
        duty_cycle = speed * 4 + 1100
    elif speed < 0:
        duty_cycle = speed * 4 + 1900
    else:
        duty_cycle = 1500
    duty_cycle = max(min(duty_cycle, 1900), 1100) # limit duty cycle to 1100-1900
    esc_pwm.ChangeDutyCycle((duty_cycle-1100)/8) # convert duty cycle to percentage

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
speed1_slider = tk.Scale(window, from_=-100, to=100, orient=tk.HORIZONTAL, label="Thruster 1 Speed")
speed2_slider = tk.Scale(window, from_=-100, to=100, orient=tk.HORIZONTAL, label="Thruster 2 Speed")
speed1_slider.pack()
speed2_slider.pack()

# Create six buttons to control the direction of each thruster
forward1_button = tk.Button(window, text="Thruster 1 Forward", command=lambda: set_speed(esc1_pwm, speed1_slider.get()))
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=lambda: set_speed(esc1_pwm, -speed1_slider.get()))
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=lambda: set_speed(esc1_pwm, 0))
forward2_button = tk.Button(window, text="Thruster 2 Forward", command=lambda: set_speed(esc2_pwm, speed2_slider.get()))
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=lambda: set_speed(esc2_pwm, -speed2_slider.get()))
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=lambda: set_speed(esc2_pwm, 0))
forward1_button.pack()
backward1_button.pack()
stop1_button.pack()
forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Define a function to update the speed labels with the current speed of each thruster
def update_speed_labels():
    speed1 = speed1_slider.get()
    speed2 = speed2_slider.get()
    speed1_label.config(text="Thruster 1: {:.0f}%".format(speed1))
    speed2_label.config(text="Thruster 2: {:.0f}%".format(speed2))
    window.after(100, update_speed_labels)

# Call the update_speed_labels() function to start updating the speed labels
update_speed_labels()

# Start the tkinter event loop
window.mainloop()
