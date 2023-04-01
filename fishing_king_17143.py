import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

R, C, M = map(int, f.readline().rstrip().split())
ocean = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, f.readline().rstrip().split())
    ocean[r-1][c-1] = (s, d, z)

def move(i, j, s, d, z):
    if d == 1: #up
        iters = (R-1-i+s) // (R-1)
        if iters % 2:
            i = ((R-1-i+s) % (R-1))
            if i != 0:
                d = 2
        else:
            i = (R-1) - (R-1-i+s) % (R-1)
            if i == R-1 and R-1-i+s != 0:
                d = 2
    elif d == 2:  #down
        iters = (i + s) // (R-1)
        if iters % 2:
            i = (R-1) - ((i + s) % (R-1))
            if i != R-1:
                d = 1
        else:
            i = (i + s) % (R-1)
            if i == 0 and (i+s) != 0:
                d = 1
    elif d == 3:  #right
        iters = (j + s) // (C-1)
        if iters % 2:
            j = (C-1) - ((j + s) % (C-1))
            if j != C-1:
                d = 4
        else:
            j = (j + s) % (C-1)
            if j == 0 and (j+s) != 0:
                d = 4
    elif d == 4: #left
        iters = (C-1-j+s) // (C-1)
        if iters % 2:
            j = (C-1-j+s) % (C-1)
            if j != 0:
                d = 3
        else:
            j = (C-1) - (C-1-j+s) % (C-1)
            if j == 0 and C-1-j+s != 0:
                d = 3
    return (i,j,s,d,z)

def one_second(ocean):
    new_ocean = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if isinstance(ocean[i][j], int):
                continue
            ni,nj,ns,nd,z = move(i,j,*(ocean[i][j]))
            if isinstance(new_ocean[ni][nj], tuple):
                if new_ocean[ni][nj][2] > z:
                    continue
            new_ocean[ni][nj] = (ns,nd,z)
    del ocean
    return new_ocean

tot_z = 0
for j in range(C):
    # print(*ocean,sep="\n")
    # print("---------------")
    for i in range(R):
        if isinstance(ocean[i][j], tuple):
            z = ocean[i][j][2]
            tot_z += z
            ocean[i][j] = 0
            break
    ocean = one_second(ocean)

print(tot_z)
