a, b, c = map(int, input().split())

cnt = len(format(b, "b"))
if "0" in str(format(b, "b")):
    cnt -= 1
num = int("0b" + "1" + "0"*cnt, 2)
answer = a

for i in range(cnt):
    answer *= answer
for _ in range(num - b):
    answer *= a
print(answer%c)
# 10 2147483647 12
# 3543 3453543 3636