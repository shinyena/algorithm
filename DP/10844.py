arr = {0:[1], 1:[0,2], 2:[1,3], 3:[2,4], 4:[3,5],
      5:[4,6], 6:[5,7], 7:[6,8], 8:[7,9], 9:[8]}

# cnt = 0
# for i in range(1,10):
#     for j in arr[i]:
#         for k in arr[j]:
#             cnt += 1
# print(cnt)
def fn(x, cnt):
    for a in arr[x]:
        cnt += 1
        return (a, cnt)

n = int(input())
cnt = 0
for i in range(1, 10):
    k = i
    for _ in range(n):
        print(k, end="")
        k, cnt = fn(k, cnt)
    print()

print("=>")
print(cnt)
