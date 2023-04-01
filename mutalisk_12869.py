import sys
from collections import deque

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N = int(f.readline().rstrip())
health = tuple(map(int, f.readline().rstrip().split())) + (0,)*(3-N)

visited = {}
q = deque()

def bfs():
    global health
    global visited
    global q
    
    health = tuple(sorted(health))
    visited[health] = 0
    q.append(health)

    cases = tuple(zip((1,1,3,3,9,9), (3,9,1,9,1,3), (9,3,9,1,3,1)))
    while True:
        health = q.popleft()
        if all(map(lambda x: x==0, health)):
            break
        for i, j, k in cases:
            nxt_heal = tuple(map(lambda xe: max(0, xe), (health[0]-i, health[1]-j, health[2]-k)))
            if all(map(lambda x: x==0, nxt_heal)):
                return visited[health] + 1
            nxt_heal = tuple(sorted(nxt_heal))
            if nxt_heal not in visited:
                visited[nxt_heal] = visited[health] + 1
                q.append(nxt_heal)
            
print(bfs())