import sys
#sys.setrecursionlimit(10**6)
is_boj = 0
if is_boj:
    T = input()
    P = input()
else:
    with open("./input.txt", "rt") as f:
        T = f.readline().rstrip()
        P = f.readline().rstrip()

F = [0 for _ in range(len(P))]
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = F[j-1]
    if P[i] == P[j]:
        j += 1
        F[i] = j
        
j = 0
detected = []
i = 0
while i < len(T) and j < len(P):
    if T[i] == P[j]:
        j += 1
    else:
        while j > 0 and T[i] != P[j]:
            j = F[j-1]
    if j == len(P):
        detected.append(i - j + 1)
    i += 1
print(len(detected))
print(' '.join(map(str, detected)))