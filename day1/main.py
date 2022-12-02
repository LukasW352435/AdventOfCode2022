with open("input_1.txt") as f:
    txt = f.read().split('\n')
    sums = []
    s = 0
    for line in txt:
        if line != '':
            s += int(line)
        else:
            sums.append(s)
            s = 0
print(max(sums))