# needs more optimisation, some much larger numbers timing out in Codewars

def mygcd(x, y):
    minVal = min(x,y)
    maxVal = max (x,y)

    i = 1
    while i !=minVal:
        if minVal % i == 0 and maxVal % (minVal // i) == 0:
            return minVal // i
        i += 1
    return 1