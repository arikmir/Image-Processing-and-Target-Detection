

from smbus2 import SMBus
from bme280 import BME280
import time
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559
import time
from enviroplus import gas

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

print(bme280.get_temperature())

print(bme280.get_pressure(), bme280.get_humidity())
while True:
    print(ltr559.get_lux())
    time.sleep(1)