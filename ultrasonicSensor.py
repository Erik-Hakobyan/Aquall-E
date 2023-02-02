import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the TRIG and ECHO pins
TRIG = 23
ECHO = 24

# Set the TRIG pin as an output, and the ECHO pin as an input
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    # Set the TRIG pin to LOW for 2us
    GPIO.output(TRIG, False)
    time.sleep(0.00002)

    # Send a 10us pulse on the TRIG pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the ECHO pin to go high, and measure the time it took for it to go low again
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    # Calculate the distance from the time it took for the pulse to travel
    duration = end - start
    distance = (duration * 34300) / 2

    # Print the distance
    print("Distance: {} cm".format(distance))
    time.sleep(1)

# Reset the GPIO settings
GPIO.cleanup()