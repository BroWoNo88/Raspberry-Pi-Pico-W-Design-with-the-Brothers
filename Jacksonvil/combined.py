import time
import random
from machine import Pin, PWM

button = Pin(12, Pin.IN, Pin.PULL_UP)

class rgb_led:
  def __init__(self,pin_r,pin_g,pin_b,freq = 1000):
    self.r = PWM(Pin(pin_r))
    self.g = PWM(Pin(pin_g))
    self.b = PWM(Pin(pin_b))

    self.r.freq(freq)
    self.g.freq(freq)
    self.b.freq(freq)

  def show_colour(self,rgb_tuple):
    #Converts from 0-255 to 65535-0
    r,g,b = rgb_tuple
    
    r_true = r*256
    self.r.duty_u16(r_true)

    g_true = g*256
    self.g.duty_u16(g_true)

    b_true = b*256
    self.b.duty_u16(b_true)
    
#Initialisation
led = rgb_led(0,1,2)
led1 = Pin(13, Pin.OUT)
buzzer_pin = Pin(15)
buzzer = PWM(buzzer_pin)

def play_tone(frequency, duration_ms):
    if frequency == 0:
        # Frequency of 0 means silence/rest
        buzzer.duty_u16(0)
    else:
        buzzer.freq(frequency)     # Set the tone pitch
        buzzer.duty_u16(32768)    # Set volume / 50% duty cycle
        
    time.sleep_ms(duration_ms)
    buzzer.duty_u16(0)

NOTES = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,

    'C5': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'G5': 784,
    'A5': 880,
    'B5': 988,

    'C6': 1047,
    'D6': 1175,
    'E6': 1319,
    'F6': 1397,
    'G6': 1568,
    'A6': 1760,
    'B6': 1976,
}

notes = [
    'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
    'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
    'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6'
]

#for note in notes:
#    play_tone(NOTES[note], 300)
#    time.sleep_ms(50)

while True:
    if button.value() == 0:  # Button is pressed (LOW)
        led.show_colour((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )) 
        led1.on()  
        play_tone(262, 150) 
    else:                    # Button is not pressed (HIGH)
        led.show_colour((0,0,0))
        led1.off()
    time.sleep(0.1)