import concertBooking
import pytest


@ pytest.mark.parametrize(
    "input, expected", [(9, 9.50), (0,0.50), (9.20, 9.70), (10,10.50), (50, 52.50), (100, 105),(101, 104.03),
    (200, 206), (500, 515)]
)
def test_priceGBP(input, expected ):
    assert concertBooking.booking(input) == expected



def test_priceBelow10Euro():
    assert concertBooking.bookingInEuro(9) == 11.02
    
def test_priceFrom10to100Euro():
    assert concertBooking.bookingInEuro(10) == 12.18
    
def test_priceOver100Euro():
    assert concertBooking.bookingInEuro(101) == 120.67






