# 성공
# 백준 silver2
# 메모리: 57116KB
# 시간: 152ms
# 풀이: 개인 역량 계산하기
import sys
from itertools import combinations

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
person = [sum(i)+sum(j) for i,j in zip(arr, zip(*arr))]
total = sum(person)
answer = total

comb_person = list(combinations(person, n//2))
for comb in comb_person[:len(comb_person)//2]:
    answer = min(answer, abs(total-sum(comb)-sum(comb)))
    if answer == 0:
        break

print(answer//2)