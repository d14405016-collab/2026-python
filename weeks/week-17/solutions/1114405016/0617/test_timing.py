"""0617 任務一 — timeit 裝飾器測試"""

import unittest
import io
import sys
import time

from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit(repeat=3)
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        @timeit(repeat=3)
        def my_func():
            """my doc"""
            return 42

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "my doc")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=5)
        def slow():
            time.sleep(0.01)
            return 0

        slow()
        self.assertEqual(len(slow.records), 5)
        self.assertIsInstance(slow.last_elapsed, float)
        self.assertGreater(slow.last_elapsed, 0)
        expected_avg = sum(slow.records) / len(slow.records)
        self.assertAlmostEqual(slow.last_elapsed, expected_avg, places=6)

    def test_rejects_invalid_repeat(self):
        for invalid in (0, -1, -100):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):
                    @timeit(repeat=invalid)
                    def f():
                        pass

    def test_repeat_one(self):
        @timeit(repeat=1)
        def f():
            return 99

        result = f()
        self.assertEqual(result, 99)
        self.assertEqual(len(f.records), 1)

    def test_no_print_inside_decorator(self):
        @timeit(repeat=2)
        def f():
            return 0

        captured = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        try:
            f()
        finally:
            sys.stdout = old_stdout
        self.assertEqual(captured.getvalue(), "")

    def test_side_effect_not_affect_timing(self):
        items = []

        @timeit(repeat=3)
        def append_item(x):
            items.append(x)
            return x

        result = append_item(1)
        self.assertEqual(result, 1)
        self.assertEqual(len(items), 3)
        self.assertEqual(len(append_item.records), 3)


if __name__ == "__main__":
    unittest.main()
