import sys
from collections import deque
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, f.readline().rstrip().split())
    graph[i].append(j)


visited = [0 for _ in range(N+1)]
order = deque()
def dfs(i):
    global visited, order

    
    if visited[i]:
        return
    visited[i] = 1
    for j in graph[i]:
        dfs(j)
    order.appendleft(i)

for i in range(1,N+1):
    dfs(i)

print(' '.join(map(str, order)))