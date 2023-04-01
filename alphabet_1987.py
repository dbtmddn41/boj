import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

R, C = map(int, f.readline().rstrip().split())

board = []
for _ in range(R):
    board.append(f.readline().rstrip())

dc = (1, 0, -1, 0)
dr = (0, -1, 0, 1)

visited_alpha = 0
cnt = 0
visited = [[0 for _ in range(C)] for _ in range(R)]
def backtracking(i,j, depth):
    global visited_alpha, visitied, cnt
    
    char_idx = ord(board[i][j]) - ord('A')
    if visited[i][j] == 1 or ((visited_alpha >> char_idx) & 1):
        return
    cnt = max(depth, cnt)
    visited_alpha |= 1 << char_idx
    visited[i][j] = 1

    for k in range(4):
        next_i = i + dc[k]
        next_j = j + dr[k]
        if (0 <= next_i < R and 0 <= next_j < C):
            backtracking(next_i, next_j, depth+1)

    visited_alpha -= 1 << char_idx
    visited[i][j] = 0
backtracking(0,0,1)
print(cnt)