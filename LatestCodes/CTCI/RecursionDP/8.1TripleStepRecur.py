def trippleStep (n):
    print ("value now :",n)
    if n < 0:
        return 0  #return 0 as that particular step is not involved 
    elif n == 0:
        return 1 # you are able to reach that step
    else :
        return trippleStep(n-1)+trippleStep(n-2)+trippleStep(n-3)

print (trippleStep(3))