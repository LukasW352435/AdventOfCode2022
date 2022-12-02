with open("input.txt") as f:
    txt = f.read().split('\n')
    sums = []
    s = 0
    for line in txt:
        if line != '':
            s += int(line)
        else:
            sums.append(s)
            s = 0

top_three = 0
for i in range(0, 3):
    top_three += max(sums)
    sums.remove(max(sums))
print(top_three)