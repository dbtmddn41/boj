import sys
import bisect

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
class segment_tree():
    def __init__(self, arr, n):
        self.arr = arr
        self.tree = [0 for _ in range(n*4)]
        self.make_tree(0, n-1, 1)
    def make_tree(self, start, end, i):
        if start == end:
            self.tree[i] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.tree[i] = self.make_tree(start, mid, i*2) + self.make_tree(mid+1, end, i*2+1)
        return self.tree[i]
    def search_tree(self, left, right, start, end, i):
        if start == left and end == right:
            return self.tree[i]
        mid = (start + end) // 2
        if right <= mid:
            return self.search_tree(left, right, start, mid, i*2)
        elif left > mid:
            return self.search_tree(left, right, mid+1, end, i*2+1)
        else:
            return self.search_tree(left, mid, start, mid, i*2) + self.search_tree(mid+1, right, mid+1, end, i*2+1)
        
T = int(f.readline().rstrip())
n = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))
m = int(f.readline().rstrip())
B = list(map(int, f.readline().rstrip().split()))

seg_tree_A = segment_tree(A, n)
seg_tree_B = segment_tree(B, m)

sum_A = []

for i in range(n):
    for j in range(i+1):
        res = seg_tree_A.search_tree(j, i, 0, n-1, 1)
        sum_A.append(res)
        
sum_A.sort()
        
cnt = 0
for i in range(m):
    for j in range(i+1):
        res = seg_tree_B.search_tree(j, i, 0, m-1, 1)
        cnt += bisect.bisect_right(sum_A, T-res) - bisect.bisect_left(sum_A, T-res)
        
print(cnt)
