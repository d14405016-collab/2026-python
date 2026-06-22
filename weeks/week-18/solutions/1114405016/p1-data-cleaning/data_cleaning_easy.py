"""
資料清理（三步驟）
學號：1114405016  D=4

步驟：
1. 只留能被 D 整除的數
2. 重複的只留第一個
3. 由小到大排序
"""

def data_cleaning(nums, D=4):
    seen = set()          # 紀錄看過的數字
    result = []
    for x in nums:
        if x % D == 0:          # 能被 D 整除
            if x not in seen:   # 沒看過就加進去
                seen.add(x)
                result.append(x)
    result.sort()               # 由小到大排
    return result


def main():
    import sys
    lines = sys.stdin.read().strip().splitlines()
    i = 0
    while i < len(lines):
        n = int(lines[i].strip())
        i += 1
        if n == 0:
            break
        nums = list(map(int, lines[i].split()))
        i += 1
        ans = data_cleaning(nums)
        if not ans:
            print("NONE")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
