# 성공
# 백준 silver2
# 메모리: 43660KB
# 시간: 128ms

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = {0:arr[0]}
answer = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    answer = max(answer, dp[i])


print(answer)