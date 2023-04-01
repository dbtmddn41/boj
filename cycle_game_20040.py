import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
n, m = map(int, f.readline().rstrip().split())

parent = list(range(n))
rank = [0 for _ in range(n)]
def get_root(i):
    if i != parent[i]:
        parent[i] = get_root(parent[i])
    return parent[i]

def union(i, j):
    root_i, root_j = get_root(i), get_root(j)
    if root_i != root_j:
        if rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_i] = root_j
            if rank[root_i] == rank[root_j]:
                rank[root_j] += 1
        return 1
    return 0

i=0
while i < m:
    a, b = map(int, f.readline().rstrip().split())
    if not union(a-1, b-1):
        break
    i += 1

if i == m:
    i = -1
print(i+1)