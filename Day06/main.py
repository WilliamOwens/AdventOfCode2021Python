import os

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
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()
    data = prepareData(_input)
    
    print(solution(data, 80))
    print(solution(data, 256))