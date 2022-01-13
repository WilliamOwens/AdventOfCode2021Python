from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    flashes, rounds = solution(_input, 100)
    assert flashes == 1656
    print("Passed Day 11 Part 1")
    assert rounds == 195
    print("Passed Day 11 Part 2")

if __name__ == "__main__":
    test()