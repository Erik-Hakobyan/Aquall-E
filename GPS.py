import serial
import adafruit_gps
import time

# Set up the serial connection to the GPS module.
# Replace '/dev/ttyUSB0' with the path to the serial device for your GPS module.
gps = adafruit_gps.GPS(serial.Serial('/dev/ttyUSB0', baudrate=9600))

# Set up the GPS module settings.
# These values are specific to the Adafruit Ultimate GPS module.
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b'PMTK220,1000')

# Initialize variables to store the current and previous latitude and longitude.
prev_lat = 0
prev_lon = 0
curr_lat = 0
curr_lon = 0

# Initialize a variable to store the total distance traveled.
total_distance = 0

# Main loop to retrieve data from the GPS module and print it to the console.
while True:
    # Update the GPS module information.
    gps.update()

    # Check if the GPS module has a fix.
    if not gps.has_fix:
        # Try again if we don't have a fix yet.
        continue

    # Store the previous latitude and longitude.
    prev_lat = curr_lat
    prev_lon = curr_lon

    # Store the current latitude and longitude.
    curr_lat = gps.latitude
    curr_lon = gps.longitude

    # Calculate the distance traveled since the last update.
    distance = gps.calculate_distance(prev_lat, prev_lon, curr_lat, curr_lon)

    # Add the distance traveled to the total distance.
    total_distance += distance

    # Calculate the speed based on the distance traveled and the time elapsed.
    # The time elapsed is assumed to be 1 second, since the updates are printed every second.
    speed = distance / 1

    # Print out the current latitude and longitude, distance traveled, and speed.
    print(f'Latitude: {curr_lat}')
    print(f'Longitude: {curr_lon}')
    print(f'Distance traveled: {total_distance}')
    print(f'Speed: {speed}')

    # Wait for 1 second before printing the next update.
    time.sleep(1)