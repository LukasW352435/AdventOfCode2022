def calculate_ranges(sensors):
    ranges = []
    for sensor in sensors:
        #print()
        #create_grid()
        #display_range(sensor)
        #print_grid()
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


def display_range(sensor):
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
                if y == y_row:
                    y_set.add(x)


def check_for_b_and_s(x, y):
    for s in sensors:
        if x == s[0] and y == s[1]:
            return True
        if x == s[2] and y == s[3]:
            return True
    return False


def print_grid():
    global grid
    i = y_min
    for r in grid:
        str = ""
        for c in r:
            str += c
        if i == y_row:
            str += "Y"
        i += 1
        print(str)


def is_point_on_line(point, line_a, line_b):
    if point[1] == y_row:
        if line_a <= point[0] <= line_b:
            return point[0]
    return "notapoint"


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
    return []


def create_grid():
    global grid
    grid = [['.'] * (x_max - x_min + 1) for i in range(0, (y_max - y_min + 1))]
    for s in sensors:
        grid[s[1] - y_min][s[0] - x_min] = "S"
        grid[s[3] - y_min][s[2] - x_min] = "B"


file = "input.txt"
y_set = set()
# "example.txt"
y_row = 10
# "input.txt"
if file == "input.txt":
    y_row = 2000000

grid = []
with open(file) as f:
    txt = f.read().split('\n')
    sensors = []
    for line in txt:
        line = line.replace(",", "").replace(":", "")
        s = line.split(' ')
        sensors.append([int(s[2].replace("x=", "")), int(s[3].replace("y=", "")),
                        int(s[8].replace("x=", "")), int(s[9].replace("y=", ""))])

    # [print(x) for x in sensors]
    x_max = max([s[0] for s in sensors] + [s[2] for s in sensors])
    x_min = min([s[0] for s in sensors] + [s[2] for s in sensors])
    y_max = max([s[1] for s in sensors] + [s[3] for s in sensors])
    y_min = min([s[1] for s in sensors] + [s[3] for s in sensors])

    ranges = calculate_ranges(sensors)
    # print(len(ranges), ranges)

    end = True
    while end:
        end = False
        for i in range(1, len(ranges)):
            c = compact_ranges(ranges[i - 1], ranges[i])
            if len(c) > 0:
                # print(f'{ranges[i-1]} + {ranges[i]} -> {c}')
                ranges.remove(ranges[i])
                ranges.remove(ranges[i - 1])
                ranges.append(c)
                end = True
                break
    # print(len(ranges), ranges)
    #create_grid()
    for s in sensors:
        #display_range(s)
        pass
    i = 0
    #print_grid()

    points_on_rages = set()
    for r in ranges:
        for s in sensors:
            points_on_rages.add(is_point_on_line([s[0], s[1]], r[0], r[1]))
            points_on_rages.add(is_point_on_line([s[2], s[3]], r[0], r[1]))
    points_on_rages.remove("notapoint")
    sum = 0
    for r in ranges:
        sum += r[1] - r[0] + 1
    print(sum - len(points_on_rages))
