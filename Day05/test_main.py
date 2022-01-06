from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, False) == 5
    print("Passed Day 05 Part 1")
    assert solution(_input, True) == 12
    print("Passed Day 05 Part 2")

if __name__ == "__main__":
    test()