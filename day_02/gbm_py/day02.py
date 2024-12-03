def load_lists(path):
    file = open(path, mode='r')
    lines = file.readlines()

    return [[int(i) for i in line.split()] for line in lines]

def is_valid(r):
        last_value = r[0]
        last_sign = None
         
        for value in r[1:]:
            diff = value - last_value
            sign = diff < 0

            fail_criteria = [
                last_sign is not None and last_sign != sign,
                abs(diff) > 3 or abs(diff) < 1
            ]

            for crit in fail_criteria:
                if crit:
                    return False

            last_sign = sign
            last_value = value
        return True

def count_valid(reports, error_tolerance=False):
    valid_reports = 0
    for r in reports:
        if not r:
            continue
        
        if is_valid(r):
            valid_reports += 1
        elif error_tolerance:
            for i in range(len(r)):
                # brute force go brrrr
                if is_valid(r[0:i] + r[i+1:]):
                    valid_reports += 1
                    break

    return valid_reports

if __name__ == "__main__":
    reports = load_lists('input.txt')
    
    print(f"Part 1: {count_valid(reports)}")
    print(f"Part 2: {count_valid(reports, True)}")

