from collections import deque

n = int(input())
board = [list(input().strip()) for _ in range(n)]
d = [(1,0), (-1,0)]

max = 1
for i in range(n):
    for j in range(n):
        queue = deque([(i, j)])
        color = board[i][j]
        now = 0
        visited = [[False]*n for _ in range(n)]
        while queue:
            (x, y) = queue.popleft()
            visited[x][y] = True
            if board[x][y] == color:
                now += 1
            for (dx, dy) in d:
                if 0<=x+dx<n and 0<=y+dy<n:
                    if not visited[x+dx][y+dy]:
                        queue.append((x+dx, y+dy))

