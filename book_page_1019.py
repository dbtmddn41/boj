import sys
is_boj = 0

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")

N = f.readline().rstrip()

cnt = [0 for _ in range(10)]
len_N = len(N)

for i in range(len_N):
    n = int(N[i])
    
    if len_N != i+1:
        nnn = (len_N - 1- i) * 10 ** (len_N - 2 - i)
    else:
        nnn = 0
    fix = 10 ** (len_N - 1 - i)
    if i >= 1:
        cnt[0] += 9 * nnn
    for j in range(10):
        if i == 0 and j == 0:
            cnt[0] += nnn *(n-1)
            continue
        cnt[j] += nnn * n
        
        if j < n:
            cnt[j] += fix
    cnt[n] += int(N) % fix + 1
    
print(' '.join(map(str, cnt)))