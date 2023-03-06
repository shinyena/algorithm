# 성공
# 백준 Sliver5
# 메모리: 31256KB
# 시간: 2820ms

import sys

n = int(input())
arr = set()
all_arr = set()
for i in range(1, 21):
    all_arr.add(i)

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "add":
        if int(cmd[1]) not in arr:
            arr.add(int(cmd[1]))

    elif cmd[0] == "remove":
        if int(cmd[1]) in arr:
            arr.remove(int(cmd[1]))

    elif cmd[0] == "check":
        if int(cmd[1]) in arr:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")

    elif cmd[0] == "toggle":
        if int(cmd[1]) in arr:
            arr.remove(int(cmd[1]))
        else:
            arr.add(int(cmd[1]))

    elif cmd[0] == "all":
        arr = all_arr

    elif cmd[0] == "empty":
        arr = set()