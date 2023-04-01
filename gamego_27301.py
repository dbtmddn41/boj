import sys
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")

N, K = f.readli
ne().rstrip().split()

def get_freq(N, j):
    cnt = 0
    len_N = len(N)

    for i in range(len_N):
        n = int(N[i])
        
        if len_N != i+1:
            nnn = (len_N - 1- i) * 10 ** (len_N - 2 - i)
        else:
            nnn = 0
        fix = 10 ** (len_N - 1 - i)
        if i >= 1 and j == 0:
            cnt += 9 * nnn
        if i == 0 and j == 0:
            cnt += nnn *(n-1)
        else:
            cnt += nnn * n
            
            if j < n:
                cnt += fix
        if j == n:
            cnt += int(N) % fix + 1
        
    return cnt

start = 10 ** len(N)

res = 0
while res == int(N):
    res = get_freq(str(start, K))
    