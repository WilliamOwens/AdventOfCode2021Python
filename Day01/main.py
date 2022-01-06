import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input

def solution1(l):
    """Count the number of increases from given list m."""
    myArray = [1 for i in range(1, len(l)) if int(l[i]) > int(l[i - 1])]
    myCount = myArray.count(True)
    return myCount


def solution2(l):
    myNewArray = [int(l[i]) + int(l[i - 1]) + int(l[i - 2]) for i in range(2, len(l))]
    myNewCount = solution1(myNewArray)
    return myNewCount


if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))
    print(solution2(_input))