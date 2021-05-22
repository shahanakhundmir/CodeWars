import productAndLcm
import pytest

def test_productAndLcm():
    assert productAndLcm.sum_differences_between_products_and_LCMs([[15,18]]) == 180
    assert productAndLcm.sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]]) == 840
    assert productAndLcm.sum_differences_between_products_and_LCMs([[1,1], [0,0], [13,91]]) == 1092
    assert productAndLcm.sum_differences_between_products_and_LCMs([[15,7], [4,5], [19,60]]) == 0
    assert productAndLcm.sum_differences_between_products_and_LCMs([[20,50], [10,10], [50,20]]) == 1890
    assert productAndLcm.sum_differences_between_products_and_LCMs([]) == 0
