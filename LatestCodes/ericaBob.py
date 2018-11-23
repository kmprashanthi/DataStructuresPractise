def winner(erica, bob):
    eS= {'S':0,'E':0,'M':0,'H':0,'sc':0}
    bS= {'S':0,'E':0,'M':0,'H':0,'sc':0}
    dictScore = {'S':0,'E':1,'M':3,'H':5}
    for i in range (0,len(erica)):
        eS['sc']+=dictScore[erica[i]]
        eS[erica[i]] +=1
        bS['sc']+=dictScore[bob[i]]
        bS[bob[i]]+=1
    print ("eS ", eS)
    print ("bS ", bS)
    if eS['sc']>bS['sc']:
        return 'Erica'
    elif eS['sc']<bS['sc']:
        return 'Bob'
    elif eS['sc']==bS['sc']:
        if eS['H']>bS['H']:
            return 'Erica'
        elif eS['H']<bS['H']:
            return 'Bob'
        elif eS['M']>bS['M']:
            return 'Erica'
        elif eS['M']<bS['M']:
            return 'Bob'
        elif eS['E']>bS['E']:
            return 'Erica'
        elif eS['E']<bS['E']:
            return 'Bob'
        else :
            return 'Tie'

print (winner('EEMEE','EESSH'))