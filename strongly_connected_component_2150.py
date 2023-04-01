import sys
sys.setrecursionlimit(10**6)
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")
    
V, E = map(int, f.readline().rstrip().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    a, b = map(int, f.readline().rstrip().split())
    graph[a-1].append(b-1)
    
sccs = []

stack = []
node_id = 0
ids = [-1 for _ in range(V)]
on_stack = [-1 for _ in range(V)]

def search(node):
    global stack, node_id, ids, on_stack
    ids[node] = node_id
    res = node_id
    node_id += 1
    stack.append(node)
    on_stack[node] = 1
    
    for succ in graph[node]:
        if ids[succ] == -1:
            res = min(search(succ), res)
        elif on_stack[succ] != -1:
            res = min(res, ids[succ])
            
    if res == ids[node]:
        scc= []
        w = stack.pop()
        while w != node:
            on_stack[w] = -1
            scc.append(w+1)
            w = stack.pop()
        on_stack[w] = -1
        scc.append(w+1)
        sccs.append(scc)
        
    return res

for v in range(V):
    if ids[v] == -1:
        search(v)
        
for i in range(len(sccs)):
    sccs[i].sort()
    
sccs.sort()

print(len(sccs))
for scc in sccs:
    print(' '.join(map(str, scc)), end=' -1\n')