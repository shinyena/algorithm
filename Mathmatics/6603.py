# 성공
# 백준 Sliver2
# 메모리: 31256KB
# 시간: 48ms

from itertools import combinations
arr = []

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.pop(0)
    brr = list(combinations(arr, 6))
    for i in range(len(brr)):
        for j in range(len(brr[i])):
            print(brr[i][j], end=" ")
        print()
    print()