from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("Temperature: %.2f Celsius" % temperature)