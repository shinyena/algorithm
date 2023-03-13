from sys import stdin
def find(arr):
    arr.sort()
    answer = arr[0][1]
    if arr[len(arr)-1][1] != 1 and arr[len(arr)-1][1] < arr[0][1]:
        answer -= 1
    return answer

t = int(input())
for _ in range(t):
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))
    print(find(arr))
    
# 반례
# 1
# 4
# 1 4
# 2 2
# 3 3
# 4 1