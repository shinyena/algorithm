# 성공
# 백준 silver1
# 메모리: 526812KB
# 시간: 1368ms

from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
p, s, m, d = map(int, input().split())
opr = []
for _ in range(p):
    opr.append("+")
for _ in range(s):
    opr.append("-")
for _ in range(m):
    opr.append("*")
for _ in range(d):
    opr.append("/")

def cal(brr):
    answer = arr[0]
    index = 1
    while index != n:
        if brr[index-1] == "+":
            answer += arr[index]
        elif brr[index-1] == "-":
            answer -= arr[index]
        elif brr[index-1] == "*":
            answer *= arr[index]
        else:
            if answer<0:
                answer = (-answer)//arr[index]
                answer = -answer
            else:
                answer //= arr[index]
        index += 1
    return answer

max = float("-inf")
min = float("inf")
for c in set(list(permutations(opr, n-1))):
    if cal(c) > max:
        max = cal(c)
    if cal(c) < min:
        min = cal(c)

print(max)
print(min)