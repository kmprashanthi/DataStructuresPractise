def binaryAdd(a,b):
    a = int(a,2)
    b = int(b,2)
    c = a+b
    print (bin(int(a,2)+int(b,2))[2:])
    return bin(c)[2:]

print(binaryAdd('11','1'))