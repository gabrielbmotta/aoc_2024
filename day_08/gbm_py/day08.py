def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
    return lines


class Grid:
    def __init__(self, data):
        self.data = data
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.unique_char = set()
        self.ant_locations = dict()
        self.antinodes = set()
        self.super_antinodes = set()
        for j, line in enumerate(data):
            for i, item in enumerate(line):
                if item == '.':
                    continue
                self.unique_char.add(item)
                if item in self.ant_locations:
                    self.ant_locations[item].append((i, j))
                else:
                    self.ant_locations[item] = [(i, j)]

    def pos_in_bounds(self, pos):
        if pos[0] < 0 or pos[0] >= self.x_lim:
            return False
        if pos[1] < 0 or pos[1] >= self.y_lim:
            return False
        return True

    def find_antinodes(self):
        for _, loc in self.ant_locations.items():
            for node in loc:
                for k in loc:
                    if k == node:
                        continue
                    i = node[0] + node[0] - k[0]
                    j = node[1] + node[1] - k[1]
                    # print(f"{l} - {k} --> {i} {j}")
                    if self.pos_in_bounds((i, j)):
                        self.antinodes.add((i, j))

    def find_super_antinodes(self):
        for _, loc in self.ant_locations.items():
            for node in loc:
                for k in loc:
                    if k == node:
                        continue
                    dx = node[0] - k[0]
                    dy = node[1] - k[1]
                    i = node[0] + dx
                    j = node[1] + dy
                    while self.pos_in_bounds((i, j)):
                        # print(f"{l} - {k} --> {i} {j}")
                        self.super_antinodes.add((i, j))
                        i += dx
                        j += dy

            if len(loc) > 1:
                for node in loc:
                    self.super_antinodes.add(node)


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
    # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue
        g = Grid(data)
        g.find_antinodes()
        print(f"Part 1: {len(g.antinodes)}")
        g.find_super_antinodes()
        print(f"Part 2: {len(g.super_antinodes)}")
