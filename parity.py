def sortArrayByParity( A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd =[]
        even = []
        
        for num in A :
            if num%2 == 0:
                print (num)
                even.append(num)
                print (even)
            else :
                print(num)
                odd.append(num)
                print(odd)
        even.extend(odd)
        print (even)
        return even


print (sortArrayByParity([3,1,2,4]))