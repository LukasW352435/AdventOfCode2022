def find_badge_code(input1, input2, input3):
    for c in input1:
        if c in input2 and c in input3:
            return c


def char_to_value(char):
    if 0 < ord(char)-64 < 27:
        return ord(char)-64+26
    else:
        return ord(char)-96


with open("input.txt") as f:
    txt = f.read().split('\n')
    sum = 0
    for i in range(0, len(txt), 3):
        if txt[i] == '':
            break
        single = find_badge_code(txt[i], txt[i+1], txt[i+2])
        sum += char_to_value(single)
    print(sum)
