def closest(s, queries):
    # Write your code here
    result =[]
    for n in queries:
        pos = -1
        min = len(s)+1
        for i in range(0,len(s)):
            if (s[n] == s[i]) and (n!=i):
                if min > abs(n-i):
                    min = abs(n-i)
                    pos = i
            elif (s[n] == s[i]) and (n == i):
                continue
        result.append(pos)
    return result
            

s = 'aaaa'
queries = [0,1,2,3]
print (closest(s,queries))