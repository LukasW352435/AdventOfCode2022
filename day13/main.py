import ast


def compare_pair(left, right):
    if type(left) == list and type(right) == list:
        while len(left) > 0 and len(right) > 0:
            if type(left[0]) == int and type(right[0]) == int:
                if left[0] < right[0]:
                    return True
                if left[0] > right[0]:
                    return False
                if left[0] == right[0]:
                    left.remove(left[0])
                    right.remove(right[0])
            elif type(left[0]) == list and type(right[0]) == list:
                ret = compare_pair(left[0], right[0])
                if ret:
                    return True
                elif type(ret) == bool:
                    return False
                else:
                    left.remove(left[0])
                    right.remove(right[0])
            else:
                if type(left[0]) == int:
                    left[0] = [left[0]]
                elif type(right[0]) == int:
                    right[0] = [right[0]]
        if len(left) < len(right):
            return True
        if len(left) > len(right):
            return False
        return None


with open("input.txt") as f:
    txt = f.read().split('\n')
    pairs = []
    p = []
    for line in txt:
        if line is '':
            pairs.append(p)
            p = []
        else:
            p.append(ast.literal_eval(line))
    index = 1
    sum = 0
    for p in pairs:
        ret = compare_pair(p[0], p[1])
        print(f'{index}: {ret}')
        if ret:
            sum += index
        index += 1
    print(sum)
