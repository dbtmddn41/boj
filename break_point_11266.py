import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

V, E = map(int, f.readline().rstrip().split())
edges = E
graph = [[] for _ in range(V)]

for _ in range(E):
    a, b = map(int, f.readline().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
break_points = [0 for _ in range(V)]
node_id = 0
ids = [-1 for _ in range(V)]

def search(node, root):
    global node_id, ids, break_points
    ids[node] = node_id
    res = node_id
    node_id += 1
    
    child = 0
    for succ in graph[node]:
        if ids[succ] == -1:
            child += 1
            lowest = search(succ, root)
            res = min(res, lowest)
            if node != root and lowest >= ids[node]:
                break_points[node] = 1
        else:
            res = min(res, ids[succ])

    if root == node:
        if child >= 2:
                break_points[node] = 1
    return res

for v in range(V):
    if ids[v] == -1:
        search(v, v)

break_points = [i+1 for i in range(V) if break_points[i] == 1]
break_points.sort()
print(len(break_points))
if len(break_points) > 0:
    print(' '.join(map(str, break_points)))