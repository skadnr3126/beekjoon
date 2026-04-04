import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(target : int) :
    if complete_time[target] != 0 :
        return complete_time[target]
    if not parent[target] :
        complete_time[target] = construct_time[target]
        return complete_time[target]
    else :
        best = 0
        for child in parent[target] :
            if complete_time[child] == 0 :
                complete_time[child] = solve(child)
            if best < complete_time[child] :
                best = complete_time[child] 
        
        complete_time[target] =  best + construct_time[target]
        return complete_time[target]
            

T = int(read())
answers = []

for _ in range(T) :
    n,k = map(int, read().split())
    construct_time = list(map(int, read().split()))
    construct_time = [0]+construct_time
    parent = [[] for _ in range(n+1)]
    complete_time = [0] * (n+1)
    for _ in range(k) :
        p,c = map(int, read().split())
        parent[c].append(p)
    target = int(read())
    answers.append(str(solve(target)))

sys.stdout.write("\n".join(answers))


