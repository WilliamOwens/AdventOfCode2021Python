from main import solution1, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution1(_input) == 26397
    print("Passed Day 10 Part 1")
    # assert solution2(_input) == 61229
    # print("Passed Day 08 Part 2")

if __name__ == "__main__":
    test()