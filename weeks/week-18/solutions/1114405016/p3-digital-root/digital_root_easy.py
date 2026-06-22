"""
任意進位的數字根（Digital Root）
學號：1114405016  base=9

作法：
1. 把 x 轉成 base 進位，加總各位數字
2. 如果總和 >= base，重複步驟 1
3. 直到總和 < base，即為答案
4. 0 的數字根固定為 0
"""

def digital_root(x, base=9):
    if x == 0:
        return 0
    while x >= base:
        total = 0
        while x > 0:
            total += x % base    # 取最低位
            x //= base           # 去掉最低位
        x = total                # 換成各位和，繼續迴圈
    return x


def main():
    import sys
    for line in sys.stdin:
        x = int(line.strip())
        print(digital_root(x))


if __name__ == "__main__":
    main()
