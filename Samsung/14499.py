# 성공
# 백준 gold4
# 메모리: 31256KB
# 시간: 44ms

import sys
n, m, x, y, k = map(int, input().split())
dice_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
direction = list(map(int, sys.stdin.readline().split()))

now = 0
left = 0
right = 0
up = 0
down = 0
bottom = 0

for d in direction:
    if d == 1:
        if y+1 < m:
            y += 1
            tmp = right
            right = now
            now = left
            left = bottom
            bottom = tmp
            if dice_map[x][y] == 0:
                dice_map[x][y] = bottom
            else:
                bottom = dice_map[x][y]
                dice_map[x][y] = 0
            print(now)
    elif d == 2:
        if y-1 >= 0:
            y -= 1
            tmp = left
            left = now
            now = right
            right = bottom
            bottom = tmp
            if dice_map[x][y] == 0:
                dice_map[x][y] = bottom
            else:
                bottom = dice_map[x][y]
                dice_map[x][y] = 0
            print(now)
    elif d == 3:
        if x-1 >= 0:
            x -= 1
            tmp = down
            down = now
            now = up
            up = bottom
            bottom = tmp
            if dice_map[x][y] == 0:
                dice_map[x][y] = bottom
            else:
                bottom = dice_map[x][y]
                dice_map[x][y] = 0
            print(now)
    else:
        if x+1 < n:
            x += 1
            tmp = up
            up = now
            now = down
            down = bottom
            bottom = tmp
            if dice_map[x][y] == 0:
                dice_map[x][y] = bottom
            else:
                bottom = dice_map[x][y]
                dice_map[x][y] = 0
            print(now)