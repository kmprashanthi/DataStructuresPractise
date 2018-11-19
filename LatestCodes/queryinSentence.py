def textQueries(sentences, queries):
    s_n = len(sentences)
    print ("sentences length: ", s_n)
    s_list = []
    for ele in sentences:
        s_list.append(ele.strip().split(" "))
    print ("sentences : ",s_list)
    q_list = []
    for ele in queries:
        q_list.append(ele.strip().split(" "))
    print ("queries : ",q_list)
    count = 0
    i=0
    for query in q_list:
        count =0
        check =0
        for sen in s_list:
            print("sen : ",sen)
            for word in query:
                print ("word : ",word)
                try :
                   sen.index(word)
                   count = count+1
                   print ("count : ",count)
                except ValueError:
                    print ("inside except")
                    break
                if count == len(sen):
                    print (i, end=" ")
                    check = check+1
                i=i+1
            if check == 0:
                print ("-1")
        print("\n")
sentences = ["jim likes mary","kate likes tom","tom does not like jim"]
queries = ["jim tom","likes"]
textQueries(sentences, queries)