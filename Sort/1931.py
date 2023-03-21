# 성공
# 백준 silver1
# 메모리: 59204KB
# 시간: 268ms

import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))

time = arr[0][1]
answer = 1
for i in range(1, n):
    if arr[i][0] >= time:
        answer += 1
        time = arr[i][1]
print(answer)