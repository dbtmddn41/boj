import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N, S = map(int,f.readline().rstrip().split())
seq = list(map(int, f.readline().rstrip().split()))

class subseq():
    def __init__(self, seq):
        self.seq = seq
        self.sums = []
        self.cnt = 0
    def get_sums(self, i, sum_i):
        global S
        if i == len(self.seq):
            return
    
        inc_sum = sum_i + self.seq[i]
        if inc_sum == S:
            self.cnt += 1
        self.sums.append(inc_sum)
        self.get_sums(i+1, inc_sum)
        self.get_sums(i+1, sum_i)


seq1 = subseq(seq[:N//2])
seq2 = subseq(seq[N//2:])

seq1.get_sums(0,0)
seq2.get_sums(0,0)
bucket = [0 for _ in range(8_000_001)]

for n in seq2.sums:
    bucket[n + 4_000_000] += 1

cnt = 0
for n in seq1.sums:
    cnt += bucket[S - n + 4_000_000]

print(seq1.cnt + seq2.cnt + cnt)