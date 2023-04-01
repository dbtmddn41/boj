import sys
import bisect
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./buba/buba.in.1", "rt")

N, H = map(int, f.readline().rstrip().split())
ceiling = []
floor = []
for i in range(N // 2):
    floor.append(int(f.readline().rstrip()))
    ceiling.append(int(f.readline().rstrip()))

floor.sort()
ceiling.sort()
def get_obs(idx):
    global floor
    global ceiling
    from_floor = N // 2 - bisect.bisect_left(floor, idx+1)
    from_ceiling = N // 2 - bisect.bisect_left(ceiling, H - idx)
    return (from_floor, from_ceiling)

min_obs = float('inf')
min_num = 1
def bi_search(left_idx, right_idx, left, right):
    if left_idx + 1 >= right_idx:
        return
    
    global min_obs
    global min_num
    
    mid_idx = (left_idx + right_idx) // 2
    mid = get_obs(mid_idx)
    mid_obs = sum(mid)
    
    if mid_obs < min_obs:
        min_obs = mid_obs
        min_num = 1
    elif mid_obs == min_obs:
        min_num += 1
        
    if mid[0] + left[1] <= min_obs:
        bi_search(left_idx, mid_idx, left, mid)
    if right[0] + mid[1] <= min_obs:
        bi_search(mid_idx, right_idx, mid, right)
            
left = get_obs(0)
right = get_obs(H-1)
min_obs = min(sum(left), sum(right))
if sum(left) == sum(right):
    min_num = 2
bi_search(0, H-1, left, right)
print(min_obs, min_num)