from collections import deque
import sys

MAX_N = 100000
N, K = map(int, sys.stdin.readline().rstrip().split(' '))

idx_num = min(MAX_N + 1, max(K*2, N+1))
trc = [-1]*idx_num
q = deque()

def find(N, K):
	trc[N] = -2
	curr_n = N
	if N == K:
		return
	while True:
		nxt_step = curr_n *2, curr_n -1, curr_n + 1
		for nxt in nxt_step:
			if nxt < 0 or nxt >= idx_num or trc[nxt] != -1:
				continue
			trc[nxt] = curr_n
			if nxt == K:
				return
			q.append(nxt)
		curr_n = q.popleft()
  
def get_trc(N, K):
    par = K
    l = []
    cnt = 0
    while True:
        l.append(par)
        if par == N:
            break
        par = trc[par]
        cnt += 1
    return l, cnt

find(N,K)
l, cnt = get_trc(N,K)
print(cnt)
print(' '.join(map(str, l[::-1])))