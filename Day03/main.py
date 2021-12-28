import os

def util(array):
    return [char for char in array]

def getBit(l, bitToSearch, mostLeast):
    zeroBit, oneBit = 0, 0
    for i in range(0, len(l)):
        if (int(l[i][bitToSearch]) == 0):
            zeroBit += 1
        else:
            oneBit += 1
    if (mostLeast == 'o2'):
        if (zeroBit > oneBit):
            return 0
    else:
        if (zeroBit <= oneBit):
            return 0
    return 1

def filterInput(l, bitNumber, oxygenOrCO2):
    bitToFind = 0
    bitToFind = getBit(l, bitNumber, oxygenOrCO2)
    filteredList = [l[i] for i in range(0, len(l)) if int(l[i][bitNumber]) == bitToFind]
    return filteredList

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

def solution2(l):
    oxygenFilteredList, co2FilteredList = l, l
    oxygenBit, co2Bit = 0, 0
    while True:
        oxygenFilteredList = filterInput(oxygenFilteredList, oxygenBit, 'o2')
        if (len(oxygenFilteredList) == 1):
            break
        oxygenBit += 1
    while True:
        co2FilteredList = filterInput(co2FilteredList, co2Bit, 'co2')
        if (len(co2FilteredList) == 1):
            break
        co2Bit += 1
    return int(oxygenFilteredList[0], 2) * int(co2FilteredList[0], 2)

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()

    print(solution1(_input))
    print(solution2(_input))
