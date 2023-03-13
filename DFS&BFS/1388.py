n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(m)]

def dfs_row(i, j):
    visited[i][j] = True
    if i<n and j+1<m:
        if arr[i][j+1] == "-" and not visited[i][j+1]:
            dfs_row(i, j+1)
def dfs_col(i, j):
    visited[i][j] = True
    if i+1<n and j<m:
        if arr[i+1][j] == "|" and not visited[i+1][j]:
            dfs_col(i+1, j)

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "-" and not visited[i][j]:
            cnt += 1
            dfs_row(i, j)
        elif arr[i][j] == "|" and not visited[i][j]:
            cnt += 1
            dfs_col(i, j)

print(cnt)