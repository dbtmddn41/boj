import sys
import os

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")
 
N, K = map(int, f.readline().rstrip().split())


n = 0
i = 0
cK = str(K)
while i < N:
    n += 1
    for c in str(n):
        if c == cK:
            i += 1

print(n)