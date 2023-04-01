import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

N = int(f.readline().rstrip())

first_x, first_y = map(int, f.readline().rstrip().split())
prev_x, prev_y = map(int, f.readline().rstrip().split())
prev_x -= first_x
prev_y -= first_y

area = 0.0
for _ in range(N-2):
    x, y = map(int, f.readline().rstrip().split())
    x -= first_x
    y -= first_y
    area += cross((prev_x, prev_y), (x, y))
    prev_x, prev_y = x, y
    
area /= 2.
area = abs(area)

print("%.1f"%(area))