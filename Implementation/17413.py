# 성공
# 백준 Sliver3
# 메모리: 31256KB
# 시간: 44ms

s = input().replace("<","A<").replace(">",">A")
arr = s.split("A")

for a in arr:
    if "<" in a and ">" in a:
        print(a, end="")
    else:
        brr = a.split(" ")
        for i in range(len(brr)):
            if i != len(brr) - 1:
                print(brr[i][::-1], end=" ")
            else:
                print(brr[i][::-1], end="")