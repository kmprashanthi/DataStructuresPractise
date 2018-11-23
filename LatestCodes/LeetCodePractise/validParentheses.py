def validParantheses(s):
    if s == '':
            return True
    stack = []
    cnt = 0
    for ele in s:
        if  ele in ['(','{','['] :
            cnt = cnt + 1
            print ("inserting : ",ele)
            stack.append(ele)
            print ("after insertion stack :",stack)
        elif ele in [')','}',']']:
            print ("popping to check:",ele)
            if len(stack) == 0:
                print ("stack empty: returning false")
                return False
            elif ele == ')' and stack.pop() == '(':
                print ("stack matches, continuing ")
                cnt = cnt -1
                continue
            elif ele == '}' and stack.pop() == '{':
                print ("stack matches, continuing ")
                cnt = cnt -1
                continue
            elif ele == ']' and stack.pop() == '[':
                print ("stack matches, continuing ")
                cnt = cnt -1
                continue
            else :
                print ("stack doesnt match : returning false")
                return False
    if cnt == 0:
        return True
    else :
        return False

print (validParantheses('[[['))