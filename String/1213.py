# 성공
# 백준 Sliver3
# 메모리: 31256KB
# 시간: 64ms

name = list(input().strip())
dic = {}
for a in range(65, 91):
    dic[chr(a)] = 0
for s in name:
    dic[s] += 1

answer = ""
odd_cnt = 0
odd_str = ""
for d in dic.keys():
    if dic[d]%2 == 0:
        answer += d*(dic[d]//2)
    else:
        odd_cnt += 1
        if odd_cnt > 1:
            print("I'm Sorry Hansoo")
            exit(0)
        odd_str = d
        answer += d*((dic[d]-1) // 2)

print(answer + odd_str + answer[::-1])

