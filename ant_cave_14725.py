import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
N = int(f.readline().rstrip())
cave = []
root={}
node_id = 0

for _ in range(N):
    line = f.readline().rstrip()
    n = int(line[0])
    line = line[2:].split()
    
    idx = 0
    for i, food, in enumerate(line):
        if i == 0:
            if food in root:
                idx = root[food]
            else:
                if n-1 == i:
                    root[food] = -1
                else:
                    cave.append({})
                    root[food] = node_id
                    idx = node_id
                    node_id += 1
        else:
            if food in cave[idx]:
                idx = cave[idx][food]
            else:
                if n-1 == i:
                    cave[idx][food] = -1
                else:
                    cave.append({})
                    cave[idx][food] = node_id
                    idx = node_id
                    node_id += 1
                    
def print_cave(idx, depth):
    for food, child_idx in sorted(cave[idx].items()):
        print('--'*depth+food)
        if child_idx != -1:
            print_cave(child_idx, depth+1)

for rt, i in sorted(root.items()):
    print(rt)
    if i != -1:
        print_cave(i, 1)
            