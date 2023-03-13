from pprint import pprint

na, ma, nb, mb = map(int, input().split())
graph_a = [[0]*(na+1) for _ in range(na+1)]
graph_b = [[0]*(nb+1) for _ in range(nb+1)]
for _ in range(ma):
    u, v, d = map(int, input().split())
    graph_a[u][v] = d
    graph_a[v][u] = d
for _ in range(mb):
    u, v, d = map(int, input().split())
    graph_b[u][v] = d
    graph_b[v][u] = d

pprint(graph_a, width=20)
print()
pprint(graph_b, width=20)