import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
n, m = map(int, f.readline().rstrip().split())

graph = [[float("inf")]*n for _ in range(n)]

for i in range(m):
	start, end, two_way = map(int, f.readline().rstrip().split())
	graph[start-1][end-1] = 0
	if two_way:
		graph[end-1][start-1] = 0
	else:
		graph[end-1][start-1] = 1
for i in range(n):
	graph[i][i] = 0

for point in range(n):
	for start in range(n):
		for end in range(n):
			graph[start][end] = min(graph[start][end], graph[start][point] + graph[point][end])
			
k = int(f.readline().rstrip().strip())

for _ in range(k):
	start, end = map(int, f.readline().rstrip().split())
	print(graph[start-1][end-1])
			