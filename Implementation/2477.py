# 성공
# 백준 silver2
# 메모리: 31256KB
# 시간: 44ms

n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
brr = []
x = 0
y = 0
for i in range(6):
    if arr[i][0] == 1:
        y += arr[i][1]
    elif arr[i][0] == 2:
        y -= arr[i][1]
    elif arr[i][0] == 3:
        x += arr[i][1]
    else:
        x -= arr[i][1]
    brr.append((x, y))

max_x = brr[0][0]
min_x = brr[0][0]
max_y = brr[0][1]
min_y = brr[0][1]
for (x, y) in brr:
    if x>max_x:
        max_x = x
    if x<min_x:
        min_x = x
    if y>max_y:
        max_y = y
    if y<min_y:
        min_y = y

x1 = 0
y1 = 0
for (x, y) in brr:
    if x not in (max_x, min_x) and y not in (max_y, min_y):
        (x1, y1) = (x, y)
x2 = 0
y2 = 0
if (max_x, min_y) not in brr:
    (x2, y2) = (max_x, min_y)
if (min_x, max_y) not in brr:
    (x2, y2) = (min_x, max_y)
if (max_x, max_y) not in brr:
    (x2, y2) = (max_x, max_y)
if (min_x, min_y) not in brr:
    (x2, y2) = (min_x, min_y)

print(((max_x-min_x)*(max_y-min_y) - abs(x1-x2)*abs(y1-y2))*n)