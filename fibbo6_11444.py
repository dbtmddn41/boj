modn = 1000000007

known = {0:0, 1:1}
def fibbo(n):
    if n in known:
        return known[n]
    
    if n & 1:
        res1 = fibbo((n+1)//2) % modn
        res2 = fibbo((n-1)//2) % modn
        res = (res1**2 + res2**2) % modn
    else:
        f_nd2 = fibbo(n//2) % modn
        res = f_nd2 * (f_nd2 + 2 * (fibbo(n//2 - 1) % modn))
    res %= modn
    known[n] = res
    return res
        
print(fibbo(int(input())))