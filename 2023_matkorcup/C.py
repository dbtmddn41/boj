import sys
import os

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")
 
D, M = map(int, f.readline().rstrip().split())

point = [[] for _ in range(D)]

for _ in range(M):
    p = tuple(map(int, f.readline().rstrip().split()))
    for i in range(D):
        point[i].append(p[i])
        
for i in range(D):
    point[i].sort()
    
s = ''
idx = M // 2
s = ''
dist = 0
for i in range(D):
    p = point[i][idx]
    s += str(p) + ' '
    for j in range(M):
        dist += abs(point[i][j] - p)
    
print(dist, s[:-1], sep='\n')