from machine import Pin, PWM, I2C
import time

# --- Hardware Configuration ---
# Match the pins configured inside diagram.json
class screen:
  def __init__(self, num = 0, sda = 0, scl = 1, freq=400000):
    self.i2c = I2C(num, sda=Pin(sda), scl=Pin(scl), freq=freq)
    self.I2C_ADDR = self.i2c.scan()[0]  # Default address for the Wokwi I2C LCD component
  # --- LCD Bitmasks ---
    self.En = 0b00000100        # Enable bit (Clock trigger pin)
    self.Rs = 0b00000001        # Register Select bit (0 = Command, 1 = Data)
    self.Backlight = 0b00001000 # Pin mask to keep the panel illuminated
  
  def lcd_strobe(self,data):
      """Pulses the Enable pin to clock data into the HD44780."""
      # Write initial data state with backlight on
      self.i2c.writeto(self.I2C_ADDR, bytes([data | self.Backlight]))
      # Pull Enable HIGH
      self.i2c.writeto(self.I2C_ADDR, bytes([data | self.En | self.Backlight]))
      # Pull Enable LOW
      self.i2c.writeto(self.I2C_ADDR, bytes([(data & ~self.En) | self.Backlight]))
  
  def lcd_send_byte(self,bits, mode):
      """Splits an 8-bit byte into 4-bit nibbles for the hardware."""
      high_nibble = mode | (bits & 0xF0)
      low_nibble = mode | ((bits << 4) & 0xF0)
      
      self.lcd_strobe(high_nibble)
      self.lcd_strobe(low_nibble)
  
  def lcd_init(self):
      """Wakes the display up in 4-bit operational mode."""
      time.sleep_ms(50)
      self.lcd_strobe(0x03 << 4)
      time.sleep_ms(5)
      self.lcd_strobe(0x03 << 4)
      time.sleep_ms(5)
      self.lcd_strobe(0x03 << 4)
      time.sleep_ms(1)
      self.lcd_strobe(0x02 << 4) # Set to 4-bit mode
      
      # Configure display rules
      self.lcd_send_byte(0x28, 0) # Function Set: 4-bit, 2 lines, 5x8 font
      self.lcd_send_byte(0x0C, 0) # Display Control: Display ON, Cursor OFF
      self.lcd_send_byte(0x06, 0) # Entry Mode: Increment cursor right
      self.lcd_send_byte(0x01, 0) # Clear Display command
      time.sleep_ms(5)
  
  def lcd_display_line(self,string, line):
      """Maps the display target line to row DDRAM matrix addresses."""
      if line == 1:
          self.lcd_send_byte(0x80, 0) # Row 1 Start Address
      elif line == 2:
          self.lcd_send_byte(0xC0, 0) # Row 2 Start Address
          
      for char in string:
          self.lcd_send_byte(ord(char), self.Rs)
  
  def lcd_display(self,str):
    line1, line2 = str.split('\n')
    self.lcd_display_line(line1,1)
    self.lcd_display_line(line2,2)
