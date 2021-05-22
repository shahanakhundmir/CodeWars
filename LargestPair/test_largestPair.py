import largestPair
import pytest

'''
def test_largestSumInList():
    assert largestPair.largest_pair_sum([1,2,3,4,5]) == 9
    assert largestPair.largest_pair_sum([10,10,10]) == 20
    assert largestPair.largest_pair_sum([1,100,3,4,5]) == 105
    assert largestPair.largest_pair_sum([1,50,3,60,5]) == 110
    assert largestPair.largest_pair_sum([1,1000,3,4,5]) == 1005
'''


@ pytest.mark.parametrize(

"input, output", [([1,2,3,4,5], 9),([10,10,10], 20), ([1,100,3,4,5], 105), ([1,50,3,60,5], 110), ([1,1000,3,4,5], 1005)]
)

def test_largestSumInList(input, output):
    assert largestPair.largest_pair_sum(input) == output