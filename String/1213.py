# 성공
# 백준 Sliver3
# 메모리: 31256KB
# 시간: 64ms

name = list(input().strip())
dic = {}
for s in name:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

answer = ""
odd_str = ""
for d in sorted(dic.keys()):
    if dic[d]%2 != 0:
        if odd_str != "":
            print("I'm Sorry Hansoo")
            exit(0)
        odd_str = d
    answer += d*(dic[d] // 2)

print(answer + odd_str + answer[::-1])

