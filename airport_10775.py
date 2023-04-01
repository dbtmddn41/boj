import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
G = int(f.readline().rstrip())
P = int(f.readline().rstrip())

empty = list(range(G))

def search_empty(i):
    global empty
    if i != empty[i] and empty[i] >= 0:
        empty[i] = search_empty(empty[i])
    return empty[i]

cnt = 0
for _ in range(P):
    g_i = int(f.readline().rstrip()) - 1
    empty_gate = search_empty(g_i)
    if empty_gate >= 0:
        empty[empty_gate] = empty_gate - 1
        cnt += 1
    else:
        break

print(cnt)