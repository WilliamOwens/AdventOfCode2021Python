import os

CHAR_DICT = {'[': ']', '{': '}', '<': '>', '(': ')'}
OPEN_SET = ('[', '{', '<', '(')
ILLEGAL_CHAR_TABLE = {')': 3, ']': 57, '}': 1197, '>': 25137}

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input

def solution1(l):
  newList = []
  corruptedList = []
  for line in l:
    for char in line:
      if char in OPEN_SET:
        newList.insert(0, CHAR_DICT[char])
      elif char == newList[0]:
        newList = newList[1:]
      else:
        corruptedList.append(char)
        break
  total = 0
  for illegalChar in corruptedList:
    total += ILLEGAL_CHAR_TABLE[illegalChar]
  return total

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))