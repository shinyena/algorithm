# 성공
# 백준 Sliver1
# 메모리: 34176KB
# 시간: 76ms


from collections import deque

m, n, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

visited = [[False]*m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = []
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 0:
            cnt += 1
            queue = deque([(i, j)])
            visited[i][j] = True
            area = 0
            while queue:
                (x,y) = queue.popleft()
                area += 1
                for (dx, dy) in d:
                    if 0<=x+dx<n and 0<=y+dy<m:
                        if not visited[x+dx][y+dy] and arr[x+dx][y+dy] == 0:
                            queue.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
            answer.append(area)

print(cnt)

answer.sort()
for i in answer:
    print(i, end=" ")