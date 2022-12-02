# Elv, me, points
# A, 1 = Rock
# B, 2 = Paper
# C, 3 = Scissors

# X = need to loss
# Y = need to draw
# Z = need to win

# Win = 6, Draw = 3, Loss = 0

with open("input.txt") as f:
    txt = f.read().split('\n')
    points = 0
    for fight in txt:
        if fight == '':
            break
        elv = fight.split(' ')[0]
        me = fight.split(' ')[1]
        if elv == 'A' and me == 'X':
            points += 3 + 0
        elif elv == 'A' and me == 'Y':
            points += 1 + 3
        elif elv == 'A' and me == 'Z':
            points += 2 + 6
        elif elv == 'B' and me == 'X':
            points += 1 + 0
        elif elv == 'B' and me == 'Y':
            points += 2 + 3
        elif elv == 'B' and me == 'Z':
            points += 3 + 6
        elif elv == 'C' and me == 'X':
            points += 2 + 0
        elif elv == 'C' and me == 'Y':
            points += 3 + 3
        elif elv == 'C' and me == 'Z':
            points += 1 + 6
    print(points)