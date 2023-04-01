import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
nums = list(map(str, sorted(map(int, f.readline().rstrip().split()))))
#list가 더 빠름
def dfs(s, used, depth):
    if depth == M:
        print(s[:-1])
        return
    
    for i in range(0, N):
        if used[i]:
            continue
        new_s = s + nums[i] + ' '
        used[i] = 1
        dfs(new_s, used, depth+1)
        used[i] = 0
        
s = ''
used = [0]*N
dfs(s, used, 0)