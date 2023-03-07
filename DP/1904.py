# 성공
# 백준 Sliver3
# 메모리: 136732KB
# 시간: 460ms

import sys
sys.setrecursionlimit(10**6)
dp = {1:1, 2:2}

n = int(input())
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n])
