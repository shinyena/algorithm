import sys
from collections import deque
from pprint import pprint

n = int(input())
arr = [[]*n for _ in range(n)]
for i in range(n):
    arr[i] = list(sys.stdin.readline().split())
    for j in range(n):
        if arr[i][j] == "S":
            start = (i,j)
        elif arr[i][j] == "E":
            end = (i,j)
        elif arr[i][j] == "a":
            a = (i,j)
        elif arr[i][j] == "b":
            b = (i,j)
        elif arr[i][j] == "A":
            A = (i,j)
        elif arr[i][j] == "B":
            B = (i,j)

d = [(1,0), (0,1), (-1,0), (0,-1)]
dp = [[9999]*n for _ in range(n)]
dp[end[0]][end[1]] = 1

for i in range(3):
    visited = [[False] * n for _ in range(n)]
    if i==0:
        visited[end[0]][end[1]] = True
        queue = deque([end])
    if i==1:
        visited[A[0]][A[1]] = True
        queue = deque([A])
    if i==2:
        visited[B[0]][B[1]] = True
        queue = deque([B])
    while queue:
        (x, y) = queue.popleft()
        visited[x][y] = True
        for (dx, dy) in d:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if not visited[x + dx][y + dy]:
                    if arr[x + dx][y + dy] in ("0", "a", "b", "S"):
                        dp[x + dx][y + dy] = min(dp[x][y] + 1, dp[x + dx][y + dy])
                        queue.append((x + dx, y + dy))
                    if arr[x + dx][y + dy] == "A":
                        dp[x + dx][y + dy] = min(dp[a[0]][a[1]] + 1, dp[x + dx][y + dy])
                        queue.append((x + dx, y + dy))
                    if arr[x + dx][y + dy] == "B":
                        dp[x + dx][y + dy] = min(dp[b[0]][b[1]] + 1, dp[x + dx][y + dy])
                        queue.append((x + dx, y + dy))
        if (x, y) == a:
            dp[A[0]][A[1]] = min(dp[x][y] + 1, dp[A[0]][A[1]])
            queue.append(A)
        elif (x, y) == b:
            dp[B[0]][B[1]] = min(dp[x][y] + 1, dp[B[0]][B[1]])
            queue.append(B)






if dp[start[0]][start[1]] == 9999:
    print(-1)
else:
    print(dp[start[0]][start[1]])

pprint(dp)