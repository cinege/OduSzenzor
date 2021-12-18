# import

import math
import smbus2
import bme280
import Adafruit_DHT

# constants
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)
see_level_pressure = data.pressure/math.exp(-0.00012*152) 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

#outfile
outfile = "/var/www/html/index.lighttpd.html"

# the compensated_reading class has the following attributes


# write html
content = ""
content += "Datum:<br>"
content += str(data.timestamp) + "<br>"
content += "Homerseklet kint:<br>"
content += str(data.temperature) + "<br>"
content += "Legnyomas:<br>"
content += str(see_level_pressure) + "<br>"
content += "Homerseklet bent:<br>"
content += str(temperature) + "<br>"
content += "Paratartalom bent:<br>"
content += str(humidity)

html_file= open(outfile,"w")
html_file.write(content)
html_file.close()

