# 성공
# 백준 silver5
# 메모리: 114328KB
# 시간: 148ms

n = int(input())
cnt = 0
index = 2
(x,y) = (0,0)
while cnt != n:
    if index%2 == 0:
        for i in range(index-1, 0, -1):
            (x,y) = (i, index-i)
            cnt += 1
            if cnt == n:
                break
    else:
        for i in range(1, index):
            (x,y) = (i, index-i)
            cnt += 1
            if cnt == n:
                break
    index += 1

print(str(x) + "/" + str(y))
