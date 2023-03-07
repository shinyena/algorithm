# 성공
# 백준 Sliver2
# 메모리: 34176KB
# 시간: 112ms

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [False]*(n+1)

def dfs(idx):
    print(idx, end=" ")
    visited[idx] = True
    for node in graph[idx]:
        if not visited[node]:
            dfs(node)

dfs(v)
print()

visited = [False]*(n+1)
queue = deque([v])
while queue:
    idx = queue.popleft()
    print(idx, end=" ")
    visited[idx] = True
    for node in graph[idx]:
        if not visited[node] and node not in queue:
            queue.append(node)