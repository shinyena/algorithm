# 성공
# 백준 silver4
# 메모리: 31256KB
# 시간: 44ms


arr = [list(map(int, input().split())) for _ in range(5)]
diag = [[(0,0), (1,1), (2,2), (3,3), (4,4)],
        [(0,4), (1,3), (2,2), (3,1), (4,0)]]

def update(num):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = "x"

def find():
    bingo = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[i][j] == "x":
                cnt += 1
        if cnt == 5:
            bingo += 1

        cnt = 0
        for j in range(5):
            if arr[j][i] == "x":
                cnt += 1
        if cnt == 5:
            bingo += 1

    for i in range(2):
        cnt = 0
        for j in range(5):
            (x,y) = diag[i][j]
            if arr[x][y] == "x":
                cnt += 1
        if cnt == 5:
            bingo += 1
    return bingo

brr = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        update(brr[i][j])
        if find() >= 3:
            print(i*5 + j + 1)
            exit(0)