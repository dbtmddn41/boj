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
break_points = []
node_id = 0
ids = [-1 for _ in range(V)]

def search(node, parent):
    global node_id, ids, break_points
    ids[node] = node_id
    res = node_id
    node_id += 1
    
    for succ in graph[node]:
        if succ == parent:
            continue
        if ids[succ] == -1:
            lowest = search(succ, node)
            res = min(res, lowest)
            if lowest > ids[node]:
                break_points.append(tuple(sorted((succ+1, node+1))))
        else:
            res = min(res, ids[succ])

    return res

for v in range(V):
    if ids[v] == -1:
        search(v, v)

break_points.sort()
print(len(break_points))
if len(break_points) > 0:
    for a, b in break_points:
        print(a, b)