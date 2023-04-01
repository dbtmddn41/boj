import sys
sys.setrecursionlimit(10**6)

is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")

N = int(f.readline().rstrip())

forest = []
for i in range(N):
    line = list(map(int, f.readline().rstrip().split()))
    forest.append(line)
    
visited = {}
max_move = 0

di = (1, 0, -1, 0)
dj = (0, 1, 0, -1)
def dfs_search(i, j):
    if (i, j) in visited:
        return visited[(i, j)]
    
    global max_move
    max_move_ij = 0
    for k in range(4):
        next_i, next_j = i + di[k], j + dj[k]
        if not (0 <= next_i < N and 0 <= next_j < N):
            continue
        if forest[i][j] < forest[next_i][next_j]:
            res = dfs_search(next_i, next_j) + 1
            max_move_ij = max(max_move_ij, res)
    visited[(i, j)] = max_move_ij
    max_move = max(max_move, max_move_ij)
    return max_move_ij

for i in range(N):
    for j in range(N):
        if (i, j) == (1, 3):
            a=1
        dfs_search(i, j)

print(max_move+1)