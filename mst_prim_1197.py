import sys
import heapq

is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

V, E = map(int, f.readline().rstrip().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    i, j, c = map(int, f.readline().rstrip().split())
    graph[i].append((c, j))
    graph[j].append((c, i))
heap = []
for x in graph[1]:
    heapq.heappush(heap, x)
    
included = {1}
tot_c = 0
while len(included) < V:
    c, i = heapq.heappop(heap)
    if i in included:
        continue
    tot_c += c
    for c_j, j in graph[i]:
        if j not in included:
            heapq.heappush(heap, (c_j, j))
    included |= {i}

print(tot_c)