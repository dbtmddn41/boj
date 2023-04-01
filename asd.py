import sys

is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

n = int(f.readline().rstrip())

wine = []
for _ in range(n):
    w = int(f.readline().rstrip())
    wine.append(w)
    

DP = [0 for _ in range(n)]

for i in range(0, n):
    if i == 0:
        DP[0] = wine[0]
    elif i == 1:
        DP[1] = DP[0] + wine[1]
    elif i == 2:
        DP[2] = max((DP[1], DP[0] + wine[2],  wine[1] + wine[2]))
    else:
      DP[i] = max((DP[i-1], wine[i] + wine[i-1] + DP[i-3], wine[i] + DP[i-2]))
print(DP[n-1])