import sys
from collections import deque

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
final_order = []
q = deque()
length = 0
for r in root:
    q.append(r)
    while q:
        node = q.popleft()
        final_order.append(node+1)
        for child in graph[node]:
            degree[child] -= 1
            if degree[child] == 0:
                q.append(child)

if len(final_order) != N:
    print(0)
else:
    print('\n'.join(map(str, final_order)), end='')