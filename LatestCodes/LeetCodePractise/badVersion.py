def badVersion(n):
    if isBadVersion(1):
        return 1
    val = n
    start = 1
    end = n
    while(start<=end): 
        mid = int((start+end)/2)
        if (isBadVersion(mid) == True):
            end = mid
            if mid < val:
                val = mid
        else:
            if mid == val-1:
                return val
            start = mid 

def isBadVersion(m):
    if m >=1:
        return True
    else :
        return False

print (badVersion(5))