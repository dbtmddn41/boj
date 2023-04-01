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

arg = lambda i: (points[i])
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

def tan(p):
    return p[1] / (p[0] + 1e-7)

def distance2(x1, x2):
    m = minus(x1, x2)
    return m[0] ** 2 + m[1] ** 2
points = [points[0]] + sorted(points[1:], key=lambda x: (round(cos((0, 1), (minus(x, points[0]))), 13), distance2(x, points[0])))

vec = minus(points[1], points[0])

stack = []
for p in points:
    while len(stack) >= 2:
        if cross((minus(stack[-1], stack[-2])), minus(p, stack[-1])) <= 0:
            stack.pop()
        else:
            break
    stack.append(p)
    
        
print(len(stack))