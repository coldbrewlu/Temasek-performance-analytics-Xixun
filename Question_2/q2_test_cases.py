# This script contains test cases for the moving_average function.

from moving_average import moving_average

def test_case_1():
    prices = [10, 20, 30, 40, 50]
    M = 3
    assert moving_average(prices, M) == [20.0, 30.0, 40.0]

def test_case_2():
    prices = [5, 10, 15, 20]
    M = 2
    assert moving_average(prices, M) == [7.5, 12.5, 17.5]

def test_case_3():
    prices = [100]
    M = 1
    assert moving_average(prices, M) == [100.0]

def test_case_4():
    prices = [8, 16, 24, 32]
    M = 4
    assert moving_average(prices, M) == [20.0]

def test_case_5():
    try:
        moving_average([10, 20, 30], 0)
    except ValueError as e:
        assert str(e) == "Window size M must be a positive integer and less than or equal to the length of prices."

def test_case_6():
    try:
        moving_average([10, 20, 30], 4)
    except ValueError as e:
        assert str(e) == "Window size M must be a positive integer and less than or equal to the length of prices."

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    print("All test cases passed!")
