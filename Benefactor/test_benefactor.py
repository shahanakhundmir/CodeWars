import benefactor
import pytest
'''
def test_valueNeedForAverage30():
    assert benefactor.new_avg([30], 30) == 30
    assert benefactor.new_avg([14, 30, 5, 7, 9, 11, 16], 90) == 628
    assert benefactor.new_avg([14, 30, 5, 7, 9, 11, 15], 92) == 645
'''
def test_valueLowerThanOne():
    assert benefactor.new_avg([14, 30, 5, 7, 9, 11, 15], 2) == "Error expected"


def test_floatOutputs():
    assert benefactor.new_avg([10.30, 10.30,10.30, 10.30], 10.30 ) == 11
    assert benefactor.new_avg([10.30, 10.30,10, 10.30], 10.30 ) == 11



@ pytest.mark.parametrize(
    "input, input2,  output", [([30], 30, 30 ), ([14, 30, 5, 7, 9, 11, 16], 90, 628), ([14, 30, 5, 7, 9, 11, 15], 92 , 645)]
)

def test_valueNeedForAverage30(input, input2, output):
    assert benefactor.new_avg(input, input2) == output


