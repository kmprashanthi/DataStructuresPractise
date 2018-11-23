def romanToInteger(s):
    dict_map = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000 }
    result = 0
    curr = 0 
    prev = 0
    s = s[::-1]
    for i in range(0,len(s)):
        curr = dict_map[s[i]]
        if i!=0:
            prev = dict_map[s[i-1]]
        if prev > curr:
            result = result - curr
        else:
            result = result + curr
    return result
        
print (romanToInteger('LIV'))    