def sorted_array(A):
    if len(A)==1:
        return True
    return ( A[0]<=A[1] and sorted_array(A[1:]))

A = [1,2,3,10,5,6,7]
print (sorted_array(A) )