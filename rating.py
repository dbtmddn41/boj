import sys
from collections import deque

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
l = list(f.readlines())
print(l)
tot = 0
for rate in l:
    tier, num = rate.rstrip().split()
    if tier == "Platinum":
        sc = 15
    elif tier == "Gold":
        sc = 10
    elif tier == "Silver":
        sc = 5
    elif tier == "Bronze":
        sc = 0
    
    if num == "I":
        sc += 5
    elif num == "II":
        sc += 4
    elif num == "III":
        sc += 3
    elif num == "IV":
        sc += 2
    elif num == "V":
        sc += 1
    
    tot += sc
    
print(tot)