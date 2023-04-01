import sys
sys.setrecursionlimit(10**6)
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
W = int(f.readline().rstrip())
 
cases = []
for _ in range(W):
    r, c = map(int, f.readline().rstrip().split())
    cases.append((r-1, c-1))

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

DP = [[(-1,) for _ in range(W)] for _ in range(W)]
def search(i, j):
    if i == W or j == W:
        return 0
    if DP[i][j][0] != -1:
        return DP[i][j][0]
    curr = max(i, j) + 1
    if i == 0:
        res1 = search(curr, j) + get_dist((0,0), cases[curr-1])
    else:
        res1 = search(curr, j) + get_dist(cases[i-1], cases[curr-1])
    if j == 0:
        res2 = search(i, curr) + get_dist((N-1,N-1), cases[curr-1])
    else:
        res2 = search(i, curr) + get_dist(cases[j-1], cases[curr-1])
    
    if res1 < res2:    
        DP[i][j] = (res1, 1)
    else:
        DP[i][j] = (res2, 2)
    
    return DP[i][j][0]

print(search(0, 0))
i = 0
j = 0
car = DP[0][0][1]
curr = 1
while curr < W:
    print(car)
    if car == 1:
        car = DP[curr][j][1]
        i = curr
    else:
        car = DP[i][curr][1]
        j = curr
    curr += 1
print(car)    
