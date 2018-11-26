def minMove(A):    
    move =0
    if len(A) == 1 or isUnique(A):
        return 0
    A.sort()
    i=1
    while( (isUnique(A)!=True) and (i < len(A))):
        if A[i]<=A[i-1]:
            diff = A[i]-A[i-1]+1
            A[i]+= diff
            move+=diff
        i=i+1
    return move
def isUnique(A):
    B=set(A)
    if list(B) == A:
        return True
    else:
        return False

print (minMove([3,2,1,2,1,7]))