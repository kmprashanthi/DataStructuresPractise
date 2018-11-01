def lowerCase(string):        
    lowerCase=''
    for s in string:
        if ord(s) >=65 and ord(s)<=90:
            lowerCase+= chr(ord(s)+32)
        else:
            lowerCase+=s
    return lowerCase

print (lowerCase('Hello'))