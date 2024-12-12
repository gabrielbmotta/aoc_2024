def load_data(path):
    file = open(path, mode='r')
    return [int(n) for n in file.readlines()[0].split()]


def blink(input):
    output = list()

    for stone in input:
        if stone == 0:
            output.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            output.append(int(str(stone)[0:mid]))
            output.append(int(str(stone)[mid:]))
        else:
            output.append(stone * 2024)

    return output


def blink_repeatedly(data, num_blinks):
    for i in range(num_blinks):
        data = blink(data)
        print(i)
    return data


if __name__ == "__main__":
    # for file in ["test.txt", "input.txt"]:
    for file in ["test.txt"]:
        print(f"== Parsing {file} ==")
        try:
            data = load_data(file)
        except FileNotFoundError:
            print("[!] File not found, skipping.")
            continue

        print(f"Part 1: {len(blink_repeatedly(data, 25))}")
        # print(f"Part 2: {len(blink_repeatedly(data, 75))}")
