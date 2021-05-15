def convert_roman_numeral(s):
  numeral = ""

  # 1000's
  m = s // 1000
  mR = s % 1000
  numeral += "M"*m
 
#500's - exclusion for 1900
  if mR// 900 == 1:
    dR = mR % 900
    numeral += "CM"
  else:
    d = mR // 500
    dR = mR % 500
    numeral += "D"*d

#100
  c = dR // 100
  cR = dR % 100
  if c == 4:
    numeral += "CD"
  else:
    numeral += "C"*c

#50
  if cR // 90 == 1:
    lR = cR % 90
    numeral += "XC"
  else:
    l = cR // 50
    lR = cR % 50
    numeral += "L"*l

#10
  x = lR // 10
  xR = lR % 10
  if x == 4:
    numeral += "XL"
  else:
    numeral += "X"*x

#5
  if xR // 9 == 1:
    vR = xR % 9
    numeral += "IX"
  else:
    v = xR // 5
    vR = xR % 5
    numeral += "V"*v

#1
  i = vR // 1
  if i == 4:
    numeral += "IV"
  else:
    numeral += "I"*i


  return numeral
  