import romanReverse

def test_roman_1000():
    assert romanReverse.toRomanNumeral("M") == 1000
    assert romanReverse.toRomanNumeral("MM") == 2000

def test_roman_500():
    assert romanReverse.toRomanNumeral("D") == 500

def test_roman_100():
    assert romanReverse.toRomanNumeral("C") == 100
    assert romanReverse.toRomanNumeral("CCC") == 300
    assert romanReverse.toRomanNumeral("CD") == 400
    assert romanReverse.toRomanNumeral("CM") == 900

def test_roman_50():
    assert romanReverse.toRomanNumeral("L") == 50

def test_roman_10():
    assert romanReverse.toRomanNumeral("X") == 10
    assert romanReverse.toRomanNumeral("XX") == 20
    assert romanReverse.toRomanNumeral("XC") == 90
    assert romanReverse.toRomanNumeral("XL") == 40

def test_roman_5():
    assert romanReverse.toRomanNumeral("V") == 5

def test_roman_1():
    assert romanReverse.toRomanNumeral("I") == 1
    assert romanReverse.toRomanNumeral("II") == 2
    assert romanReverse.toRomanNumeral("IV") == 4
    assert romanReverse.toRomanNumeral("IX") == 9

def test_roman_to_mix():
    assert romanReverse.toRomanNumeral("MD") == 1500
    assert romanReverse.toRomanNumeral("MDC") == 1600
    assert romanReverse.toRomanNumeral("MCM") == 1900
    assert romanReverse.toRomanNumeral("CL") == 150
    assert romanReverse.toRomanNumeral("CXC") == 190
    assert romanReverse.toRomanNumeral("MCXL") == 1140
    assert romanReverse.toRomanNumeral("MCXLV") == 1145
    assert romanReverse.toRomanNumeral("MCXLIX") == 1149
    assert romanReverse.toRomanNumeral("MCXLVIII") == 1148
    assert romanReverse.toRomanNumeral("MCXLII") == 1142
    