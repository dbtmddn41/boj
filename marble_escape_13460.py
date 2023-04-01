import sys
is_boj = 1

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
        elif line[j] == 'R':
            red = (i,j)
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

def restore(origin, moved):
    r_ori, b_ori = origin
    r_moved, b_moved = moved
    
    if b_moved != hole:
        board[b_moved[0]][b_moved[1]] = '.'
    if r_moved != hole:
        board[r_moved[0]][r_moved[1]] = '.'
    board[r_ori[0]][r_ori[1]] = 'R'
    board[b_ori[0]][b_ori[1]] = 'B'


visited = {}

def dfs_search(r, b, depth):
    if (r, b, depth) in visited:
        return visited[(r, b, depth)]
    if depth > 10:
        return -1
    ans = 11
    for f in (right, left, up, down):
        r_moved, b_moved = f(r, b)
        if b_moved != hole:
            if r_moved == hole:
                ans = 1
                restore((r, b), (r_moved, b_moved))
                break
            elif (r_moved, b_moved) != (r, b):
                res = dfs_search(r_moved, b_moved, depth+1)
                if res != -1:
                    ans = min(ans, res+1)
        restore((r, b), (r_moved, b_moved))
        

                
    if ans == 11:
        ans = -1
    visited[(r, b, depth)] = ans
    return ans

print(dfs_search(red, blue, 1))
                
                