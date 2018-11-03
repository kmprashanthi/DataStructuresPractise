def reverse(s):
    revSplit = s.split(' ')
    print (revSplit)
    result = ''
    for char in revSplit:
        print (char[::-1])
        result = result + ' ' +char[::-1]
    result = result.strip()

    print (s)
    print (result)

    return result


print (reverse ("Let's take LeetCode contest"))