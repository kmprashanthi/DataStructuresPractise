def goatLatin(s):
    result = ''
    ListUtil = s.split(' ')
    i=1
    for word in ListUtil:
        if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
            word = word+'ma'
        else:
            remove = word[0]
            word = word[1:]
            word = word+remove+'ma'
        word = word+(i*'a')
        i=i+1
        result = result+' '+word
    
    result = result.strip()
    return result
   
print (goatLatin("I speak Goat Latin"))