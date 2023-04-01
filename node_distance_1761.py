import sys
from math import ceil, log2, floor
from collections import deque

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
parents = [0 for _ in range(N+1)]
depths = [0 for _ in range(N+1)]
q = deque()

q.append((1, 1))
while q:
    node, p = q.popleft()
    if spt[node][0] != 0:
        continue
    depths[node] = depths[p] + 1
    spt[node][0] = p
    for j in range(1, max_2n+1):
        spt[node][j] = spt[spt[node][j-1]][j-1]
    for child, dist in nodes[node]:
        if child != p:
            parents[child] = (node, dist)
            q.append((child, node))
            
"""
def get_spt(p, depth):
    global parents, spt, depths

    depths[p] = depth
    for child, dist in nodes[p]:
        if spt[child][0] != 0:
            continue
        spt[child][0] = p
        parents[child] = (p, dist)
        for j in range(1, max_2n+1):
            spt[child][j] = spt[spt[child][j-1]][j-1]
        get_spt(child, depth+1)

spt[1][0] = 1
get_spt(1, 0)
="""

def get_lca(a, b):
    d_depth = depths[a] - depths[b]
    if d_depth < 0:
        a, b = b, a
        d_depth *= -1
    while d_depth != 0:
        a = spt[a][int(floor(log2(d_depth)))]
        d_depth = depths[a] - depths[b]
    
    k = max_2n-1
    while a != b:
        while spt[a][k] == spt[b][k] and k > 0:
            k -= 1
        a, b = spt[a][k], spt[b][k]
    return a

def get_dist(a, b):
    p = get_lca(a, b)
    dist = 0
    while p != a:
        a, d = parents[a]
        dist += d

    while p != b:
        b, d = parents[b]
        dist += d

    return dist

M = int(f.readline().rstrip())

for _ in range(M):
    a, b = map(int, f.readline().rstrip().split())
    print(get_dist(a, b))