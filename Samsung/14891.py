# 성공
# 백준 Gold5
# 메모리: 31256KB
# 시간: 40ms

import sys

gears = [list(map(int, sys.stdin.readline().strip())) for _ in range(4)]
k = int(input())
rotate = []
for i in range(k):
    n, d = map(int, sys.stdin.readline().split())
    rotate.append([n-1, d])
def change_gear(g, d):
    if d == 1: # 시계
        return gears[g][7:] + gears[g][:7]
    else: # 반시계
        return gears[g][1:] + gears[g][:1]

for (g, d) in rotate:
    tmp = [[]*4 for _ in range(4)]
    tmp[g] = change_gear(g, d)

    new_g = g + 1
    new_d = d
    while new_g < 4:
        if gears[new_g-1][2] != gears[new_g][6]:
            new_d = -new_d
            tmp[new_g] = change_gear(new_g, new_d)
            new_g += 1
        else:
            break


    new_g = g - 1
    new_d = d
    while new_g > -1:
        if gears[new_g][2] != gears[new_g+1][6]:
            new_d = -new_d
            tmp[new_g] = change_gear(new_g, new_d)
            new_g -= 1
        else:
            break

    for i in range(4):
        if tmp[i] != []:
            gears[i] = tmp[i]


answer = 0
if gears[0][0] == 1:
    answer += 1
if gears[1][0] == 1:
    answer += 2
if gears[2][0] == 1:
    answer += 4
if gears[3][0] == 1:
    answer += 8
print(answer)