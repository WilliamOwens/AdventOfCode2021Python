import os

def util(array):
    return [char for char in array]

def solution1(l):
    totalArray = [0] * len(l[0])
    finalArray = [0] * len(l[0])
    for i in range(0, len(l)):
        singleInput = util(l[i])
        for j in range(0, len(singleInput)):
            if (singleInput[j] == '1'):
                totalArray[j] += 1
    for k in range(0, len(totalArray)):
        if (int(totalArray[k]) > 500):
            finalArray[k] += 1
    gamma = int(''.join(str(e) for e in finalArray), 2)
    epsilon = int(''.join(str(f) for f in [1] * len(l[0])), 2) - gamma
    return gamma * epsilon

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()

    print(solution1(_input))
    # print(solution2(_input))