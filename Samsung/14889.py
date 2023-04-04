# 성공
# 백준 silver2
# 메모리: 31256KB
# 시간: 1356ms
import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
team = []
answer = float("inf")

def cal(start):
    link = list(set([x for x in range(n)]) - set(start))
    start_sum = 0
    link_sum = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            start_sum += arr[start[i]][start[j]] + arr[start[j]][start[i]]
            link_sum += arr[link[i]][link[j]] + arr[link[j]][link[i]]
    return abs(start_sum-link_sum)

def back(start):
    global answer
    if len(team) == n//2:
        answer = min(answer, cal(team))
    if answer == 0:
        print(0)
        exit(0)
    for i in range(start+1, n):
        if len(team)<n//2:
            team.append(i)
            back(i)
            team.pop()



back(0)
print(answer)