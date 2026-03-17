text = input()
stack = []
answer = ''

pri_dict = {'+' : 1 , '-' : 1 , '*' : 2 , '/' : 2 , '(' : 0}
for word in text :
    if word <= 'Z' and word >= 'A' :
        answer += word
        
    elif word == '(' :

        stack.append(word)
        
        
    elif word == ')' :

        while (x := stack.pop()) != '(' :
            answer += x

            
    else:
        if len(stack) == 0 :
            stack.append(word)
        else :
            while stack and pri_dict[stack[-1]] >= pri_dict[word] :
                    answer += stack.pop()
            stack.append(word)

            


while len(stack) != 0 :
    answer += stack.pop()


print(answer)
        


    
    
