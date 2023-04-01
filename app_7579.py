import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
m = list(map(int, f.readline().rstrip().split()))
m = [0] + m
c = list(map(int, f.readline().rstrip().split()))
c = [0] + c

sum_c = sum(c)

dp = [[0 for _ in range(sum_c + 1)] for _ in range(N + 1)]
min_cost = float('inf')

h = sum_c+1
for i in range(1, N+1):
    for j in range(c[i]):
        dp[i][j] = dp[i-1][j]
    for j in range(c[i], h):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + m[i])
        if dp[i][j] >= M:
            min_cost = min(min_cost, j)
            h = j
            break
        
print(min_cost)