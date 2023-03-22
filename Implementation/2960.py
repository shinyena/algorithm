# 성공
# 백준 Sliver4
# 메모리: 31256KB
# 시간: 48ms

n, k = map(int, input().split())
numbers = [i for i in range(2, n+1)]

cnt = 0
while cnt != k:
    p = numbers.pop(0)
    cnt += 1

    for number in numbers:
        if number%p == 0:
            numbers.remove(number)
            cnt += 1

            if cnt == k:
                p = number
                break

print(p)