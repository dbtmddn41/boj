import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
W = []
for _ in range(N):
    line = list(map(int, f.readline().rstrip().split()))
    W.append(line)

DP = [[-1 for _ in range(1 << N)] for _ in range(N)]
start = 0
def dfs(curr, traveled):
    global DP, start, N, W
    if traveled == (1 << N)-1:
        if W[curr][start] != 0:
            return W[curr][start]
        else:
            return 20_000_001
    if DP[curr][traveled] != -1:
        return DP[curr][traveled]
    
    left_cost = 20_000_001
    for n in range(N):
        if (traveled >> n) & 1 == 0 and W[curr][n] != 0:
            res = dfs(n, traveled | (1 << n)) + W[curr][n]
            left_cost = min(left_cost, res)
    DP[curr][traveled] = left_cost
    return left_cost

print(dfs(start, 1))