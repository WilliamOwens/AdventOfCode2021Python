from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, 'first') == 4512
    print("Passed Day 04 Part 1")
    assert solution(_input, 'last') == 1924
    print("Passed Day 04 Part 2")

if __name__ == "__main__":
    test()