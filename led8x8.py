from shifter import Shifter
import time
global pattern
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
0b10100101, 0b10011001, 0b01000010, 0b00111100] 


class LED8x8():

  #pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self):
    #self.shifter = Shifter(data, latch, clock)
    #self.pattern = pattern
    #self.display = display
    self.data, self.latch, self.clock = 20,23,24
    self.shift1 = Shifter(self.data, self.latch, self.clock)
    self.pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  
  def display(self): 
    #self.shifter.shiftByte(pattern[num])
    for n in range(len(pattern)):
      self.shift1.shiftByte(self.pattern[n]) #maybe need tilda and mask &
      self.shift1.shiftByte(1 << (n))
      self.shift1.latch()

    '''while True:
      for n in range(len(pattern)):
        self.shifter.shiftByte(pattern[n])
        time.sleep(.001)
        for k in range(len(pattern)):
          self.shifter.shiftByte(k)
          time.sleep(.001)'''
        
        #needs to go through all rows and run the pattern, then call shiftByte a second time to call for the columns

theDisplay = LED8x8()

while True:
  theDisplay.display()
  time.sleep(.001)

#((~(self.pattern[i]))&(0b11111111))