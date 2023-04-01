import sys
import bisect
sys.setrecursionlimit(10**5)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, L = map(int, f.readline().rstrip().split())
city = []
for _ in range(N):
    c = int(f.readline().rstrip())
    city.append(c)
    
city.sort()

DP = [[[float('inf'), float('inf')] for _ in range(N)] for _ in range(N)]

start = bisect.bisect_left(city, L)
right = bisect.bisect_right(city, L)

if start >= N:
    start -= 1
    
DP[start][start][0] = abs(city[start] - L) * N
DP[start][start][1] = abs(city[start] - L) * N
if right == start and start != 0:
    start -= 1
    DP[start][start][0] = abs(L - city[start]) * N
    DP[start][start][1] = abs(L - city[start]) * N

def search(i, j, at):
    global start, DP
    if DP[i][j][at] != float('inf') or i > start+1 or j < start:
        return DP[i][j][at]
    if at == 0:
        cost = (city[i+1] - city[i]) * (N - (j-i))
        res1= search(i+1, j, 0) + cost
        cost = (city[j] - city[i]) * (N - (j-i))
        res2 = search(i+1, j, 1) + cost
    else:
        cost = (city[j] - city[j-1]) * (N - (j-i))
        res1= search(i, j-1, 1) + cost
        cost = (city[j] - city[i]) * (N - (j-i))
        res2 = search(i, j-1, 0) + cost
        
    DP[i][j][at] = min(res1, res2)
    
    return DP[i][j][at]

res1 = search(0, N-1, 0)
res2 = search(0, N-1, 1)
print(min(res1, res2))