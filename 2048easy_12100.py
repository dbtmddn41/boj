import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")


def right(board):
    for i in range(N):
        merged = [0 for _ in range(N)]
        for j in range(N-2, -1, -1):
            while j < N-1:
                if board[i][j] == 0:
                    break
                elif board[i][j] == board[i][j+1]:
                    if not merged[j+1]:
                        board[i][j] = 0
                        board[i][j+1] *= 2
                        merged[j+1] = 1
                    break
                elif board[i][j+1] != 0:
                    break
                else:
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
                j += 1

def left(board):
    for i in range(N):
        merged = [0 for _ in range(N)]
        for j in range(1, N):
            while j > 0:
                if board[i][j] == 0:
                    break
                elif board[i][j] == board[i][j-1]:
                    if not merged[j-1]:
                        board[i][j] = 0
                        board[i][j-1] *= 2
                        merged[j-1] = 1
                    break
                elif board[i][j-1] != 0:
                    break
                else:
                    board[i][j-1] = board[i][j]
                    board[i][j] = 0
                j -= 1

def down(board):
    for j in range(N):
        merged = [0 for _ in range(N)]
        for i in range(N-2, -1, -1):
            while i < N-1:
                if board[i][j] == 0:
                    break
                elif board[i][j] == board[i+1][j]:
                    if not merged[i+1]:
                        board[i][j] = 0
                        board[i+1][j] *= 2
                        merged[i+1] = 1
                    break
                elif board[i+1][j] != 0:
                    break
                else:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                i += 1

def up(board):
    for j in range(N):
        merged = [0 for _ in range(N)]
        for i in range(1, N):
            while i > 0:
                if board[i][j] == 0:
                    break
                elif board[i][j] == board[i-1][j]:
                    if not merged[i-1]:
                        board[i][j] = 0
                        board[i-1][j] *= 2
                        merged[i-1] = 1
                    break
                elif board[i-1][j] != 0:
                    break
                else:
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                i -= 1

max_num = 0

def dfs(board, depth):
    global max_num
    if depth >= 5:
        max_num = max(max(map(max, board)), max_num)
        return
    
    for f in (up, down, left, right):
        new_board = list(map(lambda x: x.copy(), board))
        f(new_board)
        if board != new_board:
            dfs(new_board, depth+1)
        else:
            max_num = max(max(map(max, board)), max_num)
        del new_board

        
N = int(f.readline().rstrip())
board = []
for _ in range(N):
    line = list(map(int, f.readline().rstrip().split()))
    board.append(line)

dfs(board, 0)
print(max_num)