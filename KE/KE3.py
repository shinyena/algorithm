n = int(input())
s = input()
answer = [0]*27

for i in range(n):
    for j in range(i+1, n+1):
        if answer[len(set(s[i:j]))] < j-i:
            answer[len(set(s[i:j]))] = j-i

for i in range(1, 27):
    print(answer[i])