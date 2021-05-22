def sum_pow_dig_seq(start, n, k):
    a =[]
    for i in range(0, k):
        r1=0
        for digit in map(int, str(start)):
            r1 += digit**n
        a.append(r1)
        start = r1

    return [h, cyc_patt_arr, patt_len, last_term]
    