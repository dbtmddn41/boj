import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
ph = sorted(list(map(int, f.readline().rstrip().split())))

find_zero = 0
min_ph = 3_000_000_001
for constant in range(1, N-1):
    left=0
    right=N-1
    while left < constant < right:
        mix = ph[left] + ph[right] + ph[constant]
        if abs(mix) < min_ph:
            min_ph = abs(mix)
            res = (left, constant, right)
        if mix < 0:
            left += 1
        elif mix > 0:
            right -= 1
        else:
            find_zero = 1
            break
    if find_zero:
        break
print(*map(lambda x: ph[x], res))