def check (J,S):
    count = 0 
    for s in S :
        print (s)
        try:
            print ('here',s,J.index(s))
            count= count+1
        except:
            count = count+0
            
    return count


print (check('aAb','aAAbbbb'))