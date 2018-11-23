def validPalindrome(s):
    sTmp = []
    if s == s[::-1]:
        return True
    for i in range(0,len(s)):
        sTmp = list(s)
        print("list value of string ",sTmp)
        del sTmp[i]
        print ("sTmp after deletion : ",sTmp)
        if sTmp == sTmp[::-1]:
            print ("Temporary String and its reverse ",sTmp,sTmp[::-1])
            return True
    return False

print (validPalindrome('abca'))
    
        