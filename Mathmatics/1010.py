# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 80ms

dp = {1:1}
def fact(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = n * fact(n-1)
        return dp[n]

arr = []
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    else:
        print(int(fact(m)/(fact(n)*fact(m-n))))