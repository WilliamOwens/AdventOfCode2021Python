import os
def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    
    return prepareData(_input)

def prepareData(l):
  dataDict = dict()
  for i in range(len(l)):
    for j in range(len(l[i])):
      dataDict[(j,i)] = int(l[i][j])
  return dataDict

def increaseEnergyByOne(energyDict):
  for k in energyDict: energyDict[k] += 1

def resetEnergyToZero(energyDict):
  flashes = 0
  for k in energyDict:
    if energyDict[k] > 9:
      energyDict[k] = 0
      flashes += 1
  return flashes

def getIncreasedPoints(listOfKeys, energyDict):
  # Find the points to increase after the flash
  listOfPointsToIncrease = []
  for k in listOfKeys:
    if energyDict[k] > 9:
      listOfPointsToIncrease.append((k[0] - 1, k[1]))
      listOfPointsToIncrease.append((k[0] + 1, k[1]))
      listOfPointsToIncrease.append((k[0], k[1] - 1))
      listOfPointsToIncrease.append((k[0], k[1] + 1))
      listOfPointsToIncrease.append((k[0] - 1, k[1] - 1))
      listOfPointsToIncrease.append((k[0] - 1, k[1] + 1))
      listOfPointsToIncrease.append((k[0] + 1, k[1] - 1))
      listOfPointsToIncrease.append((k[0] + 1, k[1] + 1))

  # Return new points that flashed
  pointsToRerun = []
  for j in listOfPointsToIncrease:
    if (energyDict.get(j) is not None and energyDict.get(j) < 10):
      energyDict[j] += 1
      if energyDict[j] == 10:
        pointsToRerun.append(j)
  return pointsToRerun

def solution(inputDict, numberOfRounds):
  dictCopy = inputDict
  print(len(dictCopy))
  totalFlashes = 0
  totalRounds = 0
  keepIncreasing = True
  while keepIncreasing:
    totalRounds += 1
    # Increase all energy levels by 1
    increaseEnergyByOne(dictCopy)

    # Get flash points
    keysToIncrease = [k for k in dictCopy.keys() if dictCopy[k] == 10]
    while len(keysToIncrease) > 0:
      # If the flash causes more flashes, rerun until no more flashes
      keysToIncrease = getIncreasedPoints(keysToIncrease, dictCopy)

    # Reset flashes to 0 
    newFlashes = resetEnergyToZero(dictCopy)
    if (totalRounds <= numberOfRounds): totalFlashes += newFlashes
    if (newFlashes == len(inputDict)): keepIncreasing = False
  return totalFlashes, totalRounds

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution(_input, 100))