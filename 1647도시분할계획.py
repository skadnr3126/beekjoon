import sys
N,M = map(int, input().split())
roads= []

        
for i in range(M) :
    road_info = list(map(int,  sys.stdin.readline().rstrip().split()))
    roads.append(road_info)
    #roads = sorted(roads, key= lambda x: x[2]) 
    
roads.sort(key=lambda x: x[2])
answer = 0
selected_road = 0
parent = [-1 for i in range(N+1)]

'''def find_par(x) :
    while parent[x] != -1 :
        x = parent[x]
    return x'''

def find_par(x):
    if parent[x] < 0:
        return x
    parent[x] = find_par(parent[x])
    return parent[x]
def set_union(a,b): 
    root1 = find_par(a)
    root2 = find_par(b)
    #if(root2 != root1): 같은 경우는 싸이클 일어나는 경우니까 합치지 않는다.
    parent[root1] = root2


for road in roads :
    A = road[0]
    B = road[1]
    C = road[2]
    root_a = find_par(A)
    root_b = find_par(B)
    if root_a == root_b :
        next
    else :
        set_union(A,B)
        selected_road +=1
        if selected_road == N-1 :
            break
        else : 
            answer += C

print(answer)

    
    



