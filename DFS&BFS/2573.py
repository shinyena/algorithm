# 성공
# 백준 Gold4
# 메모리: 217944KB
# 시간: 1016ms

import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

while True:
    # bfs 수행
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    ice = deque([])
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                queue = deque([(i, j)])
                ice.append((i, j))
                visited[i][j] = True
                while queue:
                    (x, y) = queue.popleft()
                    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if not visited[x + dx][y + dy] and arr[x + dx][y + dy] != 0:
                                visited[x + dx][y + dy] = True
                                queue.append((x + dx, y + dy))

                                # 빙산이 있는 곳 ice에 담기
                                ice.append((x + dx, y + dy))
                cnt += 1

                # 두덩어리 이상이면 종료
                if cnt >= 2:
                    print(answer)
                    exit(0)

    # 다 녹았는데 두덩어리가 아니므로 종료
    if not ice:
        print(0)
        exit(0)

    # 빙산 녹이기
    tmp = {}
    while ice:
        (x, y) = ice.popleft()
        cnt = 0
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if arr[x + dx][y + dy] == 0:
                    cnt += 1
        tmp[(x, y)] = arr[x][y] - cnt
        if tmp[(x, y)] < 0:
            tmp[(x, y)] = 0

    # 녹인 빙산 반영
    for (x, y) in tmp.keys():
        arr[x][y] = tmp[(x, y)]

    # 1년 후
    answer += 1