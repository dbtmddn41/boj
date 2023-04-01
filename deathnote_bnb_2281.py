import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
	
num_people, M = map(int, f.readline().rstrip().split())

name_len = []
for i in range(num_people):
	name_len.append(int(f.readline().rstrip()))
	
best = num_people * (M**2)

def search_min_bnb(loss, left, idx):
	if idx == num_people:
		global best
		if loss < best:
			best = loss
		return

	if loss >= best:
		return
		
	if left >= name_len[idx] + 1:
		search_min_bnb(loss, left - 1 - name_len[idx], idx+1)
	search_min_bnb(loss + left**2, M - name_len[idx], idx+1)

search_min_bnb(0, M - name_len[0], 1)

print(best)