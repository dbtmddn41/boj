cases = tuple(zip((1,1,3,3,9,9), (3,9,1,9,1,3), (9,3,9,1,3,1)))
for _ in range(3):
    for i, j, k in cases:
        print(i,j,k)