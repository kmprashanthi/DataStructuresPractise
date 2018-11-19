def missingWords(s, t):
    # Write your code here
    result = []
    t_lst = t.strip().split(" ")
    s_list = s.strip().split(" ")
    strt = 0
    end = len(s_list)
    for i in range (strt,end):
        try:
            strt=t_lst.index(s_list[i])
            strt = strt+1
            print ("start", strt)
        except ValueError:
            result.append(s_list[i])
            print ("result ", result )
    return result

s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"
print(missingWords(s,t))