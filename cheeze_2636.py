import sys
from collections import deque
from queue import Queue
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split(' '))

monun = []
num_cheese = 0
for i in range(N):
	monun.append(list())
	for j in map (int, f.readline().rstrip().split()):
		monun[i].append(j)
		if j == 1:
			num_cheese += 1

dr_list = [-1, 0, 1, 0]
dc_list = [0, 1, 0, -1]


def check_air(q, cnt):
	melt = 0
	while q:
		i, j = q.popleft()
		if monun[i][j] == -cnt:
			continue
		monun[i][j] = -cnt
		for dr, dc in zip(dr_list, dc_list):
			if not (0 <= i+dr < N and 0 <= j+dc < M):
				continue
			val = monun[i+dr][j+dc]
			if val != 1 and val != -cnt:
				q.append((i+dr, j+dc))
			elif val == 1:
				monun[i+dr][j+dc] = -cnt
				melt += 1
	return melt

cnt = 1
while not all(map(lambda x: 1 not in x, monun)):
	
	q = deque()
	q.append((0, 0))
	num_melt = check_air(q, cnt)
	
	if num_cheese != num_melt:
		num_cheese -= num_melt
	del q
	cnt += 1


print(cnt-1)
print(num_cheese)