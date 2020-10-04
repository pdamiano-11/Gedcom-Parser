 try:                                #checks to see if the person is married.
         families.Married(index2) 
    except NameError:
        return "not married"
    else:
        marr_date = families.married(index2)
    if marr_date > birthday:
        return "Error, birthday is after marriage."
    else: 
        return marr_date 