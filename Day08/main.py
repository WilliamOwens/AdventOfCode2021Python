import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
  preppedData = [i.replace('| ', '').split(' ') for i in l if i != ' | ']
  return [[''.join(sorted(segment)) for segment in sublist] for sublist in preppedData]

def solution1(l):
  anotherNewArray = [segment for sublist in l for segment in sublist[10:] if (len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7)]
  return len(anotherNewArray)

def solution2(l):
  totalValue = 0
  for signal in l:
    totalValue += getOutputSum(signal[:10], signal[10:])
  return totalValue
  
def getOutputSum(signalPattern, outputPattern):
  twoLetterSignal, threeLetterSignal, fourLetterSignal, fiveLetterSignal, sixLetterSignal, sevenLetterSignal = [], [], [], [], [], []
  uniqueDict = dict()
  for i in signalPattern:
    if (len(i) == 2):
      uniqueDict[i] = '1'
      twoLetterSignal.append(i)
    elif (len(i) == 3):
      uniqueDict[i] = '7'
      threeLetterSignal.append(i)
    elif (len(i) == 4):
      uniqueDict[i] = '4'
      fourLetterSignal.append(i)
    elif(len(i) == 5):
      fiveLetterSignal.append(i)
    elif(len(i) == 6):
      sixLetterSignal.append(i)
    elif (len(i) == 7):
      uniqueDict[i] = '8'
      sevenLetterSignal.append(i)
  for i in fiveLetterSignal:
    if (len(set(i).symmetric_difference(set(twoLetterSignal[0]))) == 3):
      uniqueDict[i] = '3'
      fiveLetterSignal.remove(i)
  for i in fiveLetterSignal:
    if (len(set(i).symmetric_difference(set(fourLetterSignal[0]))) == 3):
      uniqueDict[i] = '5'
    else:
      uniqueDict[i] = '2'
  for i in sixLetterSignal:
    if(len(set(i).symmetric_difference(set(twoLetterSignal[0]))) == 6):
      uniqueDict[i] = '6'
      sixLetterSignal.remove(i)
  for i in sixLetterSignal:
    if (len(set(i).symmetric_difference(set(fourLetterSignal[0]))) == 2):
      uniqueDict[i] = '9'
    else:
      uniqueDict[i] = '0'
  runningTotal = []
  for i in outputPattern:
    runningTotal.append(uniqueDict.get(i))
  return int(''.join(runningTotal))

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution1(_input))
  print(solution2(_input))
