import sys
import os
import math

is_boj = 0
if is_boj:
	f = sys.stdin
else:
	f = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "rt")
 
n, b = map(int, f.readline().rstrip().split())

sum_x = 0
sum_y = 0

for _ in range(n):
    x, y = map(int, f.readline().rstrip().split())
    sum_x += x
    sum_y += y

def f(sum_x, sum_y):
    if sum_x == 0:
        return 'EZPZ'
    
    global n, b
    nume = sum_y - n * b
    
    if nume % sum_x == 0:
        return str(nume // sum_x)

    gcd_nx = math.gcd(nume, sum_x)
    nume //= gcd_nx
    sum_x //= gcd_nx
    s = ''
    if (nume < 0) ^ (sum_x < 0):
        s += '-'
    s += str(abs(nume)) + '/' + str(abs(sum_x))
    return s

print(f(sum_x, sum_y))