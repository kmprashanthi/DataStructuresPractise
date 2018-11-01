def isPalindrome(s):
        if s == '':
            return True
        s=s.replace(' ','')
        print (s)
        s=s.lower()
        print (s)
        i=0
        while i < len(s):
            if not s[i].isalnum():
                print (s)
                s=s.replace(s[i],'')
                print (s)
                print (s[::-1])
            i=i+1
        if s == s[::-1]:
            print ('True')
        else : 
            print ('False')
        return 'true'

isPalindrome('"Nella's simple hymn: \"I attain my help, Miss Allen.\""')