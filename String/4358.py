# 성공
# 백준 Sliver2
# 메모리: 31256KB
# 시간: 540ms

import sys

trees = {}
sum = 0
while True:
    try:
        t = sys.stdin.readline().rstrip()
        if t == "":
            break
        if t not in trees:
            trees[t] = 1
        else:
            trees[t] += 1
        sum += 1
    except:
        break

trees = sorted(trees.items())
for t in trees:
    print("%s %.4f" %(t[0], t[1]/sum*100))