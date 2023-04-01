import sys
import math
import heapq

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

n = int(f.readline().rstrip())

stars = []

for i in range(n):
    x, y = map(float, f.readline().rstrip().split())
    stars.append((x,y))

visited = {0}
heap = []
curr = 0
tot_dist = 0
while len(visited) < len(stars):
    for i in range(len(stars)):
        if i not in visited and i != stars:
            dist = distance(stars[i], stars[curr])
            heapq.heappush(heap, (dist, i))
    dist, curr = heapq.heappop(heap)
    while curr in visited:
        dist, curr = heapq.heappop(heap)
    tot_dist += dist
    visited.add(curr)

print(tot_dist)