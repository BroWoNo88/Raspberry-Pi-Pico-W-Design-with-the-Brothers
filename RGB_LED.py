from machine import Pin, PWM

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
    
    r_true = (255 - r)*256
    self.r.duty_u16(r_true)

    g_true = (255 - g)*256
    self.g.duty_u16(g_true)

    b_true = (255 - b)*256
    self.b.duty_u16(b_true)
