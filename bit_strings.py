def append_beg(x,L):
    return [x+element for element in L]

def bit_strings(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    return ( append_beg("0",bit_strings(n-1))+append_beg("1",bit_strings(n-1)))

print (bit_strings(3))

def bit_strings1(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    return [dig+bits for dig in bit_strings1(1) for bits in bit_strings1(n-1)]

print (bit_strings1(3))


