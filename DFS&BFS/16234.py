# 성공
# 백준 gold5
# 메모리: 252056KB
# 시간: 1508ms

import sys
from collections import deque
sys.setrecursionlimit(10**5)

n, l, r = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


answer = 0

def update(brr, num):
    for (x,y) in brr:
        arr[x][y] = num

while True:
    visited = [[False] * n for _ in range(n)]
    is_updated = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                brr = []
                sum = 0
                while queue:
                    (x, y) = queue.popleft()
                    brr.append((x,y))
                    sum += arr[x][y]
                    for (dx, dy) in d:
                        if 0<=x+dx<n and 0<=y+dy<n:
                            if not visited[x+dx][y+dy]:
                                if l<=abs(arr[x][y] - arr[x+dx][y+dy])<=r:
                                    queue.append((x+dx, y+dy))
                                    visited[x+dx][y+dy] = True
                if len(brr)>1:
                    update(brr, sum//len(brr))
                    is_updated = True
    if is_updated:
        answer += 1
    else:
        print(answer)
        exit(0)