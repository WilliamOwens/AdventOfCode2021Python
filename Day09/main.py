import os

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return prepareData(_input)

def prepareData(l):
  return [[int(depth) for depth in line] for line in l]

def solution1(l):
  total = 0
  for i in range(0, len(l)):
    for j in range(0, len(l[i])):
      leftCheck = 10 if j == 0 else l[i][j-1]
      rightCheck = 10 if j == (len(l[i]) - 1) else l[i][j+1]
      topCheck = 10 if i == 0 else l[i-1][j]
      bottomCheck = 10 if i == (len(l) - 1) else l[i+1][j]
      if (l[i][j] < min(leftCheck, rightCheck, topCheck, bottomCheck)):
        total += (l[i][j] + 1)
  return total


if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution1(_input))