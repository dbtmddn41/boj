import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
ph = list(map(int, f.readline().rstrip().split()))

def main():
    left = 0
    right = N-1
    
    min_ph = float('inf')
    while left < right:
        mix_ph = ph[left] + ph[right]
        if abs(mix_ph) < abs(min_ph):
            min_ph = mix_ph
            min_mix = (left, right)
            
        if mix_ph > 0:
            right -= 1
        elif mix_ph < 0:
            left += 1
        else:
            break
    return min_mix

i, j = main()
print(ph[i], ph[j])