import math 

def new_avg(arr, newavg):

    donations = len(arr) + 1
    amountNeeded = (donations * newavg) - sum(arr)
    if amountNeeded <= 0:
        #or return null 
        return "Error expected"
    else:
        # round up to the next int
        return math.ceil(amountNeeded) 

    