def toRomanNumeral(s):
    numerals = {"M": 1000,"D": 500,"C": 100,"L": 50,"X": 10,"V": 5,"I": 1,"CM": 900,"CD": 400,"XC": 90,"XL": 40, "IX": 9,"IV": 4} 
    total = 0
    i = 0
    while i<len(s):
        
        if i != len(s)-1 and (s[i]+s[i+1] == "CM" or s[i]+s[i+1] == "CD" or s[i]+s[i+1] == "XC" or s[i]+s[i+1] == "XL" or s[i]+s[i+1] == "IX" or s[i]+s[i+1] == "IV" ):
            total += numerals.get(s[i]+s[i+1])
            i+=2
        else:
            total += numerals.get(s[i])
            i +=1
    return total