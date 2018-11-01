def judgeCircle(moves):
        """
        :type moves: str
        :rtype: bool
        """
        bit_string = []
        
        for char in moves:
            if char == 'U' or char =='D':
                bit_string.append (1)
            else :
                bit_string.append(0)
        res = bit_string[0]
        for i in range(len(bit_string)-1):
            res = res ^ bit_string[i+1]
        if res == 0:
            return True
        else:
            return False

print (judgeCircle('LL'))