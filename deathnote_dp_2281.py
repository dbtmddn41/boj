import sys
sys.setrecursionlimit(10**6)

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
	
num_people, M = map(int, f.readline().rstrip().split())

note = []
name_len = []
for i in range(num_people):
	name_len.append(int(f.readline().rstrip()))
 
best_case = [[0]*num_people]*num_people

def combine(front, back):
    loss1, left1 = front
    loss2, left2 = back
    return loss1+loss2, left2

for k in range(num_people):
    for i in range(num_people - 1 - k):
        best_case_ik = -1
        for j in range(k):
            loss, left = combine(best_case[i][i+j], best_case[i+j+1][i+k])
            if loss < 
        best_case[i][i+k]