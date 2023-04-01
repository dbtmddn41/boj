import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N = int(f.readline().rstrip())
planets = []
for i in range(N):
    x,y,z = map(int, f.readline().rstrip().split())
    planets.append((x,y,z,i))

dists = []
for xyz in range(3):
    planets.sort(key=lambda x: x[xyz])
    for i in range(1, N):
        dists.append((planets[i][xyz]-planets[i-1][xyz], planets[i-1][3], planets[i][3]))
dists.sort()
            
rank = [0 for _ in range(N)]
parent = list(range(N))

def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find_root(x), find_root(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
        return 1
    return 0


tot_dist = 0
cnt = 0
for i in range(3*(N+1)):
    dist, n1, n2 = dists[i]
    if union(n1, n2):
        tot_dist += dist
        cnt += 1
    if cnt == N - 1:
        break
    
print(tot_dist)