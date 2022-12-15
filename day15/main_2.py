import itertools


def calculate_ranges(sensors, y_row):
    ranges = []
    for sensor in sensors:
        #print()
        #create_grid()
        #display_range(sensor, y_row)
        #print_grid(y_row)
        distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        y = sensor[1]

        if y_row > y:
            y_delta = y_row - y
        else:
            y_delta = y - y_row
        x_delta = distance - y_delta
        if x_delta < 0:
            continue
        x_min_sen = sensor[0] - x_delta
        x_max_sen = sensor[0] + x_delta

        ranges.append([x_min_sen, x_max_sen])

        #print(f'found: {ranges[-1]}: {ranges[-1][1] - ranges[-1][0] + 1}')

    return ranges


def display_range(sensor, y_row):
    global grid
    distance = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])

    for dy in range(-1 * distance, distance + 1):
        for dx in range(-1 * (distance - abs(dy)), distance + 1 - abs(dy)):
            y = sensor[1] + dy - y_min
            x = sensor[0] + dx - x_min

            if y < 0 or y > len(grid) - 1:
                continue
            if x < 0 or x > len(grid[0]) - 1:
                continue

            if grid[y][x] != "S" and grid[y][x] != "B":
                grid[y][x] = '█'


def print_grid():
    global grid
    i = y_min
    for r in grid:
        str = ""
        for c in r:
            str += c
        if i == 0:
            str += "0"
        i += 1
        print(str)


def compact_ranges(a, b):
    if a[0] <= b[0] <= a[1] <= b[1]:
        return [a[0], b[1]]
    if b[0] <= a[0] <= b[1] <= a[1]:
        return [b[0], a[1]]
    if b[1] >= a[1] >= b[0] >= a[0]:
        return [a[0], b[1]]
    if a[1] >= b[1] >= a[0] >= b[0]:
        return [b[0], a[1]]
    if a[0] == a[1] and b[0] < a[0] < b[1]:
        return [b[0], b[1]]
    if b[0] == b[1] and a[0] < b[0] < a[1]:
        return [a[0], a[1]]
    if a[0] <= b[0] and a[1] >= b[1]:
        return [a[0], a[1]]
    if b[0] <= a[0] and b[1] >= a[1]:
        return [b[0], b[1]]
    # if ranges next to each other
    if a[1] + 1 == b[0]:
        return [a[0], b[1]]
    if b[1] + 1 == a[0]:
        return [b[0], a[1]]
    return []


def create_grid():
    global grid
    grid = [['.'] * (x_max - x_min + 1) for i in range(0, (y_max - y_min + 1))]
    for s in sensors:
        grid[s[1] - y_min][s[0] - x_min] = "S"
        grid[s[3] - y_min][s[2] - x_min] = "B"


def multi_range_compact(ranges):
    end = True
    while end:
        end = False
        for a, b in itertools.combinations(ranges, 2):
            c = compact_ranges(a, b)
            if len(c) > 0:
                ranges.remove(a)
                ranges.remove(b)
                ranges.append(c)
                end = True
                break
    return ranges


file = "input.txt"
# "example.txt"
y_row_max = 20
# "input.txt"
if file == "input.txt":
    y_row_max = 4000000

grid = []
with open(file) as f:
    txt = f.read().split('\n')
    sensors = []
    for line in txt:
        line = line.replace(",", "").replace(":", "")
        s = line.split(' ')
        sensors.append([int(s[2].replace("x=", "")), int(s[3].replace("y=", "")),
                        int(s[8].replace("x=", "")), int(s[9].replace("y=", ""))])

    #[print(x) for x in sensors]
    x_max = max([s[0] for s in sensors] + [s[2] for s in sensors])
    x_min = min([s[0] for s in sensors] + [s[2] for s in sensors])
    y_max = max([s[1] for s in sensors] + [s[3] for s in sensors])
    y_min = min([s[1] for s in sensors] + [s[3] for s in sensors])

    y_found = 0
    x_found = 0

    for y in range(0, y_row_max + 1):
        ranges = calculate_ranges(sensors, y)
        ranges = multi_range_compact(ranges)
        if len(ranges) > 1:
            y_found = y
            x_found = min(ranges[0][1], ranges[1][1]) + 1
            # print(f'Found: x {x_found} y {y_found}')
            print(x_found*4000000+y_found)
            break
