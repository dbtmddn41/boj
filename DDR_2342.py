import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

nums = list(map(int, f.readline().rstrip().split()))
nums.pop()

N = len(nums)
DP = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(N)]

def dp(i, foot1, foot2):
    if i == 4 and foot1 == 1 and foot2 == 2:
        a=1
    if i == N:
        return 0
    if DP[i][foot1][foot2] != float('inf'):
        return DP[i][foot1][foot2]
    
    nxt = nums[i]
    
    dist = abs(foot2-nxt)
    f1, f2 = sorted((foot1, nxt))
    if foot2 == 0:
        cost = 2
    elif dist == 2:
        cost = 4
    elif dist == 0:
        cost = 1
    else:
        cost = 3
        
    tmp1 = dp(i+1, f1, f2) + cost
    
    dist = abs(foot1-nxt)
    f1, f2 = sorted((foot2, nxt))
    if foot1 == 0:
        cost = 2
    elif dist == 2:
        cost = 4
    elif dist == 0:
        cost = 1
    else:
        cost = 3
        
    tmp2 = dp(i+1, f1, f2) + cost
    
    DP[i][foot1][foot2] = min(tmp1, tmp2)
    
    return DP[i][foot1][foot2]

