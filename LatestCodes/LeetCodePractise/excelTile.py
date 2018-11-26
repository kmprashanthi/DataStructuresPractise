def excelTile(n):
    """if n == 0:
        return ''
    elif (n>0 and n<=26):
        return chr(n+64)
    else:
        return excelTile(int(n/26)) + excelTile (n%26)"""

    if n == 0:
        return ''
    if n <26 or n<0:
        return chr(n+64)
    else:
        q = int(n/26)
        r = n%26
        if r == 0:
            return excelTile(q-1)+'Z'
        else :
            return excelTile(q)+excelTile(r)

print (excelTile(27))