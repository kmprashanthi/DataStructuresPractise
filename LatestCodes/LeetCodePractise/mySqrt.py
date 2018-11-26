def mysqrt(x):
    if x==0:
        return 0
    start=1 
    end =x
    while(start<end):
        mid = int((start+end)/2)
        print ("mid : ",mid)
        print ("int(x/mid) : ",int(x/mid))
        #print ("relational Value: ",mid <= int(x/mid))
        print ("mid+1 :", mid+1)
        print ("int(x/mid+1) :",int(x/(mid+1)))
        #print ("relational Value: ",(mid+1 > int(x/mid+1))
        #print ("total relational value: ",(mid <= int(x/mid))  and (mid+1 > int(x/mid+1))
        if (mid <= int(x/mid))  and (mid+1 > int(x/(mid+1))):
            return mid
        elif mid > int(x/mid):
            end = mid
        else:
            start = mid+1
    return start

print (mysqrt(8))