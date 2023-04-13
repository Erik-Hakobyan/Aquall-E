import PyESCControl as esc
import tkinter as tk

# Initialize the ESCs with the correct channel numbers
esc1 = esc.PyESCControl(1)
esc2 = esc.PyESCControl(2)

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
forward1_button = tk.Button(window, text="Thruster 1 Forward", command=lambda: esc1.setSpeed(speed1_slider.get()/100))
backward1_button = tk.Button(window, text="Thruster 1 Backward", command=lambda: esc1.setSpeed(-speed1_slider.get()/100))
stop1_button = tk.Button(window, text="Thruster 1 Stop", command=lambda: esc1.setSpeed(0))
forward2_button = tk.Button(window, text="Thruster 2 Forward", command=lambda: esc2.setSpeed(speed2_slider.get()/100))
backward2_button = tk.Button(window, text="Thruster 2 Backward", command=lambda: esc2.setSpeed(-speed2_slider.get()/100))
stop2_button = tk.Button(window, text="Thruster 2 Stop", command=lambda: esc2.setSpeed(0))
forward1_button.pack()
backward1_button.pack()
stop1_button.pack()
forward2_button.pack()
backward2_button.pack()
stop2_button.pack()

# Define a function to update the speed labels with the current speed of each thruster
def update_speed_labels():
    speed1 = esc.getSpeed(1) * 100
    speed2 = esc.getSpeed(2) * 100
    speed1_label.config(text="Thruster 1: {:.0f}%".format(speed1))
    speed2_label.config(text="Thruster 2: {:.0f}%".format(speed2))
    window.after(100, update_speed_labels)

# Call the update_speed_labels() function to start updating the speed labels
update_speed_labels()

# Start the tkinter event loop
window.mainloop()