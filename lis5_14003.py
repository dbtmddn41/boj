import sys
import bisect
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))

l = [1_000_000_001 for _ in range(N)]
len_l = 0
record = []
for a in A:
    idx = bisect.bisect_left(l, a)
    record.append(idx)
    if l[idx] == 1_000_000_001:
        len_l += 1
    l[idx] = a

print(len_l)

i = N-1
lis = deque()
for idx in range(len_l-1, -1, -1):
    while record[i] != idx:
        i -= 1
    lis.appendleft(A[i])
    i -= 1
    
print(' '.join(map(str, lis)))        
