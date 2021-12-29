import os

def getBingoNumbers(l):
    return [i for i in l[0].split(',')]

def getBingoCards(l):
    arrayOfInputCards = [l[i].split() for i in range(2, len(l)) if len(l[i]) > 0]
    return [arrayOfInputCards[i:(i+5)] for i in range(0, len(arrayOfInputCards), 5)]

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()
    
    arrayOfBingoNumbers = getBingoNumbers(_input)
    arrayOfBingoCards = getBingoCards(_input)

    # print(solution1(_input))
    # print(solution2(_input))