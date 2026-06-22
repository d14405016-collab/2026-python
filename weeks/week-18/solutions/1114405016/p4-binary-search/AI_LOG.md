## 我問 AI 什麼
請幫我用 unittest 寫 linear_search 與 binary_search 的測試，K=116，包含找到第一個、最後一個、找不到、空陣列，並回傳 (index, cmp_count)。

## AI 給了什麼
給了 6 個測試，但漏了空陣列的 edge case，且沒包含 binary search 在單一元素陣列中找到目標的案例。

## 我改了什麼
我自己補了 `test_empty_array`（確認空陣列時 linear 與 binary 都回傳 -1）與 `test_binary_single_element_found`（確認單元素陣列 binary 能找到目標），確保邊界條件完整覆蓋。另外繪圖時發現 matplotlib 需設 `Agg` backend 才能在無 GUI 環境運作，手動加入 `matplotlib.use("Agg")`。
