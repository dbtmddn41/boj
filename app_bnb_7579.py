import sys
import heapq

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
m = list(map(int, f.readline().rstrip().split()))
c = list(map(int, f.readline().rstrip().split()))

apps = []
for i in range(N):
    if c[i] == 0:
        cost_effct = float('inf')
    else:
        cost_effct = m[i] / c[i]
    apps.append((cost_effct, m[i], c[i]))
apps.sort(reverse=True)

def get_bound(mem, i):
    global apps, M
    bound = 0
    
    while mem < M:
        if i >= N:
            return -1
        
        left = M - mem
        if apps[i][1] <= left:
            bound += apps[i][2]
        else:
            bound += left / apps[i][0]
        mem += apps[i][1]
        i += 1
    return bound

heap = []
heapq.heappush(heap, (0,0,0,0))
min_cost = float('inf')

while heap:
    bound, mem, cost, i = heapq.heappop(heap)
    
    if bound >= min_cost:
        continue

    inc_mem = mem + apps[i][1]
    inc_cost = cost + apps[i][2]
    if inc_mem >= M:
        min_cost = min(min_cost, inc_cost)
    else:
        if i ==0:
            inc_bound = get_bound(0, 0)
        else:
            inc_bound = bound
        if inc_bound < min_cost and i+1 < N:
            heapq.heappush(heap, (inc_bound, inc_mem, inc_cost, i+1))
            
    exc_bound = cost + get_bound(mem, i+1)
    if exc_bound < min_cost and exc_bound != -1 and i+1 < N:
        heapq.heappush(heap, (exc_bound, mem, cost, i+1))
        
print(min_cost)