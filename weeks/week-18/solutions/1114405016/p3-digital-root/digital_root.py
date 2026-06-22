def digital_root(x, base):
    if x == 0:
        return 0
    while x >= base:
        total = 0
        while x > 0:
            total += x % base
            x //= base
        x = total
    return x


def main():
    import sys
    base = 9
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digital_root(x, base))


if __name__ == "__main__":
    main()
