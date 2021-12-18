# import
import math, smbus2, bme280, Adafruit_DHT
from datetime import datetime

# constants
logfile = "/home/pi/sensors/sensorlog"
port = 1
address = 0x76

# calculated
now = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
with open(logfile,"a") as logfilehandle:
        logfilehandle.write("\n")
        logfilehandle.write(now + " data fetching...")
	logfilehandle.flush()

bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)
day = datetime.now().date().strftime("%Y.%m.%d")
see_level_pressure = data.pressure/math.exp(-0.00012*152)
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

newtemp = str(round(data.temperature,1))
if newtemp == "-0.0":
        newtemp = "0.0"

line = now + ","
line += newtemp + ","
line += str(round(see_level_pressure,1)) + ","
line += str(round(temperature,1)) + ","
line += str(round(humidity,1))

file  = "/home/pi/sensors/data/" + day
with open(file,"a") as filehandle:
	filehandle.write("\n")
	filehandle.write(line)
	filehandle.flush()
