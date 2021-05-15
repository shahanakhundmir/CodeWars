import roman

def test_roman_1000():
    assert roman.convert_roman_numeral(1000) == "M"
    assert roman.convert_roman_numeral(2000) == "MM"


def test_roman_500():
    assert roman.convert_roman_numeral(500) == "D"

def test_roman_100():
    assert roman.convert_roman_numeral(100) == "C"
    assert roman.convert_roman_numeral(300) == "CCC"
    assert roman.convert_roman_numeral(400) == "CD"
    assert roman.convert_roman_numeral(900) == "CM"

def test_roman_50():
    assert roman.convert_roman_numeral(50) == "L"

def test_roman_10():
    assert roman.convert_roman_numeral(10) == "X"
    assert roman.convert_roman_numeral(20) == "XX"
    assert roman.convert_roman_numeral(90) == "XC"
    assert roman.convert_roman_numeral(40) == "XL"

def test_roman_5():
    assert roman.convert_roman_numeral(5) == "V"

def test_roman_1():
    assert roman.convert_roman_numeral(1) == "I"
    assert roman.convert_roman_numeral(2) == "II"
    assert roman.convert_roman_numeral(9) == "IX"
    assert roman.convert_roman_numeral(4) == "IV"

def test_roman_to_mix():
    assert roman.convert_roman_numeral(1500) == "MD"
    assert roman.convert_roman_numeral(1600) == "MDC"
    assert roman.convert_roman_numeral(1900) == "MCM"
    assert roman.convert_roman_numeral(150) == "CL"
    assert roman.convert_roman_numeral(190) == "CXC"
    assert roman.convert_roman_numeral(1140) == "MCXL"
    assert roman.convert_roman_numeral(1145) == "MCXLV"
    assert roman.convert_roman_numeral(1149) == "MCXLIX"
    assert roman.convert_roman_numeral(1148) == "MCXLVIII"
    assert roman.convert_roman_numeral(1142) == "MCXLII"







    

