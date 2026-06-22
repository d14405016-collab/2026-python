## 我問 AI 什麼
請幫我用 unittest 寫 data_cleaning(nums) 的測試，D=4，包含去除非倍數、去重、排序，至少包含 edge case（全部被移除、全部相同、負數與零）。

## AI 給了什麼
給了 5 個測試案例（基本、全部移除、重複、單一元素可整除、單一元素不可整除），但沒寫負數與零的混合 edge case，也沒寫大數邊界案例。

## 我改了什麼
我自己補了 `test_edge_zeros_and_negatives`（題目提供的範例 `[0, -4, 5, 4, 4]`）和 `test_large_numbers`（測試 $10^9$ 邊界），確保正負零邊界與大數範圍都被覆蓋。
