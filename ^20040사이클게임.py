
import sys

input = sys.stdin.readline


def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def set_union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a == root_b:
        return False

    # 음수 절댓값이 큰 쪽(집합 크기가 큰 쪽)을 루트로 유지
    if parent[root_a] > parent[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_a] += parent[root_b]
    parent[root_b] = root_a
    return True


n, m = map(int, input().split())
parent = [-1] * n

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if not set_union(a, b):
        print(i)
        sys.exit(0)

print(0)
