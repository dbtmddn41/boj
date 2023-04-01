import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

def dfs(s, depth):
    if depth == M:
        print(s[:-1])
        return
    
    for i in range(1, N+1):
        new_s = s + str(i) + ' '
        dfs(new_s, depth+1)
        
s = ''
used = [0]*N
dfs(s, 0)