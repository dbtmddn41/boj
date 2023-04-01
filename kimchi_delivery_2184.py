import sys
import bisect

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
    

for i in range(start+1, -1, -1):
    for j in range(start, N):
        if i >= j:
            continue
        DP[i][j][0] = min(DP[i+1][j][0] + (city[i+1] - city[i]) * (N - (j-i))\
            , DP[i+1][j][1] + (city[j] - city[i]) * (N - (j-i)))
        DP[i][j][1] = min(DP[i][j-1][1] + (city[j] - city[j-1]) * (N - (j-i))\
            , DP[i][j-1][0] + (city[j] - city[i]) * (N - (j-i)))
        
print(min(DP[0][N-1][0], DP[0][N-1][1]))