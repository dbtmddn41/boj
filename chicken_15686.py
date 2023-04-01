import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N, M = map(int, f.readline().rstrip().split())

chicken = []
home = []

for i in range(N):
	line = tuple(map(int, f.readline().rstrip().split()))
	for j in range(N):
		if line[j] == 1:
			home.append((i, j))
		elif line[j] == 2:
			chicken.append((i, j))

num_chick = len(chicken)
num_home = len(home)
closest = []
closest_dist = []

for h in home:
	happy = 2*N
	for j in range(num_chick):
		distance = abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1])
		if distance < happy:
			closest_idx = j
			happy = distance
	closest.append(closest_idx)
	closest_dist.append(happy)
	
def get_chic_dist(mask):
	dist = 0
	
	for i in range(num_home):
		if (1 << closest[i]) & mask:
			dist += closest_dist[i]
		else:
			happy = 2*N
			for j in range(num_chick):
				if not ((mask >> j) & 1):
					continue
				distance = abs(home[i][0] - chicken[j][0]) + abs(home[i][1] - chicken[j][1])
				if distance < happy:
					happy = distance
			dist += happy
	return dist

def search(mask, before, depth):
    dist = get_chic_dist(mask)
    
    if depth != M:
        for i in range(before, num_chick):
            res = search(mask + (1 << (i+1)), i+1, depth+1)
            dist = min(res, dist)
    return dist

print(search(0, -1, 0))