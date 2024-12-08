from copy import deepcopy
import itertools


def sm(a, b):
    return a + b


def mult(a, b):
    return a * b


def concat(a, b):
    return int(f"{a}{b}")


class Calibration:
    def __init__(self, init_str):
        brk = init_str.split(":")
        self.result = int(brk[0])
        self.operands = [int(o) for o in brk[1].split()]
        self.valid = None
        self.operators = []

    def __repr__(self):
        return f"{self.result} : {self.operands}"

    def check_valid(self):
        def still_valid(total, ind):
            # print(f"total {total} {ind}")
            if ind == len(self.operands):
                if total == self.result:
                    self.valid = True
            elif total > self.result:
                return
            else:
                for operator in self.operators:
                    new_tot = operator(total, self.operands[ind])
                    still_valid(new_tot, ind+1)

        still_valid(0, 0)


def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    return [Calibration(line) for line in lines]


def sum_of_valid(data, operators):
    rollling_sum = 0
    for cal in data:
        cal.operators = operators
        cal.check_valid()
        if cal.valid:
            rollling_sum += cal.result

    return rollling_sum


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        operators = [sm, mult]
        print(f"Part 1: {sum_of_valid(data, operators)}")
        operators.append(concat)
        print(f"Part 2: {sum_of_valid(data, operators)}")
