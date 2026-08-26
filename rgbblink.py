from time import sleep
import random
from RGB_LED import rgb_led

led = rgb_led(0,1,2)
#Main loop
for i in range(1000):
    led.show_colour((onOrOff(), onOrOff(), onOrOff()))
    sleep(0.5)
#Disable
led.show_colour((0,0,0))
