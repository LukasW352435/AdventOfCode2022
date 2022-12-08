with open("input.txt") as f:
    txt = f.read().split('\n')
    trees = []
    for line in txt:
        row = []
        for c in line:
            row.append(int(c))
        trees.append(row)
    visible = 0
    for x in range(0, len(trees[0])):
        for y in range(0, len(trees)):
            if x == 0 or y == 0 or x == len(trees[0]) - 1 or y == len(trees) - 1:
                visible += 1
            else:
                is_not_visible = [False, False, False, False]
                # left
                for x_2 in range(0, x):
                    if trees[y][x_2] >= trees[y][x]:
                        is_not_visible[0] = True
                # right
                for x_2 in range(x + 1, len(trees[0])):
                    if trees[y][x_2] >= trees[y][x]:
                        is_not_visible[1] = True
                # top
                for y_2 in range(0, y):
                    if trees[y_2][x] >= trees[y][x]:
                        is_not_visible[2] = True
                # bottom
                for y_2 in range(y + 1, len(trees)):
                    if trees[y_2][x] >= trees[y][x]:
                        is_not_visible[3] = True
                # print(str(y) + " " + str(x) + ": " + str(trees[y][x]) + " " + str(is_not_visible) + str((not all(is_not_visible))))
                if not all(is_not_visible):
                    visible += 1

    print(visible)
