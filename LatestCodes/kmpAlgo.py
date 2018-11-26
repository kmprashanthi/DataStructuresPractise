def kmpAlgo(pat,txt):
    m =len(pat)
    n =len(txt)
    lps = [0]*m
    j=0
    
    computeLPS(pat,m,lps)

    i = 0
    while i<n:
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            print ("Index found at:", i-j)
            j = lps[j-1] #start from 1 position before the exact match
        elif i < n and pat[j] != txt[i]:
            if j !=0:
                j=lps[j-1] #the previous characters are anyway gonna match, so start from the index which is in lps
            else:
                i+=1 # just increment the ith value and start searching again from begining

def computeLPS(pat,m,lps):
    len = 0
    lps[0] = 0 
    i=1
    while i<m:
        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len!=0:
                len = lps[len-1]
            else:
                lps[i]=0
                i+=1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
kmpAlgo(pat, txt)



