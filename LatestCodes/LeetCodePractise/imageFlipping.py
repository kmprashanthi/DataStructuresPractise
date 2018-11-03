def image(A):
    result = []
    for row in A:
            row = row[::-1]
            print ('After reversing :',row)
            for i in range(len(row)):
                print (row[i])
                if row[i] == 0:
                    row[i] = 1
                    print ('case 0 if part ',row[i])
                else :
                    row[i] = 0
                    print ('case 1 else part ',row[i])
            result.append(row)
            print ('After inverting :',row)
    return result

print ( image([[1,1,0],[1,0,1],[0,0,0]]) )