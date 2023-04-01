import sys
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
        elif line[j] == 'R':
            red = (i,j)
        elif line[j] == 'O':
            hole = (i,j)

def R(r,b):
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
    
def L(r,b):
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
    
def D(r,b):
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
    
def U(r,b):
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
trace = []
ans_trace = ''
ans = -1
def dfs_search(r, b, depth):
    global ans, ans_trace, visited, trace
    
    if (r, b, depth) in visited:
        return visited[(r, b, depth)]
    if depth > 10:
        return
    for f in (R, L, U, D):
        r_moved, b_moved = f(r, b)
        trace.append(f.__name__)
        if b_moved != hole:
            if r_moved == hole:
                if depth < ans or ans == -1:
                    ans = depth
                    ans_trace = ''.join(trace)
                restore((r, b), (r_moved, b_moved))
                trace.pop()
                break
            elif (r_moved, b_moved) != (r, b):
                dfs_search(r_moved, b_moved, depth+1)
        restore((r, b), (r_moved, b_moved))
        trace.pop()
    return
dfs_search(red, blue, 1)
print(ans)
if ans != -1:
    print(ans_trace)
                
                