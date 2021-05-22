def booking(price):

    bookingFee = 0 

    # if price is less than £10, booking fee is 50p
    if price < 10:
        bookingFee = 0.50
    elif price <=100:
        bookingFee = price * 0.05
    else:
        bookingFee = price * 0.03

    totalPrice = price + bookingFee
    
    return totalPrice

def bookingInEuro(price):

    bookingFee = 0 

    # if price is less than £10, booking fee is 50p
    if price < 10:
        bookingFee = 0.50
    elif price <=100:
        bookingFee = price * 0.05
    else:
        bookingFee = price * 0.03

    totalPrice = price + bookingFee

    priceInEuro = round(totalPrice * 1.16, 2)
    
    return priceInEuro