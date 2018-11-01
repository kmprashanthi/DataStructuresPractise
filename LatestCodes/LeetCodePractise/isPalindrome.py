def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == '':
        return True
    print ('Actual string:' ,s )
    s=s.replace(' ','')
    print ('after replace: ' , s)
    s=s.lower()
    print ('after lower:' ,s)
    i=0
    while i < len(s):
        if not s[i].isalnum():
            s=s.replace(s[i],'')
            s=s.replace('\"','')
            s=s.replace(')','')
            s=s.replace('\','')
        i=i+1
    print('After replace2: ',s)
    return s == s[::-1]

print ( isPalindrome ("Damosel, a poem? A carol? Or a cameo pale? (So mad!)"))