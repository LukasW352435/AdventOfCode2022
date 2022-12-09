def check_tail(y_head, x_head, y_tail, x_tail):
    global grid_tail
    global grid

    same_col = False
    same_row = False
    if x_head == x_tail:
        same_col = True
    if y_head == y_tail:
        same_row = True

    # straight
    if same_row and x_head - 1 > x_tail:
        x_tail += 1
    if same_row and x_head + 1 < x_tail:
        x_tail -= 1
    if same_col and y_head - 1 > y_tail:
        y_tail += 1
    if same_col and y_head + 1 < y_tail:
        y_tail -= 1

    # corners
    if x_head - 1 > x_tail and y_head - 1 > y_tail:
        x_tail += 1
        y_tail += 1
    if x_head - 1 > x_tail and y_head + 1 < y_tail:
        x_tail += 1
        y_tail -= 1
    if x_head + 1 < x_tail and y_head - 1 > y_tail:
        x_tail -= 1
        y_tail += 1
    if x_head + 1 < x_tail and y_head + 1 < y_tail:
        x_tail -= 1
        y_tail -= 1

    # edges but not straight
    if not same_row and x_head - 1 > x_tail:
        x_tail += 1
        y_tail = y_head
    if not same_row and x_head + 1 < x_tail:
        x_tail -= 1
        y_tail = y_head
    if not same_col and y_head - 1 > y_tail:
        y_tail += 1
        x_tail = x_head
    if not same_col and y_head + 1 < y_tail:
        y_tail -= 1
        x_tail = x_head

    return [y_tail, x_tail]


def simulate_tail():
    global tail_pos
    global grid
    for i in range(1, len(tail_pos)):
        new_pos = check_tail(tail_pos[i - 1][0], tail_pos[i - 1][1], tail_pos[i][0], tail_pos[i][1])
        tail_pos[i][0] = new_pos[0]
        tail_pos[i][1] = new_pos[1]

    last_tail = tail_pos[len(tail_pos) - 1]
    grid_tail[last_tail[0]][last_tail[1]] = '#'


def execute_step(step):
    global tail_pos
    s = step[0]
    n = step[1]
    if s == "R":
        for i in range(0, n):
            tail_pos[0][1] += 1
            simulate_tail()
    if s == "U":
        for i in range(0, n):
            tail_pos[0][0] -= 1
            simulate_tail()

    if s == "D":
        for i in range(0, n):
            tail_pos[0][0] += 1
            simulate_tail()
    if s == "L":
        for i in range(0, n):
            tail_pos[0][1] -= 1
            simulate_tail()


def print_grid(grid):
    print("")
    for i in range(0, len(grid[0])):
        print(grid[i])


def clear_gird(grid) -> list:
    global grid_mid
    grid.clear()
    for i in range(0, grid_mid * 2):
        r = []
        for j in range(0, grid_mid * 2):
            r.append('_')
        grid.append(r)
    return grid


def update_grid():
    global grid
    global x_pos
    global y_pos
    global tail_pos
    clear_gird(grid)
    grid[y_pos][x_pos] = 's'
    for i in range(0, len(tail_pos)):
        grid[tail_pos[i][0]][tail_pos[i][1]] = str(i)


grid = []
grid_tail = []
tail_pos = []
# (1) Head + Tails
tail_count = 1 + 9

grid_mid = 1000
x_pos = int(grid_mid / 2)
y_pos = int(grid_mid / 2)

with open("input.txt") as f:
    txt = f.read().split('\n')
    steps = []
    for line in txt:
        s = line.split(" ")
        steps.append([s[0], int(s[1])])

    for i in range(0, grid_mid * 2):
        r = []
        r_t = []
        for j in range(0, grid_mid * 2):
            r_t.append('_')
            r.append('_')
        grid.append(r)
        grid_tail.append(r_t)

    for i in range(0, tail_count):
        tail_pos.append([y_pos, x_pos])

    grid[y_pos][x_pos] = 's'

    print(f'last step {steps[len(steps) - 1]}')
    for s in steps:
        # print(f'Step: {s}')
        execute_step(s)
        # update_grid()
        # print_grid(grid)

    # print_grid(grid_tail)

    count = 0
    for i in range(0, len(grid_tail)):
        for j in range(0, len(grid_tail[0])):
            if grid_tail[i][j] == '#':
                count += 1
    print(count)
