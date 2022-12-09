def check_tail():
    # this function is wrong, but the edge cases are not relevant in part 1.
    # in main_2.py this function is fixed
    global x_pos
    global y_pos
    global x_pos_tail
    global y_pos_tail
    global grid_tail
    global grid

    same_col = False
    same_row = False
    if x_pos == x_pos_tail:
        same_col = True
    if y_pos == y_pos_tail:
        same_row = True

    if not same_row and x_pos - 1 > x_pos_tail:
        y_pos_tail = y_pos
    if not same_row and x_pos + 1 < x_pos_tail:
        y_pos_tail = y_pos
    if not same_col and y_pos - 1 > y_pos_tail:
        x_pos_tail = x_pos
    if not same_col and y_pos + 1 < y_pos_tail:
        x_pos_tail = x_pos

    if x_pos - 1 > x_pos_tail:
        x_pos_tail += 1
    if x_pos + 1 < x_pos_tail:
        x_pos_tail -= 1
    if y_pos - 1 > y_pos_tail:
        y_pos_tail += 1
    if y_pos + 1 < y_pos_tail:
        y_pos_tail -= 1

    grid_tail[y_pos_tail][x_pos_tail] = '#'
    grid[y_pos][x_pos] = 'H'
    grid[y_pos_tail][x_pos_tail] = 'T'


def execute_step(step):
    global grid
    global x_pos
    global y_pos
    s = step[0]
    n = step[1]
    if s == "R":
        for i in range(0, n):
            x_pos += 1
            grid[y_pos][x_pos] = "H"
            check_tail()
    if s == "U":
        for i in range(0, n):
            y_pos -= 1
            grid[y_pos][x_pos] = "H"
            check_tail()
    if s == "D":
        for i in range(0, n):
            y_pos += 1
            grid[y_pos][x_pos] = "H"
            check_tail()
    if s == "L":
        for i in range(0, n):
            x_pos -= 1
            grid[y_pos][x_pos] = "H"
            check_tail()


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


grid = []
grid_tail = []
grid_mid = 1000
x_pos = int(grid_mid / 2)
y_pos = int(grid_mid / 2)
x_pos_tail = int(grid_mid / 2)
y_pos_tail = int(grid_mid / 2)
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
    grid[y_pos][x_pos] = 's'

    for s in steps:
        execute_step(s)

    count = 0
    for i in range(0, len(grid_tail)):
        for j in range(0, len(grid_tail[0])):
            if grid_tail[i][j] == '#':
                count += 1
    print(count)