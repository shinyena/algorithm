n = int(input())
m = int(input())
s = input()

def check(start):
    for i in range(start, start+n*2):
        if i%2 == start%2:
            if s[i] != "O":
                return False
        else:
            if s[i] != "I":
                return False
    return True

answer = 0

for i in range(m-n*2):
    if s[i] == "I":
        if check(i+1):
            answer += 1

print(answer)