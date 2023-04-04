# 성공
# 백준 silver3
# 메모리: 31256KB
# 시간: 52ms

import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
work = 0
def back(start):
    global work
    global answer
    if work>answer:
        answer = work

    for i in range(start, n):
        if i + arr[i][0] <= n:
            work += arr[i][1]
            if i + arr[i][0] <= n:
                back(i + arr[i][0])
            work -= arr[i][1]

back(0)
print(answer)