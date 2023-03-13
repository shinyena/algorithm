n = int(input())
price = list(map(int, input().split()))

max = 0
for i in range(len(price)):
    if price[i]/(i+1)*n > max:
        max = price[i]/(i+1)*n

print(int(max))