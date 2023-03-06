# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 48ms

n = int(input())
answer = [[0]*100 for _ in range(100)]

for i in range(n):
    x1, y1 = map(int, input().split())
    for x in range(x1, x1+10):
        for y in range(y1, y1+10):
            answer[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if answer[i][j] == 1:
            cnt += 1
print(cnt)