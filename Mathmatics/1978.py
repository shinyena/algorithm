# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 40ms

def check(num):
    if num == (0 or 1):
        return False

    for i in range(2, num):
        if num%i == 0:
            return False
    return True

n = int(input())
arr = []
arr = list(map(int, input().split()))

answer = 0
for a in arr:
    if check(a):
        answer += 1

print(answer)
