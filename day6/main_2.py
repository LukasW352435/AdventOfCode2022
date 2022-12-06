with open("input.txt") as f:
    txt = f.read()
    buffer = []
    index = 1
    for c in txt:
        buffer.append(c)
        if len(buffer) > 14:
            buffer.pop(0)
        if len(set(buffer)) > 13:
            print(buffer)
            print(index)
            break
        index += 1
