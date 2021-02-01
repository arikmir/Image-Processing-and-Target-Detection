import socketio
from random import seed
from random import random

import time  # Sleep time
# Sensors
from bme280 import BME280  # Temperature sensor
from ltr559 import LTR559  # Light / proximity sensor
from enviroplus import gas  # Analog gas sensor
from enviroplus.noise import Noise

sio = socketio.Client()

noise = Noise()

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp


# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

@sio.event
def connect():
    print('connection established')
    presMessage()
    



@sio.event
def presMessage():
    bme280: BME280 = BME280()
    ltr559: LTR559 = LTR559()

    cpu_temps = [get_cpu_temperature()] * 5


    while(1):	
        time.sleep(1)
        amps = noise.get_amplitudes_at_frequency_ranges([(20,20000)])

        cpu_temp = get_cpu_temperature()
        # Smooth out with some averaging to decrease jitter
        cpu_temps = cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
        raw_temp = bme280.get_temperature()
        comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)


        sio.emit('psiresponse', bme280.get_pressure())
        sio.emit('tempresponse', comp_temp)
        sio.emit('humresponse', bme280.get_humidity())
        sio.emit('lightresponse', ltr559.get_lux())
        sio.emit('noiseresponse', amps[0])
        co = gas.read_all()
        co = co/1000
        sio.emit('gasresponse', gas.read_all())

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://172.20.10.3:3001')
sio.wait()



