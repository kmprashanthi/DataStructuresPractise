def range_to_list(k):
    result=[]
    for i in range(0,k):
        result.append(str(i))
    return result

def k_arr(n,k):
    if n==0:
        return []
    if n==1:
        return range_to_list(k)
    return [digit+bitstring  for digit in k_arr(1,k) for bitstring in k_arr(n-1,k)]

print (k_arr(3,4))