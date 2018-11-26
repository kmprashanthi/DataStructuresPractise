def validPalindrome(s):
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i]:
            j = len(s) - 1 - i
            print ("i and j in parent function:",i,j)
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)
    return True
def is_pali_range(i, j):
    print ("i, j in is_pali_range",i,j)
    return all(s[k] == s[j-k+i] for k in range(i, j))

print (validPalindrome('abca'))