import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
  return [int(i) for i in l[0].split(',')]

def makeDictOfFuelUse(maxValue):
  fuelValues = dict()
  totalFuel = 0
  for i in range (maxValue + 1):
    totalFuel += i
    fuelValues[i] = totalFuel
  return fuelValues

def solution(l, fuelUseGrows):
  dictOfFuelValues = makeDictOfFuelUse(max(l))
  minValue = sum(l) * len(l)
  for i in range(min(l), max(l)):
    totalFuelUsed = 0
    for j in range(len(l)):
      totalMovement = abs(l[j] - i)
      if (fuelUseGrows):
        totalFuelUsed += dictOfFuelValues.get(totalMovement)
      else:
        totalFuelUsed += totalMovement
    if (totalFuelUsed < minValue):
      minValue = totalFuelUsed
  return minValue

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution(_input, False))
  print(solution(_input, True))