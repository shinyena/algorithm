# 성공
# 백준 silver4
# 메모리: 31388KB
# 시간: 1344ms

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = set()

def find(brr):
    max = 1
    for i in range(len(brr)-3):
        x = brr[i][0]
        y = brr[i][1]
        for d in range(min(n-x, m-y)):
            if (x+d,y) in brr and (x,y+d) in brr and (x+d,y+d) in brr:
                if (d+1)*(d+1) > max:
                    max = (d+1)*(d+1)
    return max


answer = 1
for x in range(10):
    brr = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == x:
                brr.append((i, j))
    if len(brr)>=4:
        if find(brr)>answer:
            answer = find(brr)
print(answer)