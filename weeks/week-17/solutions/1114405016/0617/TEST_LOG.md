# TEST_LOG — 0617 測試紀錄

## 執行時間

2026-06-17

## 測試結果

```
$ python -m unittest test_timing test_search -v

test_no_print_inside_decorator (test_timing.TestTimeit.test_no_print_inside_decorator) ... ok
test_preserves_function_metadata (test_timing.TestTimeit.test_preserves_function_metadata) ... ok
test_records_each_repeat_and_average (test_timing.TestTimeit.test_records_each_repeat_and_average) ... ok
test_rejects_invalid_repeat (test_timing.TestTimeit.test_rejects_invalid_repeat) ... ok
test_repeat_one (test_timing.TestTimeit.test_repeat_one) ... ok
test_returns_original_result (test_timing.TestTimeit.test_returns_original_result) ... ok
test_side_effect_not_affect_timing (test_timing.TestTimeit.test_side_effect_not_affect_timing) ... ok
test_binary_empty (test_search.TestSearch.test_binary_empty) ... ok
test_binary_first_element (test_search.TestSearch.test_binary_first_element) ... ok
test_binary_found (test_search.TestSearch.test_binary_found) ... ok
test_binary_not_found (test_search.TestSearch.test_binary_not_found) ... ok
test_linear_empty (test_search.TestSearch.test_linear_empty) ... ok
test_linear_first_element (test_search.TestSearch.test_linear_first_element) ... ok
test_linear_found (test_search.TestSearch.test_linear_found) ... ok
test_linear_not_found (test_search.TestSearch.test_linear_not_found) ... ok
test_not_modify_input (test_search.TestSearch.test_not_modify_input) ... ok
----------------------------------------------------------------------
Ran 16 tests in 0.053s
OK
```

## 效能比較

```
$ python compare.py

n = 100000
linear_search: avg = 0.002663s
binary_search: avg = 0.000002s
linear / binary = 1379.55x
```
