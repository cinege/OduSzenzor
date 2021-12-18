import math
import smbus2
import bme280
import Adafruit_DHT

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)
see_level_pressure = data.pressure/math.exp(-0.00012*152) 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

# the compensated_reading class has the following attributes

# write html

print("Datum:")
print(data.timestamp)
print("Homerseklet kint:")
print(data.temperature)
print("Legnyomas:")
print(see_level_pressure)
print("Homerseklet bent:")
print(temperature)
print("Paratartalom bent:")
print(humidity)
