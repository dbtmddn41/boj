import sys
import bisect
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))

l = [1_000_000_001 for _ in range(N)]
len_l = 0
for a in A:
    i = bisect.bisect_left(l, a)
    if l[i] == 1_000_000_001:
        len_l += 1
    l[i] = a

print(len_l)
