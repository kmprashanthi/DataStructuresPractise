def deleteDups(List_in):
    setTest = set(List_in)
    print (setTest)
    List_in = list(setTest)
    print (List_in)
    return len(List_in)

print ( deleteDups([1,1,1,2,3,4,5,5,6,6,6]) )
            
        