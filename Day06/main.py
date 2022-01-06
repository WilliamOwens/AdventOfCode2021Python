import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
    return [int(i) for i in l[0].split(',')]

def solution(l, days):
    totalFish = [l.count(x) for x in range(9)]
    for _ in range(days):
        newFish = totalFish[0]
        totalFish = totalFish[1:] + [newFish]
        totalFish[6] += newFish
    return sum(totalFish)

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution(_input, 80))
    print(solution(_input, 256))