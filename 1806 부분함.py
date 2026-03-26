import sys

N,S = map(int ,sys.stdin.readline().rstrip().split())
input_list = list(map(int ,sys.stdin.readline().rstrip().split()))


#print(input_list)

start = 0
end = 0
sum = 0
answer = 0
lenth = 0
for i in range(N):
    sum += int(input_list[i])

    if sum >= S :
        end = i #발생한 부분합의 끝 부분
        answer = i+1
        lenth = i+1
        break
    

if sum < S :
    print(0)
    exit(0)
else :
    end += 1
    while start != end and end < N :
        
        out = input_list[start]
        income = input_list[end]
        end += 1

        while out > income and end < N:
            #print(f'end :{end}, income:{income}')
            income += input_list[end] 
            end += 1
        if out > income :

            #print(answer)
            exit(0)
        else :
            sum = sum + income
            while start != end:
                if sum - input_list[start] < S :
                    break
                #print(start)
                sum -= input_list[start]
                start += 1
            
            lenth = end - start
            if answer > lenth :
                answer = lenth
        
print(answer)
    

