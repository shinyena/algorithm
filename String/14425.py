# 성공
# 백준 silver3
# 메모리: 36784KB
# 시간: 116ms

import sys

n, m = map(int, input().split())
S = set([sys.stdin.readline().rstrip() for _ in range(n)])

cnt = 0
for _ in range(m):
    if sys.stdin.readline().rstrip() in S:
        cnt += 1

print(cnt)