import copy


def load_input(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        rules = []
        changes = []

        for line in lines:
            if '|' in line:
                values = line.split('|')
                rules.append((int(values[0]), int(values[1])))
            elif line:
                values = line.split(',')
                changes.append([int(c) for c in values])

    return rules, changes


def filter_changes(changes, rules):
    valid_changes = []
    invalid_changes = []
    for change in changes:
        valid = True
        for rule in rules:
            if rule[0] in change and rule[1] in change:
                if change.index(rule[1]) < change.index(rule[0]):
                    valid = False
                    break
        if valid:
            valid_changes.append(change)
        else:
            invalid_changes.append(change)

    return valid_changes, invalid_changes


def sum_middle_page(changes):
    sum = 0
    for pages in changes:
        sum += pages[int(len(pages)/2)]
    return sum


def correct_change_order(invalid_changes, rules):
    changes = copy.deepcopy(invalid_changes)
    invalid = True
    while invalid:
        invalid = False
        for change in changes:
            for rule in rules:
                if rule[0] in change and rule[1] in change:
                    i0 = change.index(rule[0])
                    i1 = change.index(rule[1])
                    if i1 < i0:
                        invalid = True
                        change[i0], change[i1] = change[i1], change[i0]
    return changes


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
        print(f"== Parsing {file} ==")
        try:
            rules, changes = load_input(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue
        valid, invalid = filter_changes(changes, rules)
        corrected = correct_change_order(invalid, rules)

        print(f"Part 1: {sum_middle_page(valid)}")
        print(f"Part 1: {sum_middle_page(corrected)}")
