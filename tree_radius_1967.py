import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
num_node = int(f.readline().rstrip())
tree = [tuple()]*num_node
distance = [0]*num_node
distance.append(0)
radius = 0

for _ in range(num_node-1):
    line = f.readline().rstrip().split(' ')
    parent, node, dist = map(int, line)
    tree[parent - 1] += (node - 1,)
    distance[node - 1] = dist

def max_two(l):
    max1 = -1
    max2 = -1
    for element in l:
        if element >= max1:
            max2 = max1
            max1 = element
        elif element > max2:
            max2 = element
    return max1, max2

def search(node):
    if len(tree[node]) == 0:
        return distance[node]
    global radius
    
    child_len = []
    for child in tree[node]:
        child_len.append(search(child))
    if len(child_len) >= 2:
        rad = sum(max_two(child_len))
        radius = max(rad, radius)

    return max(child_len) + distance[node]

tree_len = search(0)

if len(tree[0]) == 1:
    radius = max(tree_len, radius)
    
print(radius)