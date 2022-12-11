def process_items(monkey):
    global monkeys
    for i in monkey[1]:
        monkey[6] += 1
        o = monkey[2].replace("new=", '')
        o = o.replace("old", str(i))
        new = eval(o) // 3
        if new % monkey[3] == 0:
            monkeys[monkey[4][1]][1].append(new)
        else:
            monkeys[monkey[5][1]][1].append(new)
    monkey[1] = []


monkeys = []

with open("input.txt") as f:
    txt = f.read().split('\n')
    m = []
    index = 0
    for line in txt:
        s = line.split(' ')
        if "Monkey" in line:
            m.append(index)
            index += 1
        if "Starting items:" in line:
            m.append([int(x.replace(',', '')) for x in s[4:]])
        if '' is line:
            # item count over time
            m.append(0)
            monkeys.append(m)
            m = []
        if "Operation" in line:
            m.append(line.replace(' ', '').replace("Operation:", ''))
        if "Test" in line:
            m.append(int(s[5]))
        if "If" in line:
            m.append([s[5].replace(':', ''), int(s[9])])

    for r in range(0, 20):
        for m in monkeys:
            process_items(m)
    for m in monkeys:
        print(f'{m[0]}: {m[6]}')

    c = sorted([m[6] for m in monkeys])[-2:]
    print(c[0] * c[1])


