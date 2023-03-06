# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 44ms

n = int(input())
arr = {6:0, 9:0}
while n != 0:
    if n%10 not in arr:
        arr[n%10] = 1
    else:
        arr[n%10] += 1
    n //= 10

if (arr[6] + arr[9]) %2 == 0:
    tmp = (arr[6] + arr[9])//2
    arr[6] = arr[9] = tmp
else:
    tmp = (arr[6] + arr[9]) // 2
    arr[6] = tmp
    arr[9] = tmp + 1

print(max(arr.values()))
