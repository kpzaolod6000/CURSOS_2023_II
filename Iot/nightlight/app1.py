import time 
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_relay import GroveRelay

CounterFitConnection.init('127.0.0.1', 5000)

umbral = 700
light_sensor=GroveLightSensor(0)
led = GroveLed(5)
relay=GroveRelay(1)

while True:
    light = light_sensor.light
    
    if light > umbral:
        relay.on()
        umbral = 350
    else:
        led.on()
        
    if umbral == 350:
        led.off()
    else:
        relay.off()
        umbral = 700

    time.sleep(5)
