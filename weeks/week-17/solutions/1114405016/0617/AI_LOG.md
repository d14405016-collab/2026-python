# AI_LOG — 0617 預演

## 我問 AI 什麼

> 請AI主動以開發訪談模式反問自己規格

## AI 給了什麼

> 測試程式（7 cases）、實作 timing.py、search.py、compare.py

## 我改了什麼

> 修正 test_side_effect 的預期值（items 從 1→3）和選擇 binary_search 不檢查排序、責任在呼叫端

---

## AI 反問我什麼 / 我怎麼回答

| AI 問了什麼 | 你怎麼回答 |
|---|---|
| timeit 是裝飾器工廠還是單純裝飾器？ | @timeit(repeat=5) 工廠模式 |
| repeat=0 或負數怎麼處理？ | raise ValueError |
| repeat=1 合法嗎？副作用怎麼算？ | 合法，被裝飾函式會跑 repeat 次，副作用累計 |
| 紅燈怎麼定義？ | records 長度不對、型別不對、回傳值變、沒噴錯都算紅 |
| binary_search 未排序輸入怎麼定義？ | docstring 聲明責任在呼叫端，不檢查 |
