n, m = map(int, input().split())
arr = [[]*n for _ in range(n)]
total_sum = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))
    total_sum += sum(arr[i])

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())

    if i==j==1 and x==n and y==m:
        print(total_sum)
    elif (x-i+1)*(y-j+1) > m*n//2:
        print()
    else:
        sum = 0
        for a in range(i-1, x):
            for b in range(j-1, y):
                sum += arr[a][b]
        print(sum)