import math
import sys
sys.setrecursionlimit(10**4)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
points = []

for i in range(N):
    points.append(tuple(map(int, f.readline().rstrip().split())))
    
arg = lambda i: points[i]
argmax = min(range(len(points)), key=arg)
points[0], points[argmax] = points[argmax], points[0]

def dot(x1, x2):
    return x1[0]*x2[0] + x1[1]*x2[1]
def cross(x1, x2):
    return x1[0]*x2[1] - x1[1]*x2[0]

def cos(x1, x2):
    return dot(x1, x2) / (math.sqrt(dot(x1, x1)) * math.sqrt(dot(x2, x2)))
def sin(x1, x2):
    return cross(x1, x2) / (math.sqrt(dot(x1, x1)) * math.sqrt(dot(x2, x2)))

def minus(x1, x2):
    return (x1[0] - x2[0], x1[1] - x2[1])

rev_clock = [(cos((0, 1), minus(points[i], points[0])), points[i]) for i in range(1, N)]

rev_clock.sort()
points = [points[0]] + [rev_clock[i][1] for i in range(N-1)]

angle = 0 

def check_hull(vec, start):
    for i in range(start+1, N):
        if cross(vec, minus(points[i], points[start])) < 0:
            return False
    return True

def dfs(vec, point_idx):
    global angle
    if point_idx == N - 1:
        if cross(vec, minus(points[point_idx], points[0])) != 0:
            angle += 1
        return 1

    for i in range(point_idx+1, N):
        vec_i = minus(points[i], points[point_idx])
        curr_x_prev = cross(vec, vec_i)
        if curr_x_prev < 0:
            return 0
        
        if curr_x_prev != 0:
            angle += 1
        res = dfs(vec_i, i)
        if res == 1:
            return 1
    
vec = minus(points[1], points[0])

dfs(vec, 1)
if cross(vec, minus(points[0], points[N -1])) != 0:
    angle += 1
    
print(angle)