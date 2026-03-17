import sys
import array


n = int(input())

tree = [[] for _ in range(n+1)]
visited = [False] * 10001
max = 0
max_dis = [n+1][n+1]


#트리 만들기
for i in range(n) :
    
    #value = int(input().split())
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while(data[idx] != -1) :
        next_node = data[idx]
        dist = data[idx+1]
        tree[node].append((next_node,dist))
        idx += 2
    

#dfs
 
def fine_tree_dia(int start):
    for node in tree :
        
        for next_node in node:
            if(넥스트 노드가 접근 가능한 노드가 있으면) :
                max_dis[node_num][next_node[0]] = fine_tree_dia(next_node) + next_node[1]

            else :
                max_dis[node_num][next_node[0]] = next_node[1]
            
