from machine import Pin, PWM
from I2C_LCD import screen

#Set up the display
lcd = screen()
lcd.init()
