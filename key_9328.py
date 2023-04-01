import sys
sys.setrecursionlimit(10**6)
is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

T = int(f.readline().rstrip())

for _ in range(T):
    tot_docs = 0
    h, w = map(int, f.readline().rstrip().split())
    h += 2
    w += 2
    building = []
    building.append(['.' for _ in range(w)])
    for i in range(h-2):
        line = list('.' + f.readline().rstrip() +'.')
        building.append(line)
        for p in line:
            if p == '$':
                tot_docs += 1
    building.append(['.' for _ in range(w)])

    KEYS = list(f.readline().rstrip())
    keys = 0
    if KEYS[0] != '0':
        for k in KEYS:
            keys |= 1 << (ord(k) - ord('a'))

    visited = set()
    #direction = ((1,0,-1,0),(0,-1,0,1))
    direction = ((1,0),(0,-1),(-1,0),(0,1))
    docs = 0
    doors = {}
    def dfs(i,j):
        global docs, visited, keys, doors
        if (i,j) == (4,8):
            qwe = 21
        if (i,j) in visited:
            return 0

        if building[i][j].isupper():
            if (keys >> ord(building[i][j].lower()) - ord('a')) & 1 == 0:
                if building[i][j] not in doors:
                    doors[building[i][j]] = [(i,j)]
                else:
                    doors[building[i][j]].append((i,j))                        
                return 0
            else:
                building[i][j] = '.'
        visited.add((i,j))

        if building[i][j] == '$':
            docs += 1
            building[i][j] = '.'
            if docs == tot_docs:
                return 1
        if building[i][j].islower():
            keys |= (1 << ord(building[i][j]) - ord('a')) #.으로 바꾸기
            k = building[i][j].upper()
            building[i][j] = '.'
            if k in doors:
                while doors[k]:
                    door_i, door_j = doors[k].pop()
                    dfs(door_i, door_j)

        for di, dj in direction:
            next_i = i + di
            next_j = j + dj
            if (not (0 <= next_i < h and 0 <= next_j < w)) or building[next_i][next_j] == '*':
                continue
            res = dfs(next_i, next_j)
            if res == 1:
                return 1
        return 0

    dfs(0,0)
    print(docs)