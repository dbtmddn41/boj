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

DP = [[[1_000_001, 1_000_001, 1_000_001] for _ in range(N)] for _ in range(3)]
def search(start, i, rgb):
    if i == N-1:
        if rgb != start:
            return costs[i][rgb]
        else:
            return 1_000_001
    if DP[start][i][rgb] != 1_000_001:
        return DP[start][i][rgb]
    
    DP[start][i][rgb] = min(search(start, i+1, (rgb+1)%3), search(start, i+1, (rgb+2)%3)) + costs[i][rgb]
    return DP[start][i][rgb]

ans = 1_000_001
for i in range(3):
    res = search(i,0,i)
    ans = min(res, ans)

print(ans)