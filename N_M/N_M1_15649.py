import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

def dfs(s, used, depth):
    if depth == M:
        print(s[:-1])
        return
    
    for i in range(1, N+1):
        if used[i-1]:
            continue
        new_s = s + str(i) + ' '
        used[i-1] = 1
        dfs(new_s, used, depth+1)
        used[i-1] = 0
        
s = ''
used = [0]*N
dfs(s, used, 0)