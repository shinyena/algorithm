# 성공
# 백준 Gold5
# 메모리: 31256KB
# 시간: 184ms

import sys

n, m = map(int, input().split())

city = []
home = []
chicken = []

for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i, j))

distance = [[0]*len(chicken) for _ in range(len(home))]
for i in range(len(home)):
    for j in range(len(chicken)):
        distance[i][j] = abs(home[i][0]-chicken[j][0]) + abs(home[i][1] - chicken[j][1])

survive = []
answer = float("inf")
def back(start):
    global answer
    if len(survive) == m:
        now = 0
        for h in range(len(home)):
            now += min(distance[h][s] for s in survive)
        answer = min(answer, now)

    for i in range(start, len(chicken)):
        if i not in survive and len(survive) < m:
            survive.append(i)
            back(i)
            survive.pop()

back(0)
print(answer)
