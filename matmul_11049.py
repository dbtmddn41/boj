import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
matrixs = []

for _ in range(N):
    r, c = map(int, f.readline().rstrip().split())
    matrixs.append((r,c))

DP = [[0 for _ in range(N)] for _ in range(N)]
for k in range(1, N):
    for i in range(N - k):
        min_comp = float('inf')
        for j in range(i, i + k):
            res = DP[i][j] + DP[j+1][i+k]
            res += matrixs[i][0] * matrixs[j][1] * matrixs[i+k][1]
            min_comp = min(res, min_comp)
        DP[i][i+k] = min_comp
        
print(*DP, sep="\n")
print(DP[0][N-1])