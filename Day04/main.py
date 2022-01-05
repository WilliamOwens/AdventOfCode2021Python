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

def checkForAllBingos(arrayOfCards):
    cardsWithBingo = []
    for i in range(0, len(arrayOfCards), 25):
        cardToCheck = arrayOfCards[i:i+25]
        if (checkForHorizontalOrVerticalBingo(cardToCheck)):
            cardsWithBingo.append(int(i/25))
    return cardsWithBingo

def solution(l, firstLast):
    arrayOfBingoNumbers = getBingoNumbers(l)
    singleArrayOfBingoCards = getBingoCardsAsSingleArray(l)
    emptyCard = [''] * len(singleArrayOfBingoCards)
    for bingoNumberCalled in range(0, len(arrayOfBingoNumbers)):
        spots = [i for i, e in enumerate(singleArrayOfBingoCards) if e == arrayOfBingoNumbers[bingoNumberCalled]]
        for j in range(0, len(spots)):
            emptyCard[spots[j]] = arrayOfBingoNumbers[bingoNumberCalled]
        didWeFindBingo = checkForAllBingos(emptyCard)
        if (len(didWeFindBingo) > 0):
            if (firstLast == 'first'):
                intArrayOfWholeCard = [int(i) for i in singleArrayOfBingoCards[(didWeFindBingo[0] * 25):((didWeFindBingo[0] * 25) + 25)]]
                intArrayOfPartialCard = [int(j) for j in emptyCard[(didWeFindBingo[0] * 25):((didWeFindBingo[0] * 25) + 25)] if len(j) > 0]
                return (sum(intArrayOfWholeCard) - sum(intArrayOfPartialCard)) * int(arrayOfBingoNumbers[bingoNumberCalled])
            elif (firstLast == 'last'):
                if (len(singleArrayOfBingoCards) > 25):
                    for k in reversed(range(0, len(didWeFindBingo))):
                        del singleArrayOfBingoCards[(didWeFindBingo[k] * 25):((didWeFindBingo[k] * 25) + 25)]
                        del emptyCard[(didWeFindBingo[k] * 25):((didWeFindBingo[k] * 25) + 25)]
                else:
                    intArrayOfWholeCard = [int(i) for i in singleArrayOfBingoCards]
                    intArrayOfPartialCard = [int(j) for j in emptyCard if len(j) > 0]
                    return (sum(intArrayOfWholeCard) - sum(intArrayOfPartialCard)) * int(arrayOfBingoNumbers[bingoNumberCalled])

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()
    
    print(solution(_input, 'first'))
    print(solution(_input, 'last'))