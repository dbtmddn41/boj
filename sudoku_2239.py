import sys
from collections import deque

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
puzzle = []
visited = [[[0 for _ in  range(9)] for _ in range(9)] for _ in range(3)]
for i in range(9):
    line = list(map(int, f.readline().rstrip()))
    puzzle.append(line)
    for j in range(9):
        n = line[j]
        if n != 0:
            visited[0][i][n-1] = 1
            visited[1][j][n-1] = 1
            visited[2][j//3*3+i//3][n-1] = 1
            
def promising(i, j, n):
    global visited
    if visited[0][i][n-1] == 1 or visited[1][j][n-1] == 1 or visited[2][j//3*3+i//3][n-1] == 1:
        return False
    return True

def backtrack(i, j):
    global puzzle, visited
    if (i,j) == (9,0):
        print(*map(lambda x: "".join(map(str, x)), puzzle), sep='\n')
        return 1
    if j == 8:
        next_ij = (i+1, 0)
    else:
        next_ij = (i, j+1)
    res = 0
    if puzzle[i][j] != 0:
        res = backtrack(*next_ij)
    else:
        for n in range(1,10):
            if not promising(i, j, n):
                continue
            visited[0][i][n-1] = 1
            visited[1][j][n-1] = 1
            visited[2][j//3*3+i//3][n-1] = 1
            puzzle[i][j] = n
            res = backtrack(*next_ij)
            if res == 1:
                break
            visited[0][i][n-1] = 0
            visited[1][j][n-1] = 0
            visited[2][j//3*3+i//3][n-1] = 0
        puzzle[i][j] = 0
    return res   
backtrack(0,0)