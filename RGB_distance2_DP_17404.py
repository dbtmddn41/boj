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

ans = 1_000_001
for start in range(3):
    DP[0][start] = costs[0][start]
    DP[0][(start+1)%3] = 1_000_001
    DP[0][(start+2)%3] = 1_000_001
    for i in range(1, N-1):
        for rgb in range(3):
            DP[i][rgb] = min(DP[i-1][(rgb+1)%3], DP[i-1][(rgb+2)%3]) + costs[i][rgb]
    for rgb in range(3):
        if rgb == start:
            continue
        DP[N-1][rgb] = min(DP[N-2][(rgb+1)%3], DP[N-2][(rgb+2)%3]) + costs[N-1][rgb]
        ans = min(ans, DP[N-1][rgb])
print(ans)