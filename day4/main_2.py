def has_overlapping(line):
    pairs = line.split(',')
    first = pairs[0].split('-')
    second = pairs[1].split('-')
    range_1 = list(range(int(first[0]), int(first[1])+1))
    range_2 = list(range(int(second[0]), int(second[1])+1))
    range_overlapping = [value for value in range_1 if value in range_2]
    if len(range_overlapping) > 0:
        return True
    else:
        return False


with open("input.txt") as f:
    txt = f.read().split('\n')
    sum = 0
    for line in txt:
        if has_overlapping(line):
            sum += 1
    print(sum)
