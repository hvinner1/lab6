# Shifter class

import RPi.GPIO as GPIO
import time
global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
0b10100101, 0b10011001, 0b01000010, 0b00111100]

class Shifter():

  'Shift register class'

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT) 
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, pin):  # ping the clock or latch pin
    GPIO.output(pin,1)
    time.sleep(0)
    GPIO.output(pin,0)

  def shiftByte(self, byteVal):  # display a given byte pattern
    for i in range(8):           # 8 bits in register
      #GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
      GPIO.output(self.dataPin, byteVal & (1<<i))    # if common cathode
      self.ping(self.clockPin)
    self.ping(self.latchPin)


class LED8x8():
  
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    #self.display = display

  
  def display(self, display): 
    #self.shifter.shiftByte(pattern[num])
    while True:
      for n in range(len(pattern)):
        self.shifter.shiftByte(pattern[n])
        time.sleep(.001)
        for k in range(len(pattern)):
          self.shifter.shiftByte(k)
          time.sleep(.001)
        
        #needs to go through all rows and run the pattern, then call shiftByte a second time to call for the columns


theDisplay= LED8x8(20,23,24)
LED8x8(theDisplay)


