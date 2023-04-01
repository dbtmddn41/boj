import sys
from collections import deque
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())

board = []
for i in range(N):
    line = list(f.readline().rstrip())
    board.append(line)
    for j in range(1, M-1):
        if line[j] == 'B':
            blue = (i,j)
            board[i][j]  = '.'
        elif line[j] == 'R':
            red = (i,j)
            board[i][j]  = '.'
        elif line[j] == 'O':
            hole = (i,j)

def right(r,b):
    if r[1] < b[1]:
        balls = [b, r]
        rb = 'BR'
    else:
        balls = [r, b]
        rb = 'RB'
    
    for k in range(2):
        board[balls[k][0]][balls[k][1]] = '.'
        for i in range(balls[k][1]+1, M):
            if (balls[k][0], i) == hole:
                balls[k] = hole
                break
            elif board[balls[k][0]][i] != '.':
                balls[k] = (balls[k][0], i-1)
                board[balls[k][0]][i-1] = rb[k]
                break
        
    if rb == 'RB':
        return balls
    else:
        return balls[1], balls[0]
    
def left(r,b):
    if r[1] > b[1]:
        balls = [b, r]
        rb = 'BR'
    else:
        balls = [r, b]
        rb = 'RB'
    
    for k in range(2):
        board[balls[k][0]][balls[k][1]] = '.'
        for i in range(balls[k][1]-1, -1, -1):
            if (balls[k][0], i) == hole:
                balls[k] = hole
                break
            elif board[balls[k][0]][i] != '.':
                balls[k] = (balls[k][0], i+1)
                board[balls[k][0]][i+1] = rb[k]
                break
        
    if rb == 'RB':
        return balls
    else:
        return balls[1], balls[0]
    
def down(r,b):
    if r[0] < b[0]:
        balls = [b, r]
        rb = 'BR'
    else:
        balls = [r, b]
        rb = 'RB'
    
    for k in range(2):
        board[balls[k][0]][balls[k][1]] = '.'
        for i in range(balls[k][0]+1, N):
            if (i, balls[k][1]) == hole:
                balls[k] = hole
                break
            elif board[i][balls[k][1]] != '.':
                balls[k] = (i-1, balls[k][1])
                board[i-1][balls[k][1]] = rb[k]
                break
        
    if rb == 'RB':
        return balls
    else:
        return balls[1], balls[0]
    
def up(r,b):
    if r[0] > b[0]:
        balls = [b, r]
        rb = 'BR'
    else:
        balls = [r, b]
        rb = 'RB'
    
    for k in range(2):
        board[balls[k][0]][balls[k][1]] = '.'
        for i in range(balls[k][0]-1, -1, -1):
            if (i, balls[k][1]) == hole:
                balls[k] = hole
                break
            elif board[i][balls[k][1]] != '.':
                balls[k] = (i+1, balls[k][1])
                board[i+1][balls[k][1]] = rb[k]
                break
        
    if rb == 'RB':
        return balls
    else:
        return balls[1], balls[0]

def set_rb(r, b):
    board[r[0]][r[1]] = 'R'
    board[b[0]][b[1]] = 'B'
def unset_rb(r, b):
    if r != hole:
        board[r[0]][r[1]] = '.'
    if b != hole:
        board[b[0]][b[1]] = '.'

visited = set()

def bfs_search(red, blue):
    q = deque()
    q.append((red, blue, 1))
    while q:
        r, b, depth = q.popleft()
        if (r, b) in visited:
                continue
        for f in (right, left, down, up):
            set_rb(r, b)
            r_moved, b_moved = f(r, b)
            if b_moved != hole:
                if r_moved == hole:
                    return depth
                elif (r_moved, b_moved) != (r, b):
                    q.append((r_moved, b_moved, depth+1))
            unset_rb(r_moved, b_moved)
        visited.add((r, b))
        if depth > 10:
            break
    return -1
            
                    
    
print(bfs_search(red, blue))
                
                