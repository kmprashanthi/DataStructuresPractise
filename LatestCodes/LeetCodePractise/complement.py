def compliment(num):
    return int ( bin((num ^ (2 ** (num.bit_length()+1) - 1)))[3:],2)


print (compliment(5))