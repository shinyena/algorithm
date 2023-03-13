from itertools import permutations

n, k = map(int, input().split())
arr = []
dp = {}
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
    dp[w] = v


for i in range(2, n+1):
    for p in list(permutations(arr, i)):
        w = 0
        v = 0
        for j in range(len(p)):
            w += p[j][0]
            v += p[j][1]
        if w in dp:
            tmp = dp[w]
            dp[w] = max(v, tmp)
        else:
            dp[w] = v


print(dp[k])

