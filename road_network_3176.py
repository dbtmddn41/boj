import sys
from collections import deque
from math import ceil, log2, floor

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N = int(f.readline().rstrip())

nodes = [() for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, f.readline().rstrip().split())
    nodes[a] += ((b, d),)
    nodes[b] += ((a, d),)

max_2n = int(ceil(log2(N)))
spt = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]
min_spt = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]
max_spt = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]

depths = [0 for _ in range(N+1)]
q = deque()

q.append((1, 1, 0))
while q:
    node, p, dist = q.popleft()
    if spt[node][0] != 0:
        continue
    depths[node] = depths[p] + 1
    spt[node][0] = p
    min_spt[node][0], max_spt[node][0] = dist, dist
    for j in range(1, max_2n+1):
        spt[node][j] = spt[spt[node][j-1]][j-1]
        min_spt[node][j] = min(min_spt[node][j-1], min_spt[spt[node][j-1]][j-1])
        max_spt[node][j] = max(max_spt[node][j-1], max_spt[spt[node][j-1]][j-1])
    for child, dist in nodes[node]:
        if child != p:
            q.append((child, node, dist))
            
def get_lca(a,b):
    global max_2n
    
    d_depth = depths[a] - depths[b]
    if d_depth < 0:
        a, b = b, a
        d_depth *= -1
    rmin = float('inf')
    rmax = 0
    
    while d_depth != 0:
        i = int(floor(log2(d_depth)))
        rmin = min(rmin, min_spt[a][i])
        rmax = max(rmax, max_spt[a][i])
        a = spt[a][i]
        d_depth = depths[a] - depths[b]
        
    k = max_2n-1
    while a != b:
        while spt[a][k] == spt[b][k] and k > 0:
            k -= 1
        rmin = min(rmin, min_spt[a][k], min_spt[b][k])
        rmax = max(rmax, max_spt[a][k], max_spt[b][k])
        a, b = spt[a][k], spt[b][k]
    return rmin, rmax
    
K = int(f.readline().rstrip())
for _ in range(K):
    a, b = map(int, f.readline().rstrip().split())
    print(*get_lca(a,b))
        