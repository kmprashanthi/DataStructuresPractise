import math

def answer(n):
    prime_str = getPrimeString()
    return prime_str[n : n+5]

def getPrimeString():
    prime_str=''
    i=1
    while len(prime_str )< 10006:
        i=i+1
        prime = True
        for j in range (2, int(math.sqrt(i)+1)):
            if i%j == 0:
                prime=False
        if prime:
            prime_str = prime_str+str(i)
    return prime_str


print answer(3)



            
    


