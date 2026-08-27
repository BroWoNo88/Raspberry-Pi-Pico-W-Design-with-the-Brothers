import time
from machine import Pin

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:  # Button is pressed (LOW)
        print("Button is pressed")
    else:                    # Button is not pressed (HIGH)
        print("Button is released")
    time.sleep(0.1)