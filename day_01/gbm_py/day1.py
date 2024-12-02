def load_lists(path):
    file = open(path, mode='r')
    lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        val1, val2 = line.split()
        list1.append(int(val1))
        list2.append(int(val2))

    return list1, list2

def list_diffs(l1, l2):
    sum = 0
    for a,b in zip(l1, l2):
        sum += abs(a - b)
    return sum

def list_freq_map(l):
    map = {}
    for i in l:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return map

def similarity_score(a, b):
    m = list_freq_map(b)
    sum = 0
    for i in a:
        if i in m:
            sum += i * m[i]
    return sum

if __name__ == "__main__":
    a, b = load_lists('input.txt')
    
    a.sort()
    b.sort()

    print(f"Part 1: {list_diffs(a, b)}")
    print(f"Part 2: {similarity_score(a, b)}")

