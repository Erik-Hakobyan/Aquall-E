import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

t1 = GPIO.PWM(7, 50)

t1.start(0)


t1.ChangeDutyCycle(7.5)
time.sleep(3)

try:
    while True:
        t1.ChangeDutyCycle(9.5)
        time.sleep(3)
        t1.ChangeDutyCycle(5.5)
        time.sleep(3)
        t1.ChangeDutyCycle(7.5)
        time.sleep(3)

except KeyboardInterrupt:
    print("User Cancelled")

finally:
    t1.stop()
    GPIO.cleanup()
    quit()