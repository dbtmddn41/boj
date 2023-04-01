import sys
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

x1, y1, x2, y2 = map(int, f.readline().rstrip().split())
x3, y3, x4, y4 = map(int, f.readline().rstrip().split())

def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]
def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]
v31 = (x1 - x3, y1 - y3)
v34 = (x4 - x3, y4 - y3)
v32 = (x2 - x3, y2 - y3)

v41 = (x1 - x4, y1 - y4)
v43 = (x3 - x4, y3 - y4)
v42 = (x2 - x4, y2 - y4)

res1 = cross(v31, v34)
res2 = cross(v34, v32)

res3 = cross(v41, v43)
res4 = cross(v43, v42)

area1 = cross(v31, v32)
area2 = cross(v41, v42)

if res1 * res2 < 0 or abs(res1 + res2) < abs(area1):
    print(0)
elif abs(res3 + res4) < abs(area2):
    print(0)
else:
    print(1)
