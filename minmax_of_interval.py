import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N, M = map(int, f.readline().rstrip().split())
nums = []
for _ in range(N):
    nums.append(int(f.readline().rstrip()))
min_tree = [0 for _ in range(N*4)]
max_tree = [0 for _ in range(N*4)]

def init_min_tree(start, end, i):
    if start == end:
        min_tree[i] = nums[start]
    else:
        mid = (start + end) // 2
        min_tree[i] = min(init_min_tree(start, mid, i*2), init_min_tree(mid+1, end, i*2+1))
    return min_tree[i]

def init_max_tree(start, end, i):
    if start == end:
        max_tree[i] = nums[start]
    else:
        mid = (start + end) // 2
        max_tree[i] = max(init_max_tree(start, mid, i*2), init_max_tree(mid+1, end, i*2+1))
    return max_tree[i]

#start, end: tree node의 구간 left, right: 찾을 구간
def search_min(start, end, left, right, i):
    if start == left and end == right:
        return min_tree[i]
    mid = (start + end) // 2
    if right <= mid:
        return search_min(start, mid, left, right, i*2)
    elif left > mid:
        return search_min(mid+1, end, left, right, i*2+1)
    else:
        return min(search_min(start, mid, left, mid, i*2),\
            search_min(mid+1, end, mid+1, right, i*2+1))
    
def search_max(start, end, left, right, i):
    if start == left and end == right:
        return max_tree[i]
    mid = (start + end) // 2
    if right <= mid:
        return search_max(start, mid, left, right, i*2)
    elif left > mid:
        return search_max(mid+1, end, left, right, i*2+1)
    else:
        return max(search_max(start, mid, left, mid, i*2),\
            search_max(mid+1, end, mid+1, right, i*2+1))

init_min_tree(0, N-1, 1)
init_max_tree(0, N-1, 1)


for _ in range(M):
    left, right = map(int, f.readline().rstrip().split())
    print(search_min(0,N-1,left-1,right-1,1), search_max(0,N-1,left-1,right-1,1))
    