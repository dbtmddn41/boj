import sys
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())

q = deque()
q.append(N)
trace = [0 for _ in range(N+1)]
while True: #큐에 넣기 전에 1 되면 끝내는 최적화
    n = q.popleft()
    if n == 1:
        break

    if n % 3 == 0 and trace[n//3] == 0: 
        q.append(n // 3)
        trace[n//3] = n
    if (n & 1) == 0 and trace[n//2] == 0:
        q.append(n // 2)
        trace[n//2] = n
    if trace[n-1] == 0:
        q.append(n-1)
        trace[n-1] = n

t = 1
s = str(1)
step = 0
while t != N:
    t = trace[t]
    s = str(t) + ' ' + s
    step += 1
print(step)
print(s)