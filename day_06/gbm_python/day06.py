from enum import Enum


def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
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


def rotate_dir(dir):
    match (dir):
        case Direction.N:
            return Direction.E
        case Direction.E:
            return Direction.S
        case Direction.S:
            return Direction.W
        case Direction.W:
            return Direction.N
        case _:
            return None


class Grid:
    def __init__(self, data):
        self.data = data
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.turn_track = []
        self.pos_history = set()
        self.pos_dir_history = set()
        self.loop_tally = 0
        self.extra_loc = set()

    def traverse(self):
        dir = Direction.N
        pos = self.find_guard()
        # print(f"initial: {pos}")

        while self.pos_in_bounds(pos):
            # print(pos)
            next = self.next_pos(pos, dir)
            if self.data[pos[0]][pos[1]] != '^':
                if dir in [Direction.E, Direction.W]:
                    if self.data[pos[0]][pos[1]] in ['|', '+']:
                        self.data[pos[0]][pos[1]] = '+'
                    else:
                        self.data[pos[0]][pos[1]] = '-'
                if dir in [Direction.N, Direction.S]:
                    if self.data[pos[0]][pos[1]] in ['-', '+']:
                        self.data[pos[0]][pos[1]] = '+'
                    else:
                        self.data[pos[0]][pos[1]] = '|'
            # print(self.data)

            if not self.pos_in_bounds(next):
                break

            while self.data[next[0]][next[1]] == '#':
                dir = rotate_dir(dir)
                self.data[pos[0]][pos[1]] = '+'
                self.pos_history.add(pos)
                self.pos_dir_history.add((pos, dir))
                next = self.next_pos(pos, dir)
                continue

            self.check_loop(pos, next, dir)

            pos = next

    def check_loop(self, pos, next, dir):
        self.pos_history.add(pos)
        self.pos_dir_history.add((pos, dir))

        extra_bob = next
        if extra_bob in self.extra_loc or extra_bob in self.pos_history:
            return
        new_loop_catch_pos_dir = set()

        dir = rotate_dir(dir)
        next = self.next_pos(pos, dir)
        if self.data[next[0]][next[1]] == '#' or next == extra_bob:
            dir = rotate_dir(dir)
            next = self.next_pos(pos, dir)
        pos = next

        while self.pos_in_bounds(pos):
            next = self.next_pos(pos, dir)
            new_loop_catch_pos_dir.add((pos, dir))

            if not self.pos_in_bounds(next):
                break
            while self.data[next[0]][next[1]] == '#' or next == extra_bob:
                dir = rotate_dir(dir)
                next = self.next_pos(pos, dir)
                continue

            if (pos, dir) in self.pos_dir_history:
                self.loop_tally += 1
                self.extra_loc.add(extra_bob)
                return

            pos = next
            if (pos, dir) in new_loop_catch_pos_dir:
                self.loop_tally += 1
                self.extra_loc.add(extra_bob)
                return

    def count_traversed(self):
        sum = 0
        for j in range(self.y_lim):
            for i in range(self.x_lim):
                if self.data[j][i] not in ['.', '#']:
                    sum += 1
        return sum

    def next_pos(self, pos, dir):
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

    def find_guard(self):
        for j in range(self.y_lim):
            for i in range(self.x_lim):
                if self.data[j][i] == '^':
                    return j, i

    def pos_in_bounds(self, pos):
        if pos[0] < 0 or pos[0] == self.y_lim:
            return False
        if pos[1] < 0 or pos[1] == self.x_lim:
            return False
        return True

    def print(self):
        for row in self.data:
            for i in row:
                print(i, end='')
            print()


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
    # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue
        grid = Grid(data)
        grid.traverse()
        print(f"Part 1: {grid.count_traversed()}")
        print(f"Part 2: {grid.loop_tally}")
