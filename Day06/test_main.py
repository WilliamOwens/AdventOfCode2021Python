from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, 80) == 5934
    print("Passed Day 06 Part 1")
    assert solution(_input, 256) == 26984457539
    print("Passed Day 06 Part 2")

if __name__ == "__main__":
    test()