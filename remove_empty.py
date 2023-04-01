with open("input.txt", "r") as f:
    lines = f.readlines()
print(lines)
with open("input.txt", "w") as f:
    for l in lines:
        l = l.strip()
        if l:
            f.write(l+"\n")