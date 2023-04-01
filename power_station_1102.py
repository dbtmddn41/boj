import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N = int(f.readline().rstrip())

costs = 