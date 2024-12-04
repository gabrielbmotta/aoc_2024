from enum import Enum


def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


class Direction(Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


def add_dir(pos, dir):
    y, x = pos
    if 'N' in dir.name:
        y -= 1
    if 'S' in dir.name:
        y += 1
    if 'E' in dir.name:
        x += 1
    if 'W' in dir.name:
        x -= 1

    return y, x


class WordSearch:
    def __init__(self, data):
        self.data = data
        self.keyword = 'XMAS'
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.count = None

    def check_valid_string(self, ind, pos, dir):
        if pos[0] < 0 or pos[0] == self.y_lim:
            return
        if pos[1] < 0 or pos[1] == self.x_lim:
            return

        if self.data[pos[1]][pos[0]] != self.keyword[ind]:
            return
        elif self.data[pos[1]][pos[0]] == self.keyword[-1]:
            self.count += 1
            return
        else:
            ind += 1
            pos = add_dir(pos, dir)
            self.check_valid_string(ind, pos, dir)
            return

    def loop(self):
        self.count = 0
        for j, line in enumerate(self.data):
            for i, _ in enumerate(line):
                for dir in [e for e in Direction]:
                    self.check_valid_string(0, (j, i), dir)


class XSearch:
    def __init__(self, data):
        self.data = data
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.count = None

    def pos_valid(self, pos):
        if pos[0] < 0 or pos[0] == self.y_lim:
            return False
        if pos[1] < 0 or pos[1] == self.x_lim:
            return False

        return True

    def check_valid_cross(self, pos):
        if not self.pos_valid(pos):
            return

        # not generic to any string, hard coded for M,S
        if self.data[pos[1]][pos[0]] == 'A':
            for d in [(Direction.NE, Direction.SW),
                      (Direction.NW, Direction.SE)]:
                letters = []
                p1 = add_dir(pos, d[0])
                p2 = add_dir(pos, d[1])
                if not self.pos_valid(p1) or not self.pos_valid(p2):
                    return
                letters.append(self.data[p1[1]][p1[0]])
                letters.append(self.data[p2[1]][p2[0]])

                letters.sort()
                if letters != ['M', 'S']:
                    return
            self.count += 1

    def loop(self):
        self.count = 0
        for j, line in enumerate(self.data):
            for i, _ in enumerate(line):
                self.check_valid_cross((j, i))


if __name__ == "__main__":
    data = load_data('input.txt')

    ws = WordSearch(data)
    ws.loop()
    print(f"Part 1: {ws.count}")

    xs = XSearch(data)
    xs.loop()
    print(f"Part 2: {xs.count}")
