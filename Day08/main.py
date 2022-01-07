import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
  return [i.replace('| ', '').split(' ') for i in l if i != ' | ']

def solution1(l):
  anotherNewArray = [segment for sublist in l for segment in sublist[10:] if (len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7)]
  return len(anotherNewArray)

  

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution1(_input))
  # print(solution(_input, True))