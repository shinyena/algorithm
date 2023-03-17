# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 156ms

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
brr = [list(map(int, input().split())) for _ in range(m)]

for a in range(n):
    for b in range(k):
        num = 0
        for e in range(m):
            num += arr[a][e] * brr[e][b]
        print(num, end=" ")
    print()