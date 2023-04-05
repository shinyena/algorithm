# 성공
# 백준 Gold4
# 메모리: 31256KB
# 시간: 2224ms

import sys
from itertools import  combinations

n, m = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
safety_zone = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            safety_zone.append((i, j))

def find_safe(arr):
    visited = [[False]*m for _ in range(n)]
    # 바이러스 감염
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 and not visited[i][j]:
                queue = [(i, j)]
                while queue:
                    (x, y) = queue.pop(0)
                    visited[x][y] = True
                    for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if arr[x + dx][y + dy] == 0:
                                arr[x+dx][y+dy] = 2
                                queue.append((x+dx, y+dy))
    # 안전구역 세기
    safe = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                safe += 1
    return safe

answer = 0
for wall in combinations(safety_zone, 3):
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = lab[i][j]
    for (wx, wy) in wall:
        arr[wx][wy] = 1
    answer = max(find_safe(arr), answer)


print(answer)