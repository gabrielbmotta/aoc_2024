import re

def load_data(path):
    file = open(path, mode='r')
    return file.read()

def find_mult_values(data):
    return re.findall('mul\((\d+),(\d+)\)', data)

def mult_results(data):
    result = 0
    for a,b in data:
        result += int(a) * int(b)
    return result

def capture_enabled(data):
    #why parse when we can use an obscure, hard-to-debug regex?
    return re.sub("don't\(\)(?:.|\n)*?(?:(?:do\(\))|\Z)", '', data)

if __name__ == "__main__":
    data = load_data('input.txt')

    print(f"Part 1: {mult_results(find_mult_values(data))}")
    # why read the task when you can spend 30 min debugging instead?
    print(f"Part 2: {mult_results(find_mult_values(capture_enabled(data)))}")

