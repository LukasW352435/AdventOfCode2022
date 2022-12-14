def populate_gird(grid, rock_line):
    for i in range(1, len(rock_line)):
        draw_line(grid, rock_line[i-1][0], rock_line[i-1][1], rock_line[i][0], rock_line[i][1])
    pass


def draw_line(grid, x, y, x1, y1):
    grid[y-y_min][x-x_min] = '#'
    grid[y1-y_min][x1-x_min] = '#'
    if x != x1:
        for xi in range(min(x, x1), max(x, x1)):
            grid[y - y_min][xi - x_min] = '#'
    elif y != y1:
        for yi in range(min(y, y1), max(y, y1)):
            grid[yi - y_min][x - x_min] = '#'


def print_grid(grid):
    for r in grid:
        print(r)


def simulate_sand(grid, sand_x, sand_y):
    fall_out = False
    move = 0
    while True:
        if sand_x + 1 > x_max or sand_x - 1 < x_min:
            fall_out = True
            break
        if sand_y + 1 > y_max or sand_y < y_min:
            fall_out = True
            break
        if grid[sand_y-y_min+1][sand_x-x_min] == '.':
            sand_y += 1
            move += 1
        elif grid[sand_y-y_min+1][sand_x-x_min-1] == '.':
            sand_y += 1
            sand_x -= 1
            move += 1
        elif grid[sand_y-y_min+1][sand_x-x_min+1] == '.':
            sand_y += 1
            sand_x += 1
            move += 1
        else:
            break
    if move != 0:
        grid[sand_y-y_min][sand_x-x_min] = 'o'
    return fall_out, move


with open("input.txt") as f:
    txt = f.read().split('\n')
    rock_lines = []
    grid = []

    for line in txt:
        s = line.split(" -> ")
        rock_lines.append([[int(x), int(y)] for x, y in [c.split(',') for c in s]])

    sand = [500, 0]
    x_max, x_min = sand[0], sand[0]
    y_max, y_min = sand[1], sand[1]
    for line in rock_lines:
        for c in line:
            if c[0] < x_min:
                x_min = c[0]
            if c[0] > x_max:
                x_max = c[0]
            if c[1] < y_min:
                y_min = c[1]
            if c[1] > y_max:
                y_max = c[1]

    inf = y_max + 10
    x_min -= inf
    x_max += inf
    y_max += 2
    rock_lines.append([[x_min, y_max], [x_max, y_max]])

    grid = [['.'] * (x_max-x_min+1) for i in range(0, (y_max-y_min+1))]
    grid[sand[1]-y_min][sand[0]-x_min] = '+'
    for line in rock_lines:
        populate_gird(grid, line)

    sand_count = 0
    while True:
        fall_out, move = simulate_sand(grid, sand[0], sand[1])
        if fall_out or move == 0:
            print(sand_count + 1)
            break
        else:
            sand_count += 1

    # print_grid(grid)
