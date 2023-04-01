import sys
import heapq
import bisect

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
N, K = map(int, f.readline().rstrip().split())

gems = []
for _ in range(N):
    m, v = map(int, f.readline().rstrip().split())
    heapq.heappush(gems, (m, v))

bags = []
for _ in range(K):
    #bags.append(int(f.readline().rstrip()))
    heapq.heappush(bags, int(f.readline().rstrip()))
    

bags.sort()


tot_v = 0
curr_gems = []
while bags:
    bag = heapq.heappop(bags)
    while gems and gems[0][0] <= bag:
        m, v = heapq.heappop(gems)
        heapq.heappush(curr_gems, -v)
    if curr_gems:
        tot_v -= heapq.heappop(curr_gems)
    elif not gems:
        break
print(tot_v)