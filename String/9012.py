# 성공
# 백준 silver4
# 메모리: 31256KB
# 시간: 40ms
import sys

n = int(input())
for _ in range(n):
    vps = sys.stdin.readline().rstrip()
    while "()" in vps:
        vps = vps.replace("()","")
    if len(vps)>0:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")