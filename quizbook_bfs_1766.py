import sys
import heapq
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

tree = [() for _ in range(N)]
degree = [0 for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x)-1, f.readline().rstrip().split())
    tree[i] += (j,)
    degree[j] += 1

roots = [i for i in range(N) if degree[i] == 0]

q = []
ans = ''
for root in roots:
    heapq.heappush(q, root)
    
while q:
    node = heapq.heappop(q)
    ans += str(node+1) + ' '
    for child in tree[node]:
        degree[child] -= 1
        if degree[child] == 0:
            heapq.heappush(q, child)

print(ans.rstrip())