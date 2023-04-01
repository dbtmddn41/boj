import sys

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, S = map(int, f.readline().rstrip().split())
nums = list(map(int, f.readline().rstrip().split()))

res = N+1

sum_ji = 0
j=0
for i in range(N):
    sum_ji += nums[i]
    while sum_ji >= S and j <= i:
        res = min(res, i-j+1)
        if sum_ji - S >= nums[j]:
            sum_ji -= nums[j]
            j += 1
        else:
            break

if res ==  N+1:
    res = 0
    
print(res)