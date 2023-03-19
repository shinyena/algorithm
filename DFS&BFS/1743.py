# 성공
# 백준 Sliver1
# 메모리: 34324KB
# 시간: 284ms

from collections import deque

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False]*m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            queue = deque([(i, j)])
            visited[i][j] = True
            cnt = 0
            while queue:
                (x, y) = queue.popleft()
                cnt += 1
                for (dx, dy) in d:
                    if 0<=x+dx<n and 0<=y+dy<m:
                        if not visited[x+dx][y+dy] and arr[x+dx][y+dy] == 1:
                            queue.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
            if cnt>answer:
                answer = cnt
print(answer)