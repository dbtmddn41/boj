import sys
sys.setrecursionlimit(10**6)
is_boj = 0
if is_boj:
    T = input()
    P = input()
else:
    with open("./input.txt", "rt") as f:
        T = f.readline().rstrip()
        P = f.readline().rstrip()


K = [0 for _ in range(len(P))]
"""def preprocess(j):
    k = 0
    iters = 0
    tmp = []
    while j < len(P):
        if P[j] == P[k] and j != k:
            k += 1
        elif iters == 0 or tmp[iters - 1] == 0:
            k = 0
        else:
            j__ = j - max(0, (tmp[iters -1] -2))
            del tmp
            preprocess(j__)
            return
        K[j] = max(K[j], k)
        tmp.append(k)
        j += 1
        iters += 1
    return

preprocess(0)"""
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = K[j-1]
    if P[i] == P[j]:
        j += 1
        K[i] = j

def check_same(i, j):
    j += 1
    i += 1
    while j < len(P) and i < len(T):
        if T[i] != P[j]:
            break
        j += 1
        i += 1
    return j

def find():
    global T, P, K
    detect_idx = []
    detected = 0
    i = 0
    j = 0
    while i < len(T):
        if T[i] == P[j]:
            res = check_same(i, j)
            if res == len(P):
                detected += 1
                detect_idx.append(i-j+1)
            i = i - j + res
            j = K[res-1]
        else:
            i += 1
            j = 0
    print(detected)
    if detected != 0:
        print(' '.join(map(str, detect_idx)))
    
find()
    