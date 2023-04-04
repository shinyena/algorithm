# 성공
# 백준 gold4
# 메모리: 31388KB
# 시간: 44ms

import sys

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = 1

l = int(input())
turn = {}
for _ in range(l):
    t, d = sys.stdin.readline().split()
    turn[int(t)] = d

time = 0
direct = 0
snake = []
x, y = (0, 0)
while True:
    snake.append((x, y))

    # 이동    
    if direct == 0:
        y += 1
    elif direct == 1:
        x += 1
    elif direct == 2:
        y -= 1
    elif direct == 3:
        x -= 1

    if 0<=x<n and 0<=y<n:
        if (x,y) in snake: # 이동할 곳이 뱀이면 종료
            print(time+1)
            break
        elif board[x][y] == 1: # 이동할 곳이 사과면 길이 증가
            board[x][y] = 0
        else:
            snake.pop(0)
    else: # 이동할 곳이 벽이면 종료
        print(time+1)
        break

    # 시간경과
    time += 1
    if time in turn:
        if turn[time] == "D":
            direct = (direct + 1) % 4
        else:
            direct -= 1
            if direct < 0:
                direct += 4