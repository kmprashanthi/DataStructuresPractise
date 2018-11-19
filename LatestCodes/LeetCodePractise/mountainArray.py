def mountain(A):
    """i = 0 
    flag = 0
    for i in range (len(A)-1):
        if A[i] < A[i+1] and flag ==0 :
            print (" 1. flag, A[i], A[i+1],i",flag, A[i], A[i+1],i)
            continue
        elif flag == 1 and A[i] > A[i+1]:
            print (" 2. flag, A[i], A[i+1],i",flag, A[i], A[i+1],i)
            continue
        elif (flag == 0 and A[i] > A[i+1]):
            print (" 3. flag, A[i], A[i+1],i",flag, A[i], A[i+1],i)
            flag = 1 
        elif ( flag == 1 and A[i] < A[i+1]) or (flag == 0 and i == len(A)-1 ):
            print (" 4. flag, A[i], A[i+1],i",flag, A[i], A[i+1],i)
            return False
    if flag == 1 :
        print (" 5. flag, A[i], A[i+1],i",flag, A[i], A[i+1],i)
        return True"""

    i = 0
    j= len(A)-1
    while ((i < len(A)-1) and (A[i]<A[i+1])):
        print ("1. A[i],A[i+1] ",A[i],A[i+1])
        i=i+1
    while (A[j]<A[j-1]) and (j > 0 ):
        print ("2. A[j],A[j-1] ",A[i],A[j-1])
        j=j+1
    if i == j and i!=0 and j!=len(A)-1:
        return True 
    else:
        return False

print (mountain([0,1,2,3,4,5,6,7,8,9]))
            
