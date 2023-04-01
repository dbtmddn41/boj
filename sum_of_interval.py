import sys
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N, M, K = map(int, f.readline().rstrip().split())
nums = []
for _ in range(N):
    nums.append(int(f.readline().rstrip()))
tree = [0 for _ in range(N*4)]

def init_tree(start, end, i):
    if start == end:
        tree[i] = nums[start]
    else:
        mid = (start + end) // 2
        tree[i] = init_tree(start, mid, i*2) + init_tree(mid+1, end, i*2+1)
    return tree[i]

def replace_tree(start, end, i, n_idx, delta):
    tree[i] += delta
    if start == end:
        return
    mid = (start + end) // 2
    if n_idx <= mid:
        replace_tree(start, mid, i*2, n_idx, delta)
    else:
        replace_tree(mid+1, end, i*2+1, n_idx, delta)

#start, end: tree node의 구간 left, right: 찾을 구간
def search_interval(start, end, left, right, i):
    if start == left and end == right:
        return tree[i]
    mid = (start + end) // 2
    if right <= mid:
        return search_interval(start, mid, left, right, i*2)
    elif left > mid:
        return search_interval(mid+1, end, left, right, i*2+1)
    else:
        return search_interval(start, mid, left, mid, i*2) +\
            search_interval(mid+1, end, mid+1, right, i*2+1)
    
        

init_tree(0, N-1, 1)

for _ in range(M+K):
    mode, a, b = map(int, f.readline().rstrip().split())
    if mode == 1:
        delta = b - nums[a-1]
        nums[a-1] = b
        replace_tree(0,N-1,1,a-1,delta)
    elif mode == 2:
        print(search_interval(0,N-1,a-1,b-1,1))
    