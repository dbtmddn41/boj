import sys
import heapq
from collections import deque
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
def remove_edges():
    global S, trace, roads
    q = deque()
    curr = D
    q.append(curr)
    while q:
        curr = q.popleft()
        for i in trace[curr]:
            if curr in roads[i]:
                del roads[i][curr]
                q.append(i)
    del q

while True:
    N, M = map(int, f.readline().rstrip().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, f.readline().rstrip().split())
    roads = [dict() for _ in range(N)]
    
    for _ in range(M):
        U, V, P = map(int, f.readline().rstrip().split())
        roads[U][V] = P

    heap = []
    
    dist = [float('inf') for _ in range(N)]
    dist[S] = 0
    for v, c in roads[S].items():
        heapq.heappush(heap, (c, S, v))
    
    trace = [() for _ in range(N)]
    while heap:
        cost, u, v= heapq.heappop(heap)
        if dist[v] < dist[u] + cost:
            continue
        elif dist[v] > dist[u] + cost:
            trace[v] = (u,)
        elif dist[v] == dist[u] + cost:
            trace[v] += (u,)
            continue
        dist[v] = dist[u] + cost

        for to, c in roads[v].items():
                heapq.heappush(heap, (c, v, to))
    remove_edges()
    del dist
    
    dist = [float('inf') for _ in range(N)]
    dist[S] = 0
    for v, c in roads[S].items():
        heapq.heappush(heap, (c, S, v))
    while heap:
        cost, u, v = heapq.heappop(heap)
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            for to, c in roads[v].items():
                    heapq.heappush(heap, (c, v, to))
    if dist[D] == float('inf'):
        dist[D] = -1
    print(dist[D])
    del dist, heap