import sys
from collections import deque

n, k = map(int, input().split())
arr = [[]*n for _ in range(n)]

total = 0
for i in range(n):
    arr[i] = list(sys.stdin.readline().strip())
    for j in range(n):
        if arr[i][j] == "O":
            total += 1
        elif arr[i][j] == "B":
            (bx, by) = (i, j)

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = [[False]*n for _ in range(n)]
cnt = 0


if total<k:
    print(-1)

else:
    queue = deque([(bx, by)])
    visited[bx][by] = True
    while queue:
        sorted_queue = list(queue)
        sorted_queue = sorted(sorted_queue, key=lambda x: (abs(x[0]-bx)+abs(x[1]-by), x[0], x[1]))
        queue = deque(sorted_queue)
        (x, y) = queue.popleft()
        if arr[x][y] == "O":
            arr[x][y] = "X"
            cnt += 1
            if cnt == k:
                break
        for (dx, dy) in d:
            if 0<=x+dx<n and 0<=y+dy<n:
                if not visited[x+dx][y+dy]:
                    queue.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = True
    for i in range(n):
        for j in range(n):
            sys.stdout.write(arr[i][j])
        print()