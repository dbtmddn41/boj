import sys

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
#DP[i][rgb]

for rgb in range(3):
    DP[0][rgb] = costs[0][rgb]
for i in range(1, N):
    for rgb in range(3):
        DP[i][rgb] = min(DP[i-1][(rgb+1)%3], DP[i-1][(rgb+2)%3]) + costs[i][rgb]
        
print(min(DP[N-1]))