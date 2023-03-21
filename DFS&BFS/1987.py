# 성공
# 백준 gold4
# 메모리: 116300KB
# 시간: 7888ms

import sys

r, c = map(int, input().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = set([(0,0, arr[0][0])])
answer = 1
while queue:
    (x, y, visited) = queue.pop()
    answer = max(answer, len(visited))
    for (dx, dy) in d:
        if 0<=x+dx<r and 0<=y+dy<c:
            if arr[x+dx][y+dy] not in visited:
                queue.add((x+dx, y+dy, visited+arr[x+dx][y+dy]))

print(answer)