import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, S = map(int, f.readline().rstrip().split())
seq = list(map(int, f.readline().rstrip().split()))
min_seq = abs(min(seq)) * N
max_seq = abs(max(seq)) * N
breadth = min_seq + max_seq

def dfs(i, sum_i):
    if i == N:
        return 0
    inc_sum = sum_i + seq[i]
    inc = dfs(i+1, inc_sum)
    if inc_sum == S:
        inc += 1

    exc = dfs(i+1, sum_i)
    return inc + exc

print(dfs(0,0))