def execute_move(stack, move):
    elems = []
    for i in range(0, move[0]):
        elems.append(stack[move[1]-1].pop())
    elems.reverse()
    stack[move[2]-1].extend(elems)
    return stack


with open("input.txt") as f:
    txt = f.read().split('\n')
    moves = []
    top = []
    stacks = []
    for line in txt:
        if "move" in line:
            s = line.split(' ')
            moves.append([int(s[1]), int(s[3]), int(s[5])])
        elif "[" in line:
            top.append(line)
    while len(top) > 0:
        line = top.pop()
        i = 0
        for c in line:
            i += 1
            if c != '[' and c != ']' and c != ' ':
                if len(stacks) <= (i - 1) / 4:
                    stacks.append([c])
                else:
                    stacks[int((i - 1) / 4)].append(c)

for move in moves:
    stacks = execute_move(stacks, move)

top_letter = ""
for stack in stacks:
    top_letter += stack.pop()
print(top_letter)