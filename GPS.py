import time
import math
import serial
import adafruit_gps

# Helper function to calculate distance between two coordinates
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    dlat, dlon = lat2_rad - lat1_rad, lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    return 2 * R * math.asin(math.sqrt(a)) * 3280.84  # Convert to feet

# Initialize USB connection
device_path = "/dev/ttyUSB0"  # Replace this with the device path you found
ser = serial.Serial(device_path, 9600, timeout=1)
gps = adafruit_gps.GPS(ser, debug=False)

# Configure GPS module
gps.send_command(b"PMTK220,100")  # Set update rate to 100ms
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")  # Enable only GPRMC and GPGGA
gps.send_command(b"PMTK301,2")  # Set to SBAS mode
gps.send_command(b"PMTK313,1")  # Enable SBAS
gps.send_command(b"PMTK397,0")  # Set Nav Speed Threshold to 0

# Initialize variables
last_lat, last_lon = None, None
total_distance = 0

while True:
    gps.update()

    if not gps.has_fix:
        print("Waiting for GPS fix...")
        continue

    if last_lat is not None and last_lon is not None:
        distance = haversine(last_lat, last_lon, gps.latitude, gps.longitude)
        total_distance += distance

    last_lat, last_lon = gps.latitude, gps.longitude
    speed_knots = gps.speed_knots if gps.speed_knots is not None else 0
    speed_fps = speed_knots * 1.68781  # Convert to feet per second

    print(f"Latitude: {gps.latitude:.6f}, Longitude: {gps.longitude:.6f}")
    print(f"Speed: {speed_fps:.2f} ft/s")
    print(f"Distance traveled: {total_distance:.2f} ft")

    time.sleep(1)
