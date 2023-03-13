import sys
sys.setrecursionlimit(1000000)

decimal = set([])
def check(num):
    for d in decimal:
        if num%d == 0:
            return False
    return True

m, n = map(int, input().split())

answer = ""
for i in range(m, n+1):
    if i in (0, 1):
        continue
    elif i in (2, 3, 5, 7):
        print(i)
    elif i in decimal:
        print(i)
    elif i%2 == 0 or i%3 == 0 or i%5 ==0 or i%7 ==0:
        continue
    else:
        if check(i):
            decimal.add(i)
            print(i)

print(answer)
