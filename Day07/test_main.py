from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, False) == 37
    print("Passed Day 07 Part 1")
    assert solution(_input, True) == 168
    print("Passed Day 07 Part 2")

if __name__ == "__main__":
    test()