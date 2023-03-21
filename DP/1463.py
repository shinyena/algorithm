# 성공
# 백준 silver3
# 메모리: 135672KB
# 시간: 1144ms

from collections import deque

n = int(input())
visited = {}

queue = deque([(1, 0)])
visited[1] = 0
while True:
    x, cnt = queue.popleft()
    if x == n:
        print(cnt)
        # print(visited)
        exit(0)
    if x+1 not in visited and x+1<=n:
        queue.append((x+1, cnt+1))
        visited[x+1] = cnt+1
    if x*2 not in visited and x*2<=n:
        queue.append((x*2 , cnt+1))
        visited[x*2] = cnt+1
    if x*3 not in visited and x*3<=n:
        queue.append((x*3, cnt+1))
        visited[x*3] = cnt+1
