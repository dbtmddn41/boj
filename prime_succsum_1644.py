import sys
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())

nums = [0 for i in range(N+1)]
for i in range(2, N//2+1):
    if nums[i]:
        continue
    j = 2
    n = i * j
    while n <= N:
        nums[n] = 1
        j += 1
        n = i * j

primes = []
for i in range(2, N+1):
    if nums[i] == 0:
        primes.append(i)
del nums
cnt = 0
part_sum = 0
left = 0
for right in range(len(primes)):
    part_sum += primes[right]
    while part_sum > N and left < right:
        part_sum -= primes[left]
        left += 1
    if part_sum == N:
        cnt += 1

print(cnt)