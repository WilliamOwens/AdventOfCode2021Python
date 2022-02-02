import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareDict(_input)

def prepareDict(input):
  mapDict = dict()
  for node in input:
    splitNode = node.split('-')
    if splitNode[0] in mapDict:
      mapDict[splitNode[0]].append(splitNode[1])
    else:
      mapDict[splitNode[0]] = [splitNode[1]]
    if splitNode[1] in mapDict:
      mapDict[splitNode[1]].append(splitNode[0])
    else:
      if (splitNode[0] != 'start' and splitNode[1] != 'end'):
        mapDict[splitNode[1]] = [splitNode[0]]
  return mapDict

if __name__ == "__main__":
    _input = readFile("test_input.txt")
    print(_input)