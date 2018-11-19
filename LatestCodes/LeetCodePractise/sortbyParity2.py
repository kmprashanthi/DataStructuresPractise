def sortbyParity(A):
    odd = [] 
    i=0
    even = []
    j=0
    result = [0]*(len(A))
    print (result)
    k=0
    for num in A:
        if num % 2 ==0:
            even.append(num)
            print ('in even parity:',even)
        else:
            odd.append(num)
            print ('in odd parity:',odd)
    while (k<len(A)):
        print ('Value of K:',k)
        if k%2 == 0:
            result[k]=even[i]
            i=i+1
        else:
            result[k]=odd[j]
            j=j+1
        k=k+1
    return result

print (sortbyParity([4,2,5,7]))