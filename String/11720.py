n = int(input())
s = int(input())
sum = 0

for i in range(n):
    sum += s%10
    s//=10

print(sum)