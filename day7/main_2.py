class Tree:
    dir = ""
    dir_size = 0
    up_dir = None
    content = []

    def __init__(self, dir, up_dir):
        self.dir = dir
        self.up_dir = up_dir
        self.content = []
        self.dir_size = 0

    def __str__(self):
        return self.dir + " " + str(self.content)

    def __eq__(self, other):
        return self.dir == other


ls_command = False
current_dir = None


def build_dir_table(line):
    global ls_command
    global current_dir
    sep = line.split(' ')
    if "$" in line and "cd" in line and "/" not in line:
        ls_command = False
        if ".." in sep[2]:
            current_dir = current_dir.up_dir
        else:
            for d in current_dir.content:
                if d == sep[2]:
                    current_dir = d
    elif "$" in line and "ls" in line:
        ls_command = True
    elif ls_command:
        if "dir" in sep[0]:
            current_dir.content.append(Tree(sep[1], current_dir))
        else:
            current_dir.content.append([int(sep[0]), sep[1]])


def calculate_dir_size(dir_table):
    for x in dir_table.content:
        if isinstance(x, Tree):
            calculate_dir_size(x)
            dir_table.dir_size += x.dir_size
        else:
            dir_table.dir_size += x[0]


def sum_of_dir(dir_table):
    sum = 0
    for x in dir_table.content:
        if isinstance(x, Tree):
            if x.dir_size <= 100000:
                sum += x.dir_size
            sum += sum_of_dir(x)
    return sum


def find_best_dir_to_delete(dir_table, size_to_free, current_best):
    for x in dir_table.content:
        if isinstance(x, Tree):
            if x.dir_size >= size_to_free:
                if x.dir_size < current_best:
                    current_best = x.dir_size
                current_best = find_best_dir_to_delete(x, size_to_free, current_best)
    return current_best


total_disc_space = 70000000
update_size = 30000000

with open("input.txt") as f:
    txt = f.read().split("\n")
    dir_table = Tree("/", None)
    current_dir = dir_table
    for line in txt:
        build_dir_table(line)
    calculate_dir_size(dir_table)
    current_free_size = total_disc_space - dir_table.dir_size
    size_to_free = update_size - current_free_size
    print(find_best_dir_to_delete(dir_table, size_to_free, dir_table.dir_size))
