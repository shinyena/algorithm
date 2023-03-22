# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 40ms

n = input()
a = n.split("0")
b = n.split("1")
print(min(len(a)-a.count(''), len(b)-b.count('')))