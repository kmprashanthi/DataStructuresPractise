def trippleStep(n):
    mem = [-1]*(n+1)
    print ("mem value :", mem)
    return trippleUtil(n,mem)

def trippleUtil(n,mem):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif mem[n]>=0:
        return mem[n]
    else:
        mem[n] = trippleUtil(n-1,mem)+trippleUtil(n-2,mem)+trippleUtil(n-3,mem)
        return mem[n]


print(trippleStep(3))