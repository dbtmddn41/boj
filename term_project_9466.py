import sys
sys.setrecursionlimit(10**5)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

def search(i, depth):
    global visited, trace
    if visited[i] != -1:
        return depth
    if trace[i] != -1:
        return trace[i]
    
    trace[i] = depth
    if wish[i] == i:
        visited[i] = 0
        return depth
    else:
        res = search(wish[i], depth+1)
        
    if res <= depth:
        visited[i] = 0
    else:
        visited[i] = 1
    return res

def not_team():
    global visited, n
    for i in range(n):
        search(i,0)
    return sum(visited)

T = int(f.readline().rstrip())

for _ in range(T):
    n = int(f.readline().rstrip())
    wish = list(map(lambda x: int(x)-1, f.readline().rstrip().split()))
    visited = [-1 for _ in range(n)]
    trace = [-1 for _ in range(n)]
    print(not_team())

