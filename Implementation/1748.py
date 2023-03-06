# 성공
# 백준 Sliver4
# 메모리: 31256KB
# 시간: 40ms


n = int(input())
answer = 0

for i in range(1, len(str(n))):
    answer += i * 9 * 10**(i-1)

answer += len(str(n)) * (n - 10**(len(str(n))-1) + 1)
print(answer)