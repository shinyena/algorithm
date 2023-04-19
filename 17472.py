# 성공
# 백준 gold1
# 메모리: 34436KB
# 시간: 64ms

from sys import stdin
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]


# 섬 구하기
island = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            queue = deque([(i, j)])
            visited[i][j] = True
            tmp_island = []
            while queue:
                (x, y) = queue.popleft()
                tmp_island.append((x, y))
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0<=x+dx<n and 0<=y+dy<m:
                        if not visited[x+dx][y+dy] and arr[x+dx][y+dy] == 1:
                            visited[x+dx][y+dy] = True
                            queue.append((x+dx, y+dy))
            island.append(tmp_island)

# 다리 구하기
bridge = {}
for i in range(len(island)):
    for (x, y) in island[i]:
        
        # 아래로 이동
        (a, b) = (x, y)
        cnt = -1
        while a+1<n:
            a += 1
            cnt += 1
            if arr[a][b] == 1: # 1 만나면 중지
                if cnt>1: # 단, 거리 2이상 떨어져 있으며, 다른 섬에 있는 1을 만났으면 다리를 놓기
                    for j in range(i+1, len(island)): # 어느 섬에 속한지 찾기
                        if (a, b) in island[j]:
                            if (i, j) in bridge:
                                bridge[(i, j)] = min(bridge[(i, j)], cnt)
                                bridge[(j, i)] = min(bridge[(j, i)], cnt)
                            else:
                                bridge[(i, j)] = cnt
                                bridge[(j, i)] = cnt
                break
        
        # 위로 이동
        (a, b) = (x, y)
        cnt = -1
        while a - 1 >= 0:
            a -= 1
            cnt += 1
            if arr[a][b] == 1:
                if cnt > 1:
                    for j in range(i + 1, len(island)):
                        if (a, b) in island[j]:
                            if (a, b) in island[j]:
                                if (i, j) in bridge:
                                    bridge[(i, j)] = min(bridge[(i, j)], cnt)
                                    bridge[(j, i)] = min(bridge[(j, i)], cnt)
                                else:
                                    bridge[(i, j)] = cnt
                                    bridge[(j, i)] = cnt
                break

        # 오른쪽으로 이동
        (a, b) = (x, y)
        cnt = -1
        while b + 1 < m:
            b += 1
            cnt += 1
            if arr[a][b] == 1:
                if cnt > 1:
                    for j in range(i + 1, len(island)):
                        if (a, b) in island[j]:
                            if (i, j) in bridge:
                                bridge[(i, j)] = min(bridge[(i, j)], cnt)
                                bridge[(j, i)] = min(bridge[(j, i)], cnt)
                            else:
                                bridge[(i, j)] = cnt
                                bridge[(j, i)] = cnt
                break

        # 왼쪽으로 이동
        (a, b) = (x, y)
        cnt = -1
        while b - 1 >= 0:
            b -= 1
            cnt += 1
            if arr[a][b] == 1:
                if cnt > 1:
                    for j in range(i + 1, len(island)):
                        if (a, b) in island[j]:
                            if (i, j) in bridge:
                                bridge[(i, j)] = min(bridge[(i, j)], cnt)
                                bridge[(j, i)] = min(bridge[(j, i)], cnt)
                            else:
                                bridge[(i, j)] = cnt
                                bridge[(j, i)] = cnt
                break

graph = [[]*len(island) for _ in range(len(island))]
for (a, b) in bridge:
    graph[a].append(b)

answer = 0
visited_node = {0}  # 방문한 노드
for _ in range(len(island) - 1):
    min_node = 0
    min_value = float("inf")
    for node in visited_node: # 지금까지 방문한 노드와
        for target in graph[node]: # 인접한 노드 중에서
            if bridge[(node, target)]<min_value and target not in visited_node: # 최소 간선 선택하기
                min_value = bridge[(node, target)]
                min_node = target
    visited_node.add(min_node) # 방문 기록하고
    answer += min_value # 값 더하기
    
# 답 출력
if answer == float("inf"):
    print(-1)
else:
    print(answer)