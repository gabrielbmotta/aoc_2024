def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    lines = [[int(n) for n in list(line.strip())] for line in lines]
    return lines


def cardinal_adjacent(coord):
    return [
            (coord[0] - 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] + 1),
            ]

class TrailMap:
    def __init__(self, data):
        self.data = data
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.trailheads = list()

    def pos_in_bounds(self, pos):
        if pos[0] < 0 or pos[0] >= self.x_lim:
            return False
        if pos[1] < 0 or pos[1] >= self.y_lim:
            return False
        return True

    def find_trailheads(self):
        for j, row in enumerate(self.data):
            for i, n in enumerate(row):
                if n == 0:
                    self.trailheads.append((i, j))

    def total_trail_scores(self):
        self.find_trailheads()
        total_score = 0
        total_rating = 0

        for th in self.trailheads:
            result = self.trail_score(th)
            total_score += result[0]
            total_rating += result[1]

        return total_score, total_rating

    def trail_score(self, trailhead):
        endpoints = set()
        rating = 0

        def look_for_end(current_pos):
            nonlocal rating
            nonlocal endpoints
            val = self.data[current_pos[1]][current_pos[0]]
            if val == 9:
                endpoints.add(current_pos)
                rating += 1
                return
            for pos in cardinal_adjacent(current_pos):
                if not self.pos_in_bounds(pos):
                    continue
                if self.data[pos[1]][pos[0]] == val + 1:
                    look_for_end(pos)

        look_for_end(trailhead)

        return len(list(endpoints)), rating


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
    # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue
        g = TrailMap(data)

        score, rating = g.total_trail_scores()
        print(f"Part 1: {score}")
        print(f"Part 2: {rating}")
