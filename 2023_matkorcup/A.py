import sys
import os

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")

T, S = map(int, f.readline().rstrip().split())

def jin(T, S):
    is_lunch = (11 <= T <=16)
    if S == 1 or not is_lunch:
        return 280
    if is_lunch:
        return 320
        
print(jin(T, S))