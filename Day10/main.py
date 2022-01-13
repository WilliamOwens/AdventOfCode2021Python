import os

CHAR_DICT = {'[': ']', '{': '}', '<': '>', '(': ')'}
OPEN_SET = ('[', '{', '<', '(')
ILLEGAL_CHAR_TABLE = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_SET_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input

def getIncompleteLinesScore(incompleteLinesList):
  totalScore = []
  for i in incompleteLinesList:
    lineScore = 0
    for char in i:
      lineScore *= 5
      lineScore += INCOMPLETE_SET_SCORE[char]
    totalScore.append(lineScore)
  totalScore.sort()
  return totalScore[int(len(totalScore) / 2)]


def solution(l, incompleteLinesBoolean):
  corruptedList = []
  incompleteLines = []
  for line in l:
    newList = []
    for char in line:
      if char in OPEN_SET:
        newList.insert(0, CHAR_DICT[char])
      elif char == newList[0]:
        newList = newList[1:]
      else:
        corruptedList.append(char)
        newList = []
        break
    if len(newList) > 0:
      incompleteLines.append(newList)
  total = 0
  for illegalChar in corruptedList:
    total += ILLEGAL_CHAR_TABLE[illegalChar]
  incompleteLinesScore = getIncompleteLinesScore(incompleteLines)
  if (incompleteLinesBoolean):
    return incompleteLinesScore
  return total

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution(_input, False))
    print(solution(_input, True))