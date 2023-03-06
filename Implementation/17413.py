# 성공
# 백준 Sliver3
# 메모리: 32820KB
# 시간: 104ms


s = input()

tmp = []
idx = 0
while idx != len(s):
    if s[idx] == " ":
        if len(tmp) != 0:
            print(''.join(str(t) for t in reversed(tmp)), end="")
            tmp = []
        print(" ", end="")
    elif s[idx] == "<":
        if len(tmp) != 0:
            print(''.join(str(t) for t in reversed(tmp)), end="")
            tmp = []
        print(s[idx], end="")
        while s[idx] != ">":
            idx += 1
            print(s[idx], end="")
    else:
        tmp.append(s[idx])
    idx += 1

if len(tmp) != 0:
    print(''.join(str(t) for t in reversed(tmp)), end="")
