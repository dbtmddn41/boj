import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
	
num_people, M = map(int, f.readline().rstrip().split())

name_len = []
memo_loss = []
for i in range(num_people):
	name_len.append(int(f.readline().rstrip()))
memo_loss =  [[-1] * M for _ in range(num_people)]

def get_loss(name_idx, left):
	if name_idx == num_people:
		return 0
	
	if memo_loss[name_idx][left-1] != -1:
		return memo_loss[name_idx][left-1]

	memo_loss[name_idx][left-1] = left**2 + get_loss(name_idx+1, M - name_len[name_idx])
	
	if left > name_len[name_idx]:
		memo_loss[name_idx][left-1] = min(memo_loss[name_idx][left-1], get_loss(name_idx+1, left - 1 - name_len[name_idx]))
	return memo_loss[name_idx][left-1]
  ###재귀로 짠 이유: 행렬 곱셈과는 다르게 행렬 좌상단 삼각형 모든 원소가 필요하지 않음. 그래서 재귀로 필요한 것만 채움


print(get_loss(1, M - name_len[0]))