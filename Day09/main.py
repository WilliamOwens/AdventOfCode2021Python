import os

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return prepareData(_input)

def prepareData(l):
  return [[int(depth) for depth in line] for line in l]

def buildInputDictionary(l):
  heightMap = dict()
  for i in range(0, len(l)):
    for j in range(0, len(l[i])):
      heightMap[(i,j)] = l[i][j]
  return heightMap

def solution1(l):
  total = 0
  lowPointsDict = dict()
  for i in range(0, len(l)):
    for j in range(0, len(l[i])):
      leftCheck = 10 if j == 0 else l[i][j-1]
      rightCheck = 10 if j == (len(l[i]) - 1) else l[i][j+1]
      topCheck = 10 if i == 0 else l[i-1][j]
      bottomCheck = 10 if i == (len(l) - 1) else l[i+1][j]
      if (l[i][j] < min(leftCheck, rightCheck, topCheck, bottomCheck)):
        lowPointsDict[(i,j)] = l[i][j]
        total += (l[i][j] + 1)
  return total, lowPointsDict

def solution2(l, lowPointDictionary):
  heightMap = buildInputDictionary(l)
  listOfBasinSizes = []
  for key in lowPointDictionary.keys():
    basinSet = set()
    basinSet.add(key)
    basinSet = getBasinSize(key, heightMap, basinSet)
    listOfBasinSizes.append(len(basinSet))
  listOfBasinSizes.sort(reverse=True)
  return (listOfBasinSizes[0] * listOfBasinSizes[1] * listOfBasinSizes[2])

def getBasinSize(k, hm, startingBasinSet):
  basinSet = startingBasinSet
  if ((k[0], k[1] + 1) not in basinSet and hm.get((k[0], k[1] + 1)) is not None and hm.get((k[0], k[1] + 1)) < 9):
    basinSet.add((k[0], k[1] + 1))
    basinSet = getBasinSize((k[0], k[1] + 1), hm, basinSet)
  if ((k[0], k[1] - 1) not in basinSet and hm.get((k[0], k[1] - 1)) is not None and hm.get((k[0], k[1] - 1)) < 9):
    basinSet.add((k[0], k[1] - 1))
    basinSet = getBasinSize((k[0], k[1] - 1), hm, basinSet)
  if ((k[0] + 1, k[1]) not in basinSet and hm.get((k[0] + 1, k[1])) is not None and hm.get((k[0] + 1, k[1])) < 9):
    basinSet.add((k[0] + 1, k[1]))
    basinSet = getBasinSize((k[0] + 1, k[1]), hm, basinSet)
  if ((k[0] - 1, k[1]) not in basinSet and hm.get((k[0] - 1, k[1])) is not None and hm.get((k[0] - 1, k[1])) < 9):
    basinSet.add((k[0] - 1, k[1]))
    basinSet = getBasinSize((k[0] - 1, k[1]), hm, basinSet)
  return basinSet

if __name__ == "__main__":
  _input = readFile("input.txt")
  sol1, solutionDict = solution1(_input)
  print(sol1)
  print(solution2(_input, solutionDict))