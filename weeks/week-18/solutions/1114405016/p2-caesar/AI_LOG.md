## 我問 AI 什麼
請幫我用 unittest 寫 caesar_cipher(text, shift) 的測試，SHIFT=7，包含大小寫獨立循環、邊界繞回、符號保留、空字串。

## AI 給了什麼
給了 5 個測試（基本位移、大寫繞回、小寫繞回、符號保留、空字串），但沒寫 shift=0 的情形與非字母字元獨立的 edge case。

## 我改了什麼
我自己補了 `test_shift_zero`（確認位移 0 不改變原文）與 `test_only_non_letters`（純數字標點應完全不變），確保無位移與純符號邊界都被覆蓋。
