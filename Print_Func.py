def print_func(n):
    if n==0:
        return 0
    else :
        print n
        return print_func(n-1)

print_func(5)