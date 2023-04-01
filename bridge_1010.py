import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

T = int(f.readline().rstrip())

known = {}
def dp(m, n):
    if m == n or n == 0:
        return 1
    if (m, n) in known:
        return known[(m, n)]
    
    res = dp(m-1, n) + dp(m-1, n-1)
    known[(m, n)] = res
    return res

for _ in range(T):
    N, M = map(int, f.readline().rstrip().split())
    print(dp(M, N))
    