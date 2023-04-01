import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
select = [0]*N

def dfs(s, start, depth):
    if depth == M:
        print(s[:-1])
        return

    for i in range(start, N):
        s_new = s + str(i+1) + ' '
        dfs(s_new, i+1, depth+1)


dfs('', 0, 0)