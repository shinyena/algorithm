# 성공
# 백준 silver2
# 메모리: 31256KB
# 시간: 412ms

import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = []
cnt = 0

def back(idx):
    global cnt

    if idx >= n:
        return

    answer.append(arr[idx])

    if sum(answer) == s and len(answer)>0:
        cnt += 1

    back(idx + 1)
    answer.pop()
    back(idx + 1)

back(0)
print(cnt)