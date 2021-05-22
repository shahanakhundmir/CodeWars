def sum_differences_between_products_and_LCMs(pairs):
    result = 0 
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        c =  a * b

        while a != b :
            d = max(a,b)- min(a,b)
            a = min(a,b)
            b = d
        if c==0 and a ==0:
            result += 0
        else:
            result += c - (c / a)
    return result
 