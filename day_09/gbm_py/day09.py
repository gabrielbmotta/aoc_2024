def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    return [int(n) for n in lines[0].strip("\n")]


class Filesystem():
    def __init__(self, data):
        self.data = data
        self.layout = None

    def __repr__(self):
        for i in self.layout:
            return ''.join([str(s) for s in self.layout])

    def expand_layout(self):
        self.layout = list()
        file_state = True
        file_count = 0

        for c in self.data:
            if file_state:
                for i in range(c):
                    self.layout.append(file_count)
                file_count += 1
                file_state = False
            else:
                for i in range(c):
                    self.layout.append('.')
                file_state = True

    def arrange_layout_file_blocks(self):
        self.expand_layout()
        b_ptr = len(self.layout) - 1
        while self.layout[b_ptr] == '.':
            b_ptr - 1
        f_ptr = 0

        while f_ptr < b_ptr:
            if self.layout[f_ptr] != '.':
                f_ptr += 1
                continue
            if self.layout[b_ptr] == '.':
                b_ptr -= 1
                continue
            self.layout[f_ptr] = self.layout[b_ptr]
            self.layout[b_ptr] = '.'

    def arrange_layout_whole_files(self):
        self.expand_layout()
        ptr = len(self.layout) - 1
        while self.layout[ptr] == '.':
            ptr -= 1
        ptr_val = self.layout[ptr]

        def file_size():
            nonlocal ptr, ptr_val
            n = 0
            while (ptr - n > 0 and
                   self.layout[ptr - n] == ptr_val):
                n += 1
            return n

        def move_file(dest, src, size):
            val = self.layout[src]
            for n in range(size):
                self.layout[dest + n] = val
                self.layout[src - n] = '.'

        spaces = self.map_spaces()

        while ptr_val > 0:
            s = file_size()
            for i, space in enumerate(spaces):
                if space[0] > ptr:
                    break
                if s <= space[1]:
                    move_file(space[0], ptr, s)
                    if s == space[1]:
                        spaces.pop(i)
                    else:
                        spaces[i] = (space[0] + s, space[1] - s)
                    break
            ptr_val -= 1
            while (ptr >= 0 and
                   self.layout[ptr] != ptr_val):
                ptr -= 1

    def map_spaces(self):
        spaces = list()
        i = 0
        while i < len(self.layout):
            if self.layout[i] == '.':
                size = 0
                while (i + size < len(self.layout) and
                       self.layout[i + size] == '.'):
                    size += 1
                spaces.append((i, size))
                i += size
            else:
                i += 1
        return spaces

    def get_checksum(self):
        checksum = 0
        for i, n in enumerate(self.layout):
            if n != '.':
                checksum += i * n
        return checksum


if __name__ == "__main__":
    for file in ["test2.txt", "test.txt", "input.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        fs = Filesystem(data)
        fs.arrange_layout_file_blocks()
        print(f"Part 1: {fs.get_checksum()}")

        fs.arrange_layout_whole_files()
        print(f"Part 2: {fs.get_checksum()}")
