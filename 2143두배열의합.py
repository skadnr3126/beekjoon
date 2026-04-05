from bisect import bisect_left

T = int(input())
a = int(input())
list_a = list(map(int, input().split()))

b = int(input())
list_b = list(map(int, input().split()))

# A의 부분합을 "합 -> 개수"로 저장
sum_count_a = {}
for i in range(a):
    current_sum = 0
    for j in range(i, a):
        current_sum += list_a[j]
        if current_sum in sum_count_a:
            sum_count_a[current_sum] += 1
        else:
            sum_count_a[current_sum] = 1

# 합 기준으로 정렬된 리스트 (합들만) + 각 합의 개수 매핑 유지
sorted_sums_a = sorted(sum_count_a.keys())

answer = 0

# B의 부분합을 순회하며 T - 부분합을 이분탐색으로 찾기
for i in range(b):
    current_sum = 0
    for j in range(i, b):
        current_sum += list_b[j]
        target = T - current_sum

        idx = bisect_left(sorted_sums_a, target)
        if idx < len(sorted_sums_a) and sorted_sums_a[idx] == target:
            answer += sum_count_a[target]

print(answer)