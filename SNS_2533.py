import sys
from collections import deque
sys.setrecursionlimit(10**6)

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
    
q = deque()
tree = [set() for _ in range(N+1)]

q.append((1, 0))
while q:
    node, p = q.pop()
    tree[p].add(node)
    for child in nodes[node]:
        if child != p:
            q.append((child, node))
            
del nodes, q
DP = [[0 for _ in range(2)] for _ in range(N+1)]

def search(node, is_ea):
    if DP[node][is_ea] != 0:
        return DP[node][is_ea]
    
    tot_ea = is_ea
    for child in tree[node]:
        res1 = N + 1
        if is_ea:
            res1 = search(child, 0)
        res2 = search(child, 1)
        tot_ea += min(res1, res2)
    DP[node][is_ea] = tot_ea
    return tot_ea

print(min(search(1, 0), search(1, 1)))