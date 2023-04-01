import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N, M = map(int, f.readline().rstrip().split())
graph = [() for _ in range(N)]
degree = [0 for _ in range(N)]

for i in range(M):
    order = tuple(map(int, f.readline().rstrip().split()))
    for j in range(1, order[0]):
        graph[order[j]-1] += (order[j+1]-1,)
        degree[order[j+1]-1] += 1

root = [i for i in range(N) if degree[i] == 0]
visited = [0 for _ in range(N)]
final_order = ''
def dfs(node, parents):
    global visited, final_order, graph
    if (parents >> node) & 1:
        return -1
    if visited[node] == 1:
        return 0
    visited[node] = 1
    
    for child in graph[node]:
        res = dfs(child, parents | (1 << node))
        if res == -1:
            return -1
    final_order = str(node+1)+'\n'+final_order
    return 0
        
res = -1
for r in root:
    res = dfs(r, 0)
    if res == -1:
        break
if res == -1:
    print(0)
else:
    print(final_order, end='')