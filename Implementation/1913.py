# 성공
# 백준 silver3
# 메모리: 70172KB
# 시간: 916ms


n = int(input())
a = int(input())

arr = [[0]*n for _ in range(n)]

x, y = (n//2, n//2)
num = 1
cnt = 1
arr[x][y] = num

def pprint(arr, answer):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print(answer[0] + 1, answer[1] + 1)

answer = (x, y)
while True:
    for _ in range(cnt):
        x -= 1
        num += 1
        arr[x][y] = num
        if num == a:
            answer = (x,y)
        if num == n*n:
            pprint(arr, answer)
            exit(0)

    for _ in range(cnt):
        y += 1
        num += 1
        arr[x][y] = num
        if num == a:
            answer = (x, y)
    cnt += 1

    for _ in range(cnt):
        x += 1
        num += 1
        arr[x][y] = num
        if num == a:
            answer = (x, y)

    for _ in range(cnt):
        y -= 1
        num += 1
        arr[x][y] = num
        if num == a:
            answer = (x, y)
    cnt += 1

