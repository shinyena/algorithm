n = int(input())
arr = list(map(int, input().split()))

i = n-1
while i != 0:
    if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        arr = arr[:i] + sorted(arr[i:], reverse=True)
        for a in arr:
            print(a, end=" ")
        exit(0)
    else:
        i -= 1
print(-1)