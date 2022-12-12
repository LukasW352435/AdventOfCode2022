import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)


def walk_to(y, x, steps):
    global grid_steps
    global grid
    current = grid[y][x]
    if grid_steps[y][x] > steps:
        grid_steps[y][x] = steps
    if grid_steps[y][x] < steps:
        return
    if current == '{':
        return
    if y - 1 >= 0:
        new = grid[y - 1][x]
        if ord(new) <= ord(current) + 1 and is_better(y, x, y - 1, x):
            walk_to(y - 1, x, steps + 1)
    if y + 1 < len(grid):
        new = grid[y + 1][x]
        if ord(new) <= ord(current) + 1 and is_better(y, x, y + 1, x):
            walk_to(y + 1, x, steps + 1)
    if x - 1 >= 0:
        new = grid[y][x - 1]
        if ord(new) <= ord(current) + 1 and is_better(y, x, y, x - 1):
            walk_to(y, x - 1, steps + 1)
    if x + 1 < len(grid[0]):
        new = grid[y][x + 1]
        if ord(new) <= ord(current) + 1 and is_better(y, x, y, x + 1):
            walk_to(y, x + 1, steps + 1)


def is_better(y, x, ny, nx):
    if grid_steps[ny][nx] > grid_steps[y][x] + 1:
        return True
    return False


ys = 0
xs = 0

ye = 0
xe = 0

grid_steps = []

with open("input.txt") as f:
    txt = f.read().split('\n')
    for i in range(0, len(txt)):
        txt[i] = list(txt[i])
    grid = txt

    grid_steps = [[99999] * len(txt[0]) for i in range(0, len(txt))]

    for i in range(0, len(txt)):
        for j in range(0, len(txt[0])):
            if txt[i][j] == 'S':
                ys = i
                xs = j
            if txt[i][j] == 'E':
                ye = i
                xe = j

    txt[ys][xs] = 'a'
    txt[ye][xe] = '{'

    smallest_a = 99999

    for i in range(0, len(txt)):
        for j in range(0, len(txt[0])):
            if txt[i][j] == 'a':
                ys = i
                xs = j
                walk_to(ys, xs, 0)
                if grid_steps[ye][xe] < smallest_a:
                    smallest_a = grid_steps[ye][xe]

    print(smallest_a)

