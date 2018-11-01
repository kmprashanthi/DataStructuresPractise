def divide(left,right):
    result =[]
    for i in range (left,right+1):
        flag =0
        stringVer = str(i)
        for char in stringVer:
            if int(char) ==0:
                flag =1
                break
            if (i % (int(char))) != 0:
                flag = 1
        if flag == 0:
            result.append(i)
    return result

print (divide (1,22))