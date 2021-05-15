def remove_exclamation_marks(s):
    print(s)
    #filter all chars not equal to !
    t = "".join(filter(lambda x: x!= "!", s))
    return(t)
    #return filter string

    #return "ggg"