from machine import Pin, PWM
from I2C_LCD import screen
from RGB_LED import rgb_led

def get_colour(bounds,value,inverted = False):
  if value < bounds[0] or value > bounds[-1]:
      return 'INV'
  if inverted:
    if value < bounds[1] or value > bounds[-2]:
      return 'GRN'
    elif value < bounds[2] or value > bounds[-3]:
      return 'YLW'
    else:
      return 'RED'
  else:
    if value < bounds[1] or value > bounds[-2]:
      return 'RED'
    elif value < bounds[2] or value > bounds[-3]:
      return 'YLW'
    else:
      return 'GRN'

#Set up the display
lcd = screen()
lcd.start()

#Set up the RGB LEDs
temp_led = rgb_led(3,4,5)

hum_led = rgb_led(6,7,8)
