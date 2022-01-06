import os

def prepareData(l):
    for i in range(len(l)):
        l[i] = l[i].split(' -> ')
        for j in range(len(l[i])):
            l[i][j] = l[i][j]
    return [[(int(s[0]), int(s[1])) for s in (x.split(",") for x in line)] for line in l]

def solution(l, useDiagonals):
    points = dict()
    for i in l:
        x1, y1, x2, y2 = i[0][0], i[0][1], i[1][0], i[1][1]
        xDirection = 1 if (x1 < x2) else -1 if (x1 > x2) else 0
        yDirection = 1 if (y1 < y2) else -1 if (y1 > y2) else 0
        length = max(abs(x1 - x2), abs(y1 - y2))
        if (xDirection == 0 or yDirection == 0):
            for _ in range(length+1):
                if (x1,y1) in points:
                    points[(x1,y1)] += 1
                else:
                    points[(x1,y1)] = 1
                if (xDirection == 0):
                    y1 += (yDirection * 1)
                else:
                    x1 += (xDirection * 1)
        elif (useDiagonals):
            for _ in range(length+1):
                if (x1,y1) in points:
                    points[(x1,y1)] += 1
                else:
                    points[(x1,y1)] = 1
                x1 += (xDirection * 1)
                y1 += (yDirection * 1)
    return sum([1 for (k,v) in points.items() if v > 1])

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()

    prepared_data = prepareData(_input)
    print(solution(prepared_data, False))
    print(solution(prepared_data, True))
