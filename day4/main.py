def has_overlapping(line):
    pairs = line.split(',')
    first = pairs[0].split('-')
    second = pairs[1].split('-')
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        return True
    elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
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
