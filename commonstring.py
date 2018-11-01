def longestCommonPrefix( strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c_str =  strs[0]
        i=1
        while (c_str != '') and (i<len(strs)):
            j=0
            print (c_str , strs[i])
            for j in range (len(strs[i])):
                if (strs[i][j]==c_str[j]) and (j<len(c_str)):
                    print (j, strs[i][j],c_str[j])
                    j=j+1
                else:
                    print ('else part',j, strs[i][j],c_str[j])
                    c_str = c_str[0:j]
                    print ('else part', c_str)
                print ('final c_str',c_str)
            i=i+1
        
        return c_str


print (longestCommonPrefix(["flower","flow","flight"]))