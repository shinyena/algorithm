import sys
from collections import deque

n, m = map(int, input().split())
paper = []
max_num = 0
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
    max_num = max(max_num, max(paper[i]))

max_answer = 0
for k in range(max_num, -1, -1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if paper[i][j] >= k:
                cnt = 0
                answer = 0
                queue = deque([(i, j)])
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                while queue and cnt != 4:
                    (x, y) = queue.popleft()
                    answer += paper[x][y]
                    cnt += 1
                    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if paper[x + dx][y + dy] >= k and not visited[x + dx][y + dy]:
                                visited[x + dx][y + dy] = True
                                queue.append((x + dx, y + dy))
                max_answer = max(max_answer, answer)
    if cnt == 4:
        print(max_answer)
        exit(0)
