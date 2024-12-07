from copy import deepcopy
import itertools

class Calibration:
    def __init__(self, init_str):
        brk = init_str.split(":")
        self.result = int(brk[0])
        self.operands = [int(o) for o in brk[1].split()]
        self.valid = None
        # self.valid_operator_orders = []

    def __repr__(self):
        return f"{self.result} : {self.operands}"

    def check_valid(self, operators=['+', '*' ]):
        total_ops = []
        num_op = len(self.operands) - 1
        op_it = itertools.product(operators, repeat=num_op)
        for it in op_it:
            operation = [self.operands[0]]
            for op, num in zip(list(it), self.operands[1:]):
                operation.append(op)
                operation.append(num)
            total_ops.append(operation)

        for op in total_ops:
            running_total = op[0]
            i = 1
            while i < len(op):
                running_total = eval(f"{running_total}{op[i]}{op[i+1]}")
                i += 2
            if running_total == self.result:
                self.valid = True
                return





def load_data(path):
    file = open(path, mode='r')
    lines = file.readlines()
    return [Calibration(line) for line in lines]


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
    # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        rollling_sum = 0
        for cal in data:
            cal.check_valid()
            if cal.valid:
                rollling_sum += cal.result
        print(f"Part 1: {rollling_sum}")
        # print(f"Part 1: {sum_middle_page(corrected)}")
