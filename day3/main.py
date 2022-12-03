def same_char_from_string_half(input):
    first = input[:int(len(input)/2)]
    second = input[int(len(input)/2):]
    for c in first:
        if c in second:
            return c


def char_to_value(char):
    if 0 < ord(char)-64 < 27:
        return ord(char)-64+26
    else:
        return ord(char)-96


with open("input.txt") as f:
    txt = f.read().split('\n')
    sum = 0
    for line in txt:
        if line == '':
            break
        single = same_char_from_string_half(line)
        sum += char_to_value(single)
    print(sum)
