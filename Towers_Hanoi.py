def towers_of_hanoi(n,strt=1,end=3):
    if n :
        towers_of_hanoi(n-1,strt,6-strt-end)
        print(" Move disk %d from %d peg to %d peg ")%(n,strt,end)
        towers_of_hanoi(n-1,6-strt-end,end)
    
towers_of_hanoi(4)