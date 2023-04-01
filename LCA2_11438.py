import sys
from math import ceil, log2, floor
sys.setrecursionlimit(20000)

is_boj = 0
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
spt = [[0 for _ in range(max_2n+1)] for _ in range(N+1)]

depths = [0 for _ in range(N+1)]

def get_parents(p, depth):
    global parents, spt, depths
    
    depths[p] = depth
    for child in nodes[p]:
        if spt[child][0] != 0:
            continue
        spt[child][0] = p
        
        get_parents(child, depth+1)
        
spt[1][0] = 1
get_parents(1, 0)

del nodes
for i in range(1, N+1):
    for j in range(1, max_2n):
        spt[i][j] = spt[spt[i][j-1]][j-1]
        
def get_lca(a,b):
    d_depth = depths[a] - depths[b]
    if d_depth < 0:
        a, b = b, a
        d_depth *= -1
    while d_depth > 0:
        a = spt[a][floor(log2(d_depth))]
        d_depth = depths[a] - depths[b]
    return lca(a, b, max_2n-1)

def lca(a, b, k):
    if a == b:
        return a
    
    while spt[a][k] == spt[b][k] and k > 0:
        k -= 1
    a, b = spt[a][k], spt[b][k]
    return lca(a, b, k)


M = int(f.readline().rstrip())
for _ in range(M):
    a, b = map(int, f.readline().rstrip().split())
    print(get_lca(a, b))