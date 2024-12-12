from collections import Counter


def load_data(path):
    file = open(path, mode='r')
    return [int(n) for n in file.readlines()[0].split()]


def blink(input):
    output = dict()

    def add_to_dict(v, n):
        nonlocal output
        if v in output:
            output[v] += n
        else:
            output[v] = n

    for stone, num in input.items():
        if stone == 0:
            add_to_dict(1, num)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            add_to_dict(int(str(stone)[0:mid]), num)
            add_to_dict(int(str(stone)[mid:]), num)
        else:
            add_to_dict(stone * 2024, num)

    return output


def blink_repeatedly(data, num_blinks):
    for i in range(num_blinks):
        data = blink(data)
    return data


if __name__ == "__main__":
    for file in ["test.txt", "input.txt"]:
    # for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        blink25 = blink_repeatedly(dict(Counter(data)), 25)
        p1_sum = 0
        for _, n in blink25.items():
            p1_sum += n
        print(f"Part 1: {p1_sum}")

        blink75 = blink_repeatedly(dict(Counter(data)), 75)
        p2_sum = 0
        for _, n in blink75.items():
            p2_sum += n
        print(f"Part 2: {p2_sum}")
