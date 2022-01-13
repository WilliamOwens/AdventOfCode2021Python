from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, False) == 26397
    print("Passed Day 10 Part 1")
    assert solution(_input, True) == 288957
    print("Passed Day 10 Part 2")

if __name__ == "__main__":
    test()