# 성공
# 백준 Sliver3
# 메모리: 31256KB
# 시간: 52ms

dp = {0:(1, 0), 1:(0, 1)}

def fib(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = (fib(n-1)[0] + fib(n-2)[0], fib(n-1)[1] + fib(n-2)[1])
        return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(fib(n)[0],fib(n)[1])