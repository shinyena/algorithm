# 성공
# 백준 silver4
# 메모리: 31256KB
# 시간: 44ms

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]


for x in range(min(n, m), -1, -1):
    for i in range(n-x):
        for j in range(m-x):
            if arr[i][j] == arr[i][j+x] == arr[i+x][j] == arr[i+x][j+x]:
                print((x+1)**2)
                exit(0)