import sys
from pprint import pprint

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cctv = {1:[], 2:[], 3:[], 4:[], 5:[]}

for i in range(n):
    for j in range(m):
        if arr[i][j] in cctv:
            cctv[arr[i][j]].append((i, j))

if cctv[5]:
    for (x,y) in cctv[5]:
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            a, b = x+dx, y+dy
            while 0<=a<n and 0<=b<m:
                if arr[a][b] == 0:
                    arr[a][b] = 9
                elif arr[a][b] == 6:
                    break
                a, b = a+dx, b+dy


pprint(arr)