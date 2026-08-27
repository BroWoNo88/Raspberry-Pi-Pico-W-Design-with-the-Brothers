from machine import Pin, PWM
import random
from time import sleep

button = Pin(12, Pin.IN, Pin.PULL_UP)

pressed = False

while not pressed:
    if button.value() == 0:
        pressed = True

buzzer = PWM(Pin(15))
buzzer.duty_u16(32768)

class rgb_led:
  def __init__(self,pin_r=0,pin_g=1,pin_b=2,freq = 1000):
    self.r = PWM(Pin(pin_r))
    self.g = PWM(Pin(pin_g))
    self.b = PWM(Pin(pin_b))

    self.r.freq(freq)
    self.g.freq(freq)
    self.b.freq(freq)

  def show_colour(self,rgb_tuple):
    #Converts from 0-255 to 65535-0
    r,g,b = rgb_tuple
    
    r_true = r*256 + 255
    self.r.duty_u16(r_true)

    g_true = g*256 + 255
    self.g.duty_u16(g_true)

    b_true = b*256 +255
    self.b.duty_u16(b_true)

led = rgb_led(0,1,2)

def play_notes(buzzer,notes,dur,colours_r,colours_g,colours_b):
    buzzer.duty_u16(32768)
    for ii in range(len(notes)):
        buzzer.freq(notes[ii])
        led.show_colour((colours_r[ii],colours_g[ii],colours_b[ii]))
        sleep(dur[ii])
    
    buzzer.duty_u16(0)

notes = [349,392,261,392,440,523,466,440,392,349,392,261,261,261,261,294,294,329,329]
dur = [0.75,0.75,0.5,0.75,0.75,0.125,0.125,0.125,0.125,0.75,0.75,0.25,1.25,0.125,0.125,0.125,0.125,0.125,0.125]

colours_r = [random.randint(0,256) for x in range(len(notes))]
colours_g = [random.randint(0,256) for x in range(len(notes))]
colours_b = [random.randint(0,256) for x in range(len(notes))]

new_notes = []
new_dur = []

for x in notes:
    new_notes.append(x)

for y in notes:
    new_dur.append(y*1.5)

play_notes(buzzer,new_notes,dur,colours_r,colours_g,colours_b)