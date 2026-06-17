# 0617 預演：timeit + 搜尋效能評估

## 效能評估

- n = 100,000 的已排序串列，`linear_search` 平均約 **0.0027s**，`binary_search` 約 **0.000002s** — binary 快約 **1379 倍**。
- `binary_search` 需要先排序（O(n log n)），「排序 + binary」對單次查詢在資料量大時才划算；如果只查一次，排序成本遠高於 linear 一次性掃描。
- 我的直覺是「排序 + binary」在 **大量重複查詢** 同一份資料時才划算，精確交叉點留給明天 6/18 用數據驗證。

## 檔案清單

| 檔案 | 說明 |
|------|------|
| `timing.py` | timeit 裝飾器（TDD 紅綠燈） |
| `test_timing.py` | timeit 測試（7 cases） |
| `search.py` | linear_search + binary_search |
| `test_search.py` | 搜尋測試（9 cases） |
| `compare.py` | 效能比較腳本 |
| `AI_LOG.md` | AI 協作紀錄 |
