with open("input.txt") as f:
    txt = f.read().split('\n')
    trees = []
    for line in txt:
        row = []
        for c in line:
            row.append(int(c))
        trees.append(row)
    visible = 0
    best_scenic_score = 0
    for x in range(0, len(trees[0])):
        for y in range(0, len(trees)):
            score = [0, 0, 0, 0]
            # left
            for x_2 in range(x-1, -1, -1):
                if trees[y][x_2] < trees[y][x]:
                    score[0] += 1
                else:
                    score[0] += 1
                    break

            # right
            for x_2 in range(x + 1, len(trees[0])):
                if trees[y][x_2] < trees[y][x]:
                    score[1] += 1
                else:
                    score[1] += 1
                    break
            # top
            for y_2 in range(y-1, -1, -1):
                if trees[y_2][x] < trees[y][x]:
                    score[2] += 1
                else:
                    score[2] += 1
                    break
            # bottom
            for y_2 in range(y + 1, len(trees)):
                if trees[y_2][x] < trees[y][x]:
                    score[3] += 1
                else:
                    score[3] += 1
                    break
            total = 1
            for s in score:
                total *= s
            if total > best_scenic_score:
                best_scenic_score = total
            # print(str(y) + " " + str(x) + ": " + str(trees[y][x]) + " " + str(score) + " " + str(total))

    print(best_scenic_score)
