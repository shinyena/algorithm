# 성공
# 백준 silver1
# 메모리: 31256KB
# 시간: 44ms

n = int(input())
arr = list(input().split())

max_number = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
min_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

max_answer = [-1]*(n+1)
min_answer = [-1]*(n+1)

i = 0
while i != n:
    if arr[i] == ">":
        max_answer[i] = max_number.pop(0)
        for j in range(i-1, -1, -1):
            if max_answer[j] == -1:
                max_answer[j] = max_number.pop(0)
    i += 1
for j in range(n, -1, -1):
    if max_answer[j] == -1:
        max_answer[j] = max_number.pop(0)

i = 0
while i != n:
    if arr[i] == "<":
        min_answer[i] = min_number.pop(0)
        for j in range(i-1, -1, -1):
            if min_answer[j] == -1:
                min_answer[j] = min_number.pop(0)
    i += 1
for j in range(n, -1, -1):
    if min_answer[j] == -1:
        min_answer[j] = min_number.pop(0)

for x in max_answer:
    print(x, end="")
print()
for x in min_answer:
    print(x, end="")