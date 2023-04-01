import sys
import bisect

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
nums = list(map(str, sorted(map(int, f.readline().rstrip().split()))))
visited = []

def bisect_in(bt, element):
    return bisect.bisect_right(bt, element) - bisect.bisect_left(bt, element)


def dfs(s, start, depth):
    if bisect_in(visited, s):
        return
    else:
        bisect.insort(visited, s)

    if depth == M:
        print(s[:-1])
        return

    for i in range(start, N):
        s_new = s + nums[i] + ' '
        dfs(s_new, i+1, depth+1)


dfs('', 0, 0)