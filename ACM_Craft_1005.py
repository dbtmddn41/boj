import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

T = int(f.readline().rstrip())


def get_depend(N, K):
    depend = [[] for _ in range(N)]
    for _ in range(K):
        i, j = map(int, f.readline().rstrip().split())
        depend[j-1].append(i-1)
    return depend

def dfs(con):
    global depend, DP, D
    if DP[con] != -1:
        return DP[con]
    depend_max = 0
    for c in depend[con]:
        depend_max = max(depend_max, dfs(c))
    DP[con] = depend_max + D[con]
    return DP[con]

for _ in range(T):
    N, K = map(int, f.readline().rstrip().split())
    D = list(map(int, f.readline().rstrip().split()))
    depend = get_depend(N, K)
    W = int(f.readline().rstrip())

    DP = [-1 for _ in range(N)]
    print(dfs(W-1))