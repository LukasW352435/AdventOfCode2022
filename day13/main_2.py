import ast
import copy


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
    for p in pairs:
        ret = compare_pair(copy.deepcopy(p[0]), copy.deepcopy(p[1]))
    new_pairs = []
    for p in pairs:
        new_pairs.append(p[0])
        new_pairs.append(p[1])
    new_pairs.append([[2]])
    new_pairs.append([[6]])
    sorted_pairs = []
    while len(new_pairs) > 0:
        for p in new_pairs:
            last_index = -1
            for s in sorted_pairs:
                if compare_pair(copy.deepcopy(s), copy.deepcopy(p)):
                    last_index = sorted_pairs.index(s) + 1
            if last_index != -1:
                sorted_pairs.insert(last_index, p)
            else:
                sorted_pairs.insert(0, p)
            new_pairs.remove(p)
    print((sorted_pairs.index([[2]])+1)*(sorted_pairs.index([[6]])+1))


