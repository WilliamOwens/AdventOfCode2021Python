from main import solution1, solution2, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution1(_input) == 26
    print("Passed Day 08 Part 1")
    assert solution2(_input) == 61229
    print("Passed Day 08 Part 2")

if __name__ == "__main__":
    test()