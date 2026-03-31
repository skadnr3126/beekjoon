N = int(input())
origin_arr = []
arr = [[0] * 3 for _ in range(N)]
cost = [[0] * 3 for _ in range(N)]

def init_cost() :
    for i in range(N) :
        for j in range(3) :
            cost[i][j] = 0
    
def init_arr(color) :
    for i in range(N) :
        for j in range(3) :
            arr[i][j] = origin_arr[i][j]
    arr[0][(color+1)%3] = 10010
    arr[0][(color+2)%3] = 10010
    arr[N-1][color] = 10010

def get_min_color(N, before_color) : #n번째 집에서 가장 작은 코스트,인덱스가져오기
    idx = before_color 
    a = (idx + 1) % 3
    b = (idx + 2) % 3
    if arr[N][a] < arr[N][b] :
        return arr[N][a], a
    else :
        return arr[N][b], b

def get_min_cost(N,current_color) :
    idx = current_color
    a = (idx + 1) % 3
    b = (idx + 2) % 3
    if cost[N-1][a] >cost[N-1][b] :
        return cost[N-1][b]
    else :
        return cost[N-1][a]

def min_cost_by_first_home_color(color : int): #0,1,2 // R,G,B 
    #첫번째, 마지막에서 선택할때 고려해야되는거 추가하기
    total_cost = 0
    for i in range(N):
        min, color = get_min_color(i, color)
        total_cost += min
        #print(f'{i}번째 집에서 선택한 색깔 : {color}, 비용 : {min}')
        for j in range(3) :
            cost[i][j] =  arr[i][j] - min
        
        a = (color+1)%3
        b = (color+2)%3

        cost[i][a] = cost[i][a] + get_min_cost(i,a)
        cost[i][b] = cost[i][b] + get_min_cost(i,b)
        if cost[i][a] < 0 : 
            total_cost += cost[i][a]
            #print(f'{i}번째 집에서 선택한 색깔 : {a}, 비용 : {cost[i][a]}')
            color = a
            plus_cost = cost[i][a]
            for j in range(3) :
                cost[i][j] = cost[i][j] - plus_cost
        
        if cost[i][b] < 0 :
            total_cost += cost[i][b]
            #print(f'{i}번째 집에서 선택한 색깔 : {b}, 비용 : {cost[i][b]}')
            color = b
            plus_cost = cost[i][b]
            for j in range(3) :
                cost[i][j] = cost[i][j] - plus_cost
    
    return total_cost   

for i in range(N):
    origin_arr.append(list(map(int, input().split())))


init_cost()
init_arr(0)
#print(arr)
home_0 = min_cost_by_first_home_color(1)

init_cost()
init_arr(1)
home_1 = min_cost_by_first_home_color(2)

init_cost()
init_arr(2) 
home_2 = min_cost_by_first_home_color(0)
#print(home_2)

print(min(home_0, home_1, home_2))
#print(cost)


