import sys
from math import ceil, log2
from collections import deque

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N = int(f.readline().rstrip())

nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, f.readline().rstrip().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
max_2n = ceil(log2(N))
spt = [[0 for _ in range(max_2n)] for _ in range(N+1)]

depths = [0 for _ in range(N+1)]
q = deque()

q.append((1, 1))
while q:
    node, p = q.popleft()
    if spt[node][0] != 0:
        continue
    depths[node] = depths[p] + 1
    spt[node][0] = p
    for j in range(1, max_2n):
        spt[node][j] = spt[spt[node][j-1]][j-1]
    for child in nodes[node]:
        if child != p:
            q.append((child, node))
        
del q
del nodes
        
def get_lca(a,b):
    d_depth = depths[a] - depths[b]
    if d_depth < 0:
        a, b = b, a
        d_depth *= -1
    """while d_depth > 0:
        a = spt[a][floor(log2(d_depth))]
        d_depth = depths[a] - depths[b]"""
    for i in range(max_2n-1, -1, -1):
        if d_depth >= (1 << i):
            a = spt[a][i]
            d_depth = depths[a] - depths[b]
    k = max_2n - 1
    while a != b:
        while spt[a][k] == spt[b][k] and k > 0:
            k -= 1
        a, b = spt[a][k], spt[b][k]
    return a

M = int(f.readline().rstrip())
for _ in range(M):
    a, b = map(int, f.readline().rstrip().split())
    print(get_lca(a, b))