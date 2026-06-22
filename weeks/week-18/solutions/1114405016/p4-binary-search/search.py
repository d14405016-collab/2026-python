import timeit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os


def linear_search(arr, K):
    cmp = 0
    for i, val in enumerate(arr):
        cmp += 1
        if val == K:
            return i, cmp
    return -1, cmp


def binary_search(arr, K):
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


def draw_radar(sizes, linear_times, binary_times,
               linear_cmps, binary_cmps):
    categories = [f"N={s}" for s in sizes]
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    def _normalize(data):
        mx = max(data) if max(data) > 0 else 1
        return [v / mx for v in data]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6),
                                   subplot_kw=dict(polar=True))

    for ax, data_list, title in [
        (ax1,
         [_normalize(linear_times), _normalize(binary_times)],
         "Time Comparison"),
        (ax2,
         [_normalize(linear_cmps), _normalize(binary_cmps)],
         "Comparison Count"),
    ]:
        for values, label, color in zip(
            data_list,
            ["Linear Search", "Binary Search"],
            ["red", "blue"],
        ):
            values += values[:1]
            ax.plot(angles, values, "o-", label=label, color=color)
            ax.fill(angles, values, alpha=0.1, color=color)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_title(title)
        ax.legend(loc="upper right")

    plt.tight_layout()
    os.makedirs("assets", exist_ok=True)
    plt.savefig("assets/radar.png", dpi=150)
    print("[OK] Radar chart saved to assets/radar.png")


def main():
    sizes = [1000, 5000, 10000, 50000]
    K = 116
    results = []

    for n in sizes:
        arr = list(range(n))
        arr[-1] = K
        arr.sort()

        l_time = timeit.timeit(lambda: linear_search(arr, K), number=100)
        b_time = timeit.timeit(lambda: binary_search(arr, K), number=100)
        l_time /= 100
        b_time /= 100

        _, l_cmp = linear_search(arr, K)
        _, b_cmp = binary_search(arr, K)

        results.append((n, l_time, b_time, l_cmp, b_cmp))
        l_idx, _ = linear_search(arr, K)
        b_idx, _ = binary_search(arr, K)
        l_label = f"FOUND [{l_idx}]" if l_idx != -1 else "NOT FOUND"
        b_label = f"FOUND [{b_idx}]" if b_idx != -1 else "NOT FOUND"
        print(f"N={n:6d} | Linear: {l_label} cmp={l_cmp:2d} "
              f"{l_time:.6f}s | Binary: {b_label} cmp={b_cmp:2d} "
              f"{b_time:.6f}s")

    sizes_arr = [r[0] for r in results]
    l_times = [r[1] for r in results]
    b_times = [r[2] for r in results]
    l_cmps = [r[3] for r in results]
    b_cmps = [r[4] for r in results]

    draw_radar(sizes_arr, l_times, b_times, l_cmps, b_cmps)


if __name__ == "__main__":
    main()
