import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
n = int(f.readline().rstrip())
res = n
p = 2
while p ** 2 <= n:
    if n % p == 0:
        res -= res//p
        while n % p == 0:
            n //= p
    p += 1
    
if n > 1:
    res -= res//n

print(res)