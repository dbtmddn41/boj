import sys
import bisect

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())

DP = [[[-1 for _ in range(1 << 10)] for _ in range(N)] for _ in range(10)]

def search(n, depth, used):
    if depth == N:
        if used == (1 << 10) -1:
            return 1
        else:
            return 0
        
    if DP[n][depth][used] != -1:
        return DP[n][depth][used]
    res = 0
    for dn in (-1, 1):
        if 0 <= n+dn <= 9:
            res += search(n+dn, depth+1, used | (1 << (n+dn)))
    DP[n][depth][used] = res
    return res

res = 0
for i in range(1, 10):
    res += search(i, 1, 1 << i)
    res %= 1_000_000_000
print(res)