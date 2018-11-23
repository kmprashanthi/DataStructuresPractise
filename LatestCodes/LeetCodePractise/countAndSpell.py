def countSpell(n):
    i = 0
    string ='1'
    cnt =1
    tmpStr =''
    for i in range(2,n+1):
        j=0
        curr =string[0]
        count = 0
        tmpStr = ''
        for j in range (0,len(string)):
            print ("j,string,count ", j, string[0],count)
            if (string[j] == curr) :
                print("Char match string[j], curr", string[j],curr)
                count =count+1
            else:
                print ("concat : ", str(count)+curr)
                tmpStr = tmpStr+str(count)+curr
                count =1
                curr = string[j]
            if j == len(string)-1:
                tmpStr = tmpStr+str(count)+curr
        string = tmpStr
        print ("string at n : ",string,i)
    return string
            

print (countSpell(5))
            
            

        