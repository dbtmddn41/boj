import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
costs = []
for _ in range(N):
    c = list(map(int, f.readline().rstrip().split()))
    costs.append(c)

DP = [[1_000_001, 1_000_001, 1_000_001] for _ in range(N)]
def search(i, rgb):
    if i == N-1:
        DP[i][rgb] = costs[i][rgb]
        return costs[i][rgb]
    if DP[i][rgb] != 1_000_001:
        return DP[i][rgb]
    
    DP[i][rgb] = min(search(i+1, (rgb+1)%3), search(i+1, (rgb+2)%3)) + costs[i][rgb]
    return DP[i][rgb]

for rgb in range(3):
    search(0, rgb)
print(min(DP[0]))