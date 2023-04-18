import os
import time
os.system ("sudo pigpiod")
time.sleep(1)
import pigpio

ESC1 = 12
ESC2 = 13

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 1500)
pi.set_servo_pulsewidth(ESC2, 1500)

max_value = 1700
min_value = 1300
base_value = 1500

def control():
    speed1 = base_value
    speed2 = base_value
    print "Controls - w to go forward, s to go backward, d to turn right, a to turn left, x to stop, stop to abort"
    while True:
        pi.set_servo_pulsewidth(ESC1, speed1)
        pi.set_servo_pulsewidth(ESC2, speed2)
        inp = raw_input()
        
        if inp == "w":
            speed1 = max_value
            speed2 = max_value
        elif inp == "s":
            speed1 = min_value
            speed2 = min_value
        elif inp == "a":
            speed1 = max_value
            speed2 = min_value
        elif inp == "d":
            speed1 = min_value
            speed2 = max_value
        elif inp = "x":
            speed1 = base_value
            speed2 = base_value
        elif inp == "stop":
            stop()
            break

control()
