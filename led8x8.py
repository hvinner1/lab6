from shifter import *
global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
0b10100101, 0b10011001, 0b01000010, 0b00111100] 


class LED8x8():

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(20, 23, 24)
    #self.pattern = pattern
    #self.display = display

  
  def display(self): 
    #self.shifter.shiftByte(pattern[num])
    while True:
      for n in range(len(pattern)):
        self.shifter.shiftByte(pattern[n])
        time.sleep(.001)
        for k in range(len(pattern)):
          self.shifter.shiftByte(k)
          time.sleep(.001)
        
        #needs to go through all rows and run the pattern, then call shiftByte a second time to call for the columns



LED8x8.display(Shifter(20, 23, 24))