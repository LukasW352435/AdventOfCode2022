x = 1
cycles = 0
addx_cycles = 0
cycles_signal_strengths = [20, 60, 100, 140, 180, 220]


def execute_command(command):
    global x
    global cycles
    global addx_cycles
    if "noop" in command[0]:
        return 1
    elif "addx" in command[0]:
        addx_cycles += 1
        if addx_cycles == 2:
            addx_cycles = 0
            x += command[1]
            return 1
    return 0


with open("input.txt") as f:
    txt = f.read().split('\n')
    commands = []
    for line in txt:
        s = line.split(' ')
        if "noop" in line:
            commands.append([s[0]])
        if "addx" in line:
            commands.append([s[0], int(s[1])])
    command_index = 0
    sum = 0
    while command_index < len(commands):
        cycles += 1
        # print(f'{cycles}: {commands[command_index]} x: {x}')
        if cycles in cycles_signal_strengths:
            print(x * cycles)
            sum += x * cycles
        command_index += execute_command(commands[command_index])
        # print(f'{cycles}: x: {x}')
    print(sum)
