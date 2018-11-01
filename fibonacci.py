def fibonaccival(n):
    mem = [0] * (n+1)
    print (mem)
    mem[1]= 1
    for i in range (2,n+1):
        mem[i]=mem[i-1]+mem[i-2]
    return mem[n]

print (fibonaccival(4))
