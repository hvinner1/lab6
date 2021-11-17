from shifter import Shifter
import time
import multiprocessing
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
    #self.pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]. #for smiley face
    self.myArray= multiprocessing.Array('i',8)
    self.myArray[0],self.myArray[1],self.myArray[2],self.myArray[3],self.myArray[4],self.myArray[5],self.myArray[6],self.myArray[7] = 0b00000001, 0b00000010,0b00000100,0b00001000,0b00010000,0b00100000,0b01000000,0b10000000
    self.pattern = [0b00000001, 0b00000010,0b00000100,0b00001000,0b00010000,0b00100000,0b01000000,0b10000000]
    #self.p1 = multiprocessing.Process(target=self.display, args=(row,col))
    self.p1.daemon = True
    self.p1.start()

  
  def display(self, row, col): 

    self.shift1.shiftByte((~(self.pattern[col]))&(0b11111111)) #maybe need tilda and mask &
    self.shift1.shiftByte(1 << (row))
    self.shift1.latch()

    
  

theDisplay = LED8x8()

#while True:
  #theDisplay.display(row,col)
  #time.sleep(.001)
