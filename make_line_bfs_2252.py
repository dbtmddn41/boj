import sys
from collections import deque
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

degree = [0 for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, f.readline().rstrip().split())
    graph[i].append(j)
    degree[j] += 1
    
visited = [0 for _ in range(N+1)]
dq = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        dq.append(i)
        visited[i] = 1

order = []     
while dq:
    i = dq.popleft()
    order.append(i)
    for j in graph[i]:
        if visited[j]:
            continue
        degree[j] -= 1
        if degree[j] == 0:
            visited[j] = 1
            dq.append(j)
            
print(' '.join(map(str, order)))