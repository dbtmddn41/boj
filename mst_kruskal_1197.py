import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

V, E = map(int, f.readline().rstrip().split())
edges = []

for _ in range(E):
    i, j, c = map(int, f.readline().rstrip().split())
    edges.append((c, i-1, j-1))
edges.sort()

parent = list(range(V))
rank = [0 for _ in range(V)]

def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find_root(x), find_root(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
        return 1
    return 0

tot_c = 0
for c, i, j in edges:
    res = union(i, j)
    if res:
        tot_c += c

print(tot_c)