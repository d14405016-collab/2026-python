"""
二分搜尋效率與雷達圖
學號：1114405016  K=116

功能：
1. 線性搜尋：從頭一個個找，回傳 (位置, 比較次數)
2. 二分搜尋：每次切一半找，回傳 (位置, 比較次數)
3. timeit 比較兩者耗時
4. 畫出多維度效能雷達圖存到 assets/radar.png
"""

import timeit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os


def linear_search(arr, K):
    """線性搜尋：從頭找到尾"""
    cmp = 0
    for i, val in enumerate(arr):
        cmp += 1
        if val == K:
            return i, cmp
    return -1, cmp


def binary_search(arr, K):
    """二分搜尋：每次砍掉一半"""
    lo, hi = 0, len(arr) - 1
    cmp = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cmp += 1
        if arr[mid] == K:
            return mid, cmp
        cmp += 1
        if arr[mid] < K:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, cmp


def draw_radar(sizes, l_time, b_time, l_cmp, b_cmp):
    """畫兩張雷達圖：時間 vs 比較次數"""
    labels = [f"N={s}" for s in sizes]
    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    def norm(v):
        m = max(v) if max(v) else 1
        return [x / m for x in v]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6),
                                   subplot_kw=dict(polar=True))

    for ax, d1, d2, title in [
        (ax1, norm(l_time), norm(b_time), "時間比較"),
        (ax2, norm(l_cmp), norm(b_cmp), "比較次數"),
    ]:
        for vals, color, label in [
            (d1 + d1[:1], "red", "線性搜尋"),
            (d2 + d2[:1], "blue", "二分搜尋"),
        ]:
            ax.plot(angles, vals, "o-", color=color, label=label)
            ax.fill(angles, vals, alpha=0.1, color=color)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.set_title(title)
        ax.legend()

    plt.tight_layout()
    os.makedirs("assets", exist_ok=True)
    plt.savefig("assets/radar.png", dpi=150)
    print("雷達圖已儲存至 assets/radar.png")


def main():
    sizes = [1000, 5000, 10000, 50000]
    K = 116
    results = []

    for n in sizes:
        arr = list(range(n))
        arr[-1] = K
        arr.sort()

        # 測時間（跑 100 次取平均）
        lt = timeit.timeit(lambda: linear_search(arr, K), number=100) / 100
        bt = timeit.timeit(lambda: binary_search(arr, K), number=100) / 100

        _, lc = linear_search(arr, K)
        _, bc = binary_search(arr, K)
        results.append((n, lt, bt, lc, bc))

        li, _ = linear_search(arr, K)
        bi, _ = binary_search(arr, K)
        lf = f"FOUND [{li}]" if li != -1 else "NOT FOUND"
        bf = f"FOUND [{bi}]" if bi != -1 else "NOT FOUND"
        print(f"N={n:6d} | 線性: {lf} cmp={lc:2d} {lt:.6f}s | "
              f"二分: {bf} cmp={bc:2d} {bt:.6f}s")

    draw_radar(
        [r[0] for r in results],
        [r[1] for r in results],
        [r[2] for r in results],
        [r[3] for r in results],
        [r[4] for r in results],
    )


if __name__ == "__main__":
    main()
