import sys

is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

def dfs(mask, start, depth):
    if depth == M:
        end = ' '
        for i in range(1, N+1):
            if mask & 1:
                if i == start:
                    end = '\n'
                print(i, end=end)
            mask >>= 1
        return
    
    for i in range(start, N):
        mask |= 1 << i
        dfs(mask, i+1, depth+1)
        mask -= 1 << i

dfs(0, 0, 0)