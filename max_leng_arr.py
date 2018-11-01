def get_val(A,i,j,R,C,size):
    if(i<0 or i>=R or j<0 or j>=C):
        return 0
    else:
        return A[i][j]

def get_max_blocks(A,r,c,R,C,size):
    global maxsize
    global cntarr
    if (r>=R or c>=C): 
        return 
    cntarr[r][c]=1
    size+=1
    if (size > maxsize):
        maxsize = size 
    dir=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range (0,7):
        newi = r+dir[i][0]
        newj = c+dir[i][1]
        print ("the new pair of i,j after ( %d , %d ) is ( %d , %d ) with max sixe %d "%(r,c,newi,newj,maxsize))
        val = get_val(A,newi,newj,R,C,size)
        if(val>0 and cntarr[newi][newj]==0):
            get_max_blocks(A,newi,newj,R,C,size)
    cntarr[r][c]=0

def get_max_ones(A,R,C):
    global maxsize
    global size
    global cntarr
    for i in range (0,R):
        for j in range (0,C):
            if A[i][j]==1 :
                get_max_blocks(A,i,j,R,C,size)
    return maxsize

zarr = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
rmax=5
colmax=5
maxsize=0
size=0
cntarr=rmax*[colmax*[0]] # creates an array with rmax rows and colmax columns , check the syntax
print ("max 1 s are :")
print get_max_ones(zarr,rmax,colmax)