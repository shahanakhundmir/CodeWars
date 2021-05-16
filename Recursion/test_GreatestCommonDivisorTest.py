import greatestCommonDivisor

def test_return_one():
    assert greatestCommonDivisor.mygcd(1,1) == 1

def test_smallest_into_largest():
    assert greatestCommonDivisor.mygcd(6,12) == 6

def test_no_divisible():
    assert greatestCommonDivisor.mygcd(3,2) == 1

def test_divisible_not_smallest():
    assert greatestCommonDivisor.mygcd(30,12) == 6




