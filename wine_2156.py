import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

n = int(f.readline().rstrip())

wine = []
for _ in range(n):
    w = int(f.readline().rstrip())
    wine.append(w)
    
DP = [[-1 for _ in range(n+1)] for _ in range(3)]

def dp(y, i):
    if i > n:
        return 0
    if DP[y][i] != -1:
        return DP[y][i]
    
    w = 0
    if y > 0:
        w = wine[i-1]
    tmp1= 0
    if y < 2:
        tmp1 = dp(y+1, i+1) + w
    tmp2 = dp(0, i+1) + w
    
    DP[y][i] = max(tmp1, tmp2)
    return DP[y][i]



def dp2():
    global wine
    DP = [0 for _ in range(n)]
    DP[0] = wine[0]
    DP[1] = DP[0] + wine[1]
    DP[2] = max((DP[1], DP[0] + wine[2],  wine[1] + wine[2]))
    for i in range(3, n):
        DP[i] = max((DP[i-1], wine[i] + wine[i-1] + DP[i-3], wine[i] + DP[i-2]))
    return DP

print(dp2()[n-1])
print(dp(0,0))