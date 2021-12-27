import os

VERT = {'down': 1, 'up': -1} 

def solution1(l):
    x = 0 
    y = 0
    for i in range(0, len(l)):
        directons = l[i].split()
        if(directons[0] == 'forward'):
            x += int(directons[1])
        else:
            y += (int(directons[1]) * VERT[directons[0]])
    return x * y

def solution2(l):
    x = 0 
    y = 0
    aim = 0
    for i in range(0, len(l)):
        directons = l[i].split()
        if(directons[0] == 'forward'):
            x += int(directons[1])
            if(aim > 0):
                y += (int(directons[1]) * aim)
        else:
            aim += (int(directons[1]) * VERT[directons[0]])
    return x * y


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        _input = file.read().splitlines()

    print(solution1(_input))
    print(solution2(_input))