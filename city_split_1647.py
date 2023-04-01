import sys
import heapq

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    i, j, c = map(int, f.readline().rstrip().split())
    graph[i-1].append((c, j-1))
    graph[j-1].append((c, i-1))

visited = {0}
curr = 0
heap = []
tot_cost = 0
max_cost = 0
while len(visited) < N:
    for cost, node in graph[curr]:
        if node not in visited:
            heapq.heappush(heap, (cost, node))
    cost, curr = heapq.heappop(heap)
    while curr in visited:
        cost, curr = heapq.heappop(heap)
    tot_cost += cost
    max_cost = max(max_cost, cost)
    visited.add(curr)

print(tot_cost-max_cost)

    