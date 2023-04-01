import sys
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

tree = [() for _ in range(N)]
degree = [0 for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x)-1, f.readline().rstrip().split())
    tree[i] += (j,)
    degree[j] += 1

roots = [i for i in range(N) if degree[i] == 0]

q = deque()
visited = set()
ans = ''
def dfs(node):
    global visited, ans
    if node in visited:
        return
    visited.add(node)
    for child in tree[node]:
        dfs(child)
    ans = str(node + 1) + ' ' + ans

for i in range(len(roots)-1, -1, -1):
    dfs(roots[i])
print(ans.rstrip())