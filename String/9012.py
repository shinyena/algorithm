def isvps(ps):
    for i in range(1, len(ps)+1):
        left = ps[:i].count("(")
        right = ps[:i].count(")")
        if left<right:
            return "NO"
    if left>right:
        return "NO"
    return "YES"


n = int(input())
for i in range(n):
    print(isvps(input()))