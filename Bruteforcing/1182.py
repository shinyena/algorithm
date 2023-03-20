# 성공
# 백준 silver2
# 메모리: 31256KB
# 시간: 352ms

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(1, n+1):
    crr = combinations(arr, i)
    for c in crr:
        if sum(c) == s:
            answer += 1
print(answer)