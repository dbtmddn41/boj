import sys
sys.setrecursionlimit(10**5)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
M -= 1
lamps = []

for _ in range(N):
    D, W = map(int, f.readline().rstrip().split())
    lamps.append((D, W))
    
sums = []
s = 0
for i in range(N):
    s += lamps[i][1]
    sums.append(s)

def get_sum(i, j):
    global sums
    if i == 0:
        return sums[j]
    else:
        return sums[j] - sums[i-1]
    
DP = [[[1_000_000_000, 1_000_000_000] for _ in range(N)] for _ in range(N)]

DP[M][M][0] = 0
DP[M][M][1] = 0

def search(i, j, at):
    global s, DP
    if DP[i][j][at] != 1_000_000_000 or i > M or j < M:
        return DP[i][j][at]
    if at == 0:
        cost = (lamps[i+1][0] - lamps[i][0]) * (s - get_sum(i+1, j))
        res1= search(i+1, j, 0) + cost
        cost = (lamps[j][0] - lamps[i][0]) * (s - get_sum(i+1, j))
        res2 = search(i+1, j, 1) + cost
    else:
        cost = (lamps[j][0] - lamps[j-1][0]) * (s - get_sum(i, j-1))
        res1= search(i, j-1, 1) + cost
        cost = (lamps[j][0] - lamps[i][0]) * (s - get_sum(i, j-1))
        res2 = search(i, j-1, 0) + cost
        
    DP[i][j][at] = min(res1, res2)
    
    return DP[i][j][at]

res1 = search(0, N-1, 0)
res2 = search(0, N-1, 1)
print(min(res1, res2))