x = 1
cycles = 0
addx_cycles = 0
crt_display = []


def init_crt_display():
    global crt_display
    for i in range(0, 6):
        row = []
        for j in range(0, 40):
            row.append(' ')
        crt_display.append(row)


def display_crt_display():
    global crt_display
    for i in range(0, len(crt_display)):
        row = ""
        for j in range(0, len(crt_display[0])):
            row += crt_display[i][j]
        print(row)


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
    init_crt_display()
    command_index = 0
    sum = 0
    while command_index < len(commands):
        # print(f'{int(cycles / 40)}, {int(cycles % 40) - 1}, x: {x}')
        if cycles % 40 == x or cycles % 40 == x - 1 or cycles % 40 == x + 1:
            crt_display[int(cycles / 40)][int(cycles % 40)] = '#'
        cycles += 1
        command_index += execute_command(commands[command_index])
    display_crt_display()
