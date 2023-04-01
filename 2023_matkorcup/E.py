import sys
import os

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")
 
digits = {1: 0b0101000, 2:0b0110111, 3: 0b0101111, 4:0b1101010, 5:0b1001111, 6:0b1011111, 7:1101100, 8:1111111, 9:0b1101111}
N = int(f.readline().rstrip())
num_jari = len(str(N))
max_num = 10**len(str(N)) - 1

N_sep = []
tmp = N
for i in range(num_jari):
    N_sep.append(digits[tmp%10])
    tmp //= 10
    
def mult(l):
    res = 1
    for i in l:
        res *= i
    return res

def xor_dgt(a,b):
    global digits, num_jari
    res = map(lambda x: x[0]^x[1], zip(a, b))
    return list(res)

trace = [0]*max_num
visited = [{0} for _ in range(num_jari)]

def is_visited(nxt_digit):
    global num_jari, visited
    tmp = nxt_digit
    for i in range(num_jari):
        if tmp%10 in visited[i]:
            return True
        tmp //= 10
    return False



sum_ans = N * 3 
mult_ans = N ** 3
ans = [N]*3
trace = []
def dfs(state, prev, bound):
    global sum_ans, mult_ans, ans, visited, trace
    if bound > sum_ans:
        return 1
    
    if state == N_sep and len(trace) > 1:
        mult_curr = mult(state)
        if sum_ans == bound:
            if mult_curr > mult_ans:
                return
        mult_ans = mult_curr
        sum_ans = bound
        ans = trace[:]
        return 1
        
    for nxt_dgt in range(prev+1, max_num):
        if not is_visited(nxt_dgt):
            tmp = nxt_dgt
            nxt_state = []
            for i in range(0, num_jari):
                visited[i] |= {tmp % 10}
                nxt_state.append(digits[tmp % 10])
                tmp //= 10
            trace.append(nxt_dgt)
            
            res = dfs(xor_dgt(state, nxt_state), nxt_dgt, bound+nxt_dgt)
            
            tmp = nxt_dgt
            for i in range(0, num_jari):
                visited[i] -= {tmp % 10}
                tmp //= 10        
            trace.pop()
            if res == 1:
                return 0

dfs([0 for _ in range(num_jari)], 1, 0)
    
print(sum_ans, len(ans))
print('\n'.join(list(map(str, ans))))