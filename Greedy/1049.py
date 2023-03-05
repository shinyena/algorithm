# 성공
# 백준 Sliver4
# 메모리: 31256KB
# 시간: 44ms

n, m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

arr.sort()
min1 = arr[0][0]

arr.sort(key=lambda x: x[1])
min2 = arr[0][1]

if min1/6 >= min2:
    print(min2*n)
else:
    x = min1*(n//6) + min2*(n%6)
    y = min1*(n//6 + 1)
    print(min(x, y))