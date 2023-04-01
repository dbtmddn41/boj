import sys
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

n = int(f.readline().rstrip())
points = []
for _ in range(n):
    x, y = map(int, f.readline().rstrip().split())
    points.append((x, y))

points.sort()
def get_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

near_points = deque()
min_dist = get_dist(points[0], points[1])
near_points.append(points[0])

for i in range(2, n):
    near_points.append(points[i-1])
    if near_points:
        while (points[i][0] - near_points[0][0])**2 >= min_dist:
            near_points.popleft()
            if not near_points:
                break
    
    for p in near_points:
        if (p[1] - points[i][1])**2 < min_dist:
            min_dist = min(min_dist, get_dist(p, points[i]))

print(min_dist)