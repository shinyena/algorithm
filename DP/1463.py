# 성공
# 백준 Sliver3
# 메모리: 31256KB
# 시간: 40ms

n = int(input())
dp = {1:0, 2:1}
def fn(x):
    if x in dp:
        return dp[x]
    if x%3 == 0 and x%2 == 0:
        dp[x] = min(fn(x//3), fn(x//2)) + 1
    elif x%3 == 0:
        dp[x] = min(fn(x//3), fn(x-1)) + 1
    elif x%2 == 0:
        dp[x] = min(fn(x//2), fn(x-1)) + 1
    else:
        dp[x] = fn(x-1) + 1
    return dp[x]


print(fn(n))