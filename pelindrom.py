import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
nums = list(map(int, f.readline().rstrip().split()))
M = int(f.readline().rstrip())

def is_pel(i,j):
    global DP
    length = j-i+1
    for k in range(length // 2):
        if DP[i+k][j-k] != -1:
            return DP[i+k][j-k]
        if nums[i+k] != nums[j-k]:
            return 0
    return 1

DP = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i, j = map(int, f.readline().rstrip().split())
    res = is_pel(i-1,j-1)
    DP[i-1][j-1] = res
    print(res)