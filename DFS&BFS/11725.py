# 성공
# 백준 Sliver2
# 메모리: 49356KB
# 시간: 316ms

import sys
from collections import deque

n = int(input())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
parent[1] = 1

queue = deque([1])
while queue:
    now = queue.popleft()
    for node in graph[now]:
        if parent[node] == 0:
            parent[node] = now
            queue.append(node)

answer = ""
for i in range(2, n+1):
    sys.stdout.write(str(parent[i]) + "\n")