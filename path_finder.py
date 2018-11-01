def path_finder(Arr,pos,N):
    if pos==(N-1,N-1):
        return [(N-1,N-1)]
    
    x,y = pos
    if x+1 < N and Arr[x+1][y]==1:  # moving down 
        a = path_finder(Arr,(x+1,y),N)
        if a!=None:
            return [(x,y)]+a
    
    if y+1 < N and Arr[x][y+1]==1:  # moving left 
        b = path_finder(Arr,(x,y+1),N)
        if b !=None : 
            return [(x,y)]+b

Arr = [[1,1,1,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,0,0],[1,1,1,1,1]]
print (path_finder(Arr,(0,0),5))