n, m = map(int, input().split())
S = []
for i in range(n):
    S.append(input())

cnt = 0
for i in range(m):
    if input() in S:
        cnt += 1

print(cnt)