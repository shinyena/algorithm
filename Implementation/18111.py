# 성공
# 백준 Sliver2
# 메모리: 117424KB
# 시간: 824ms

import sys

n, m, b = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_time = sys.maxsize
max_height = 0
for height in range(257):
    add_block = 0
    sub_block = 0
    for i in range(n):
        for j in range(m):
            if height < arr[i][j]:
                sub_block += arr[i][j] - height
            else:
                add_block += height - arr[i][j]

    if sub_block - add_block + b >= 0:
        if (add_block + 2*sub_block) <= min_time:
            min_time = add_block + 2*sub_block
            max_height = height

print(min_time, max_height)



