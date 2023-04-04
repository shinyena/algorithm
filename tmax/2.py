from itertools import combinations
def solution(n, problems):
    p = [i for i in range(1, len(problems)+1)]
    arr = [[]*len(problems) for _ in range(len(problems))]
    for i in range(len(problems)):
        for j in range(n):
            if problems[i][j] == 1:
                arr[i].append(j)

    for idx in range(1, len(problems)):
        for comb in list(combinations(p, idx)):
            visited = [False]*n
            for i in range(idx):
                for x in arr[comb[i]-1]:
                    visited[x] = True
            if False not in visited:
                return list(comb)
    return p





print(solution(5, [[1, 1, 0, 0, 1], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1]]))
print(solution(4, [[0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]))
print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1]]))