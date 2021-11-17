import multiprocessing

print("yah")
myValue = multiprocessing.Value('i')
myArray = multiprocessing.Array('f',3)

def fn(myArray, myValue):
  for (idx,n) in enumerate([3,2,1]):
    myArray[idx] = n**2
    myValue.value = int(sum(myArray))
    print("In the process, iter={}:".format(idx))
    print(" Array: {}".format(myArray[:]))
    print(" Value: {}".format(myValue.value))

  p1 = multiprocessing.Process(target=fn, args=(myArray, myValue))

  print("Before starting process:")
  print(" Array: {}".format(myArray[:]))
  print(" Value: {}".format(myValue.value))
  
  p1.start()
  print("\n\nImmediately after starting process:")
  print(" Array: {}".format(myArray[:]))
  print(" Value: {}\n\n".format(myValue.value))
  
  p1.join()
  print("\n\nAfter completing process:")
  print(" Array: {}".format(myArray[:]))
  print(" Value: {}".format(myValue.value))