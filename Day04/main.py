import os

def getBingoNumbers(l):
    return [i for i in l[0].split(',')]

def getBingoCardsAsSingleArray(l):
    arrayOfInputCards = [l[i].split() for i in range(2, len(l)) if len(l[i]) > 0]
    return [item for sublist in arrayOfInputCards for item in sublist]

def checkForHorizontalOrVerticalBingo(inputCard):
    for i in range(0, len(inputCard), 5):
        if (len(inputCard[i]) > 0 and len(inputCard[i+1]) > 0 and len(inputCard[i+2]) > 0 and len(inputCard[i+3]) > 0 and len(inputCard[i+4]) > 0):
            return True
    for j in range(0,5):
        if (len(inputCard[j]) > 0 and len(inputCard[j+5]) > 0 and len(inputCard[j+10]) > 0 and len(inputCard[j+15]) > 0 and len(inputCard[j+20]) > 0):
            return True
    return False

def checkForBingo(arrayOfCards):
    for i in range(0, len(arrayOfCards), 25):
        cardToCheck = arrayOfCards[i:i+25]
        if (checkForHorizontalOrVerticalBingo(cardToCheck)):
            return int(i/25)
    return 'No Bingo Found'

def solution1(l):
    arrayOfBingoNumbers = getBingoNumbers(l)
    singleArrayOfBingoCards = getBingoCardsAsSingleArray(l)
    emptyCard = [''] * len(singleArrayOfBingoCards)
    for bingoNumberCalled in range(0, len(arrayOfBingoNumbers)):
        spots = [i for i, e in enumerate(singleArrayOfBingoCards) if e == arrayOfBingoNumbers[bingoNumberCalled]]
        for j in range(0, len(spots)):
            emptyCard[spots[j]] = arrayOfBingoNumbers[bingoNumberCalled]
        didWeFindBingo = checkForBingo(emptyCard)
        if (didWeFindBingo != 'No Bingo Found'):
            intArrayOfWholeCard = [int(i) for i in singleArrayOfBingoCards[(didWeFindBingo * 25):((didWeFindBingo * 25) + 25)]]
            intArrayOfPartialCard = [int(j) for j in emptyCard[(didWeFindBingo * 25):((didWeFindBingo * 25) + 25)] if len(j) > 0]
            return (sum(intArrayOfWholeCard) - sum(intArrayOfPartialCard)) * int(arrayOfBingoNumbers[bingoNumberCalled])

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()
    
    print(solution1(_input))
    # print(solution2(_input))