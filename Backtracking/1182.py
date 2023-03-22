# 성공
# 백준 silver2
# 메모리: 31256KB
# 시간: 488ms

import sys

n, s = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
answer = []

def back(start):
    global cnt
    if sum(answer) == s and len(answer)>0:
        cnt += 1

    for i in range(start, n):
        answer.append(arr[i])
        back(i+1)
        answer.pop()

back(0)
print(cnt)