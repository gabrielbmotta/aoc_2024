def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    lines = [[n for n in line.strip('\n')] for line in lines]
    return lines


def cardinal_adjacent(coord):
    return [
            (coord[0] - 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] + 1),
            ]

class PlotMap:
    def __init__(self, data):
        self.data = data
        self.y_lim = len(data)
        self.x_lim = len(data[0])
        self.plots = list()

    def pos_in_bounds(self, pos):
        if pos[0] < 0 or pos[0] >= self.x_lim:
            return False
        if pos[1] < 0 or pos[1] >= self.y_lim:
            return False
        return True

    def find_plots(self):
        def look_for_plot(plot_set, loc, value):
            if self.data[loc[1]][loc[0]] == value:
                plot_set.add(loc)
                for coord in cardinal_adjacent(loc):
                    if self.pos_in_bounds(coord) and not coord in plot_set:
                        look_for_plot(plot_set, coord, value)

        in_group = set()
        for j, row in enumerate(self.data):
            for i, n in enumerate(row):
                if (i, j) in in_group:
                    continue
                else:
                    current_plot = set()
                    look_for_plot(current_plot, (i, j), n)
                    for s in current_plot:
                        in_group.add(s)
                    self.plots.append(current_plot)

    def total_price(self):
        def plot_price(plot):
            area = 0
            perimeter = 0
            for item in plot:
                area += 1
                for adj in cardinal_adjacent(item):
                    if adj not in plot:
                        perimeter += 1
            return area * perimeter

        total_price = 0
        for plot in self.plots:
            total_price += plot_price(plot)
            # print(total_price)

        return total_price



if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
        # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        plot_map = PlotMap(data)
        plot_map.find_plots()
        print(plot_map.total_price())
