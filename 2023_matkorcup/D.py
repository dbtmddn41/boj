import sys
import os

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")
 
T = int(f.readline().rstrip())

for i in range(T):
    N = int(f.readline().rstrip())
    if N < 2:
        print('1 0')
    else:
        print('0 1')
