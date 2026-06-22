def data_cleaning(nums, D=4):
    seen = set()
    result = []
    for x in nums:
        if x % D == 0 and x not in seen:
            seen.add(x)
            result.append(x)
    return sorted(result)


def main():
    import sys
    data = sys.stdin.read().strip().splitlines()
    i = 0
    while i < len(data):
        line = data[i].strip()
        if not line:
            i += 1
            continue
        n = int(line)
        if n == 0:
            break
        i += 1
        if i >= len(data):
            break
        nums = list(map(int, data[i].split()))
        i += 1
        cleaned = data_cleaning(nums)
        if not cleaned:
            print("NONE")
        else:
            print(" ".join(map(str, cleaned)))


if __name__ == "__main__":
    main()
