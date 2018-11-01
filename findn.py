def findNumber(arr, k):
    try :
        arr.index(k)
        return 'yes'
    except ValueError:
        return 'no'


print (findNumber([1,2,3,4,5],10))
