import sys

is_boj = 0
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

str1 = '-' + f.readline().rstrip()
str2 = '-' + f.readline().rstrip()

DP = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

i = len(str1)-1
j = len(str2)-1
print(DP[i][j])
s=''
while DP[i][j] != 0:
    if DP[i][j] == DP[i-1][j]:
        i -= 1
    elif DP[i][j] == DP[i][j-1]:
        j -= 1
    else:
        s = str1[i] + s
        i -= 1
        j -= 1

if s != '':
    print(s)

    