# 성공
# 백준 Gold5
# 메모리: 31316KB
# 시간: 64ms

import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
clean = 0
forward = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
backward = {0:(1, 0), 1:(0, -1), 2:(-1, 0), 3:(0, 1)}
def dfs(x, y, d):
    global clean
    if room[x][y] == 0:
        clean += 1
        room[x][y] = 9

    cnt = 0
    while cnt != 4:
        d -= 1
        if d < 0:
            d += 4
        if 0<=x+forward[d][0]<n and 0<=y+forward[d][1]<m and room[x+forward[d][0]][y+forward[d][1]] == 0:
            dfs(x+forward[d][0], y+forward[d][1], d)
            break
        else:
            cnt += 1

    if cnt == 4:
        if 0<=x+backward[d][0]<n and 0<=y+backward[d][1]<m:
            if room[x+backward[d][0]][y+backward[d][1]] != 1:
                dfs(x + backward[d][0], y + backward[d][1], d)


dfs(r, c, d)
print(clean)