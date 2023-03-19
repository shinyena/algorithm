# 성공
# 백준 Sliver2
# 메모리: 34104KB
# 시간: 136ms

from collections import deque

a, b = map(int, input().split())

queue = deque([(a,0)])

while queue:
    (x, cnt) = queue.popleft()
    cnt += 1
    if x == b:
        print(cnt)
        exit(0)
    if x*2<=b:
        queue.append((x*2, cnt))
    if int(str(x) + "1")<=b:
        queue.append((int(str(x) + "1"), cnt))
print(-1)