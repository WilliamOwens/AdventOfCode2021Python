from main import solution1, solution2, readFile

def test():
    _input = readFile("test_input.txt")
    sol, dict = solution1(_input)
    assert sol == 15
    print("Passed Day 08 Part 1")
    assert solution2(_input, dict) == 1134
    print("Passed Day 08 Part 2")

if __name__ == "__main__":
    test()