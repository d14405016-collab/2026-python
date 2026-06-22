import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_found_first(self):
        arr = [116, 200, 300, 400]
        idx, cmp = linear_search(arr, 116)
        self.assertEqual(idx, 0)
        self.assertEqual(cmp, 1)

    def test_linear_found_last(self):
        arr = [10, 20, 30, 116]
        idx, cmp = linear_search(arr, 116)
        self.assertEqual(idx, 3)

    def test_linear_not_found(self):
        arr = [1, 2, 3]
        idx, cmp = linear_search(arr, 116)
        self.assertEqual(idx, -1)

    def test_binary_found_first(self):
        arr = [116, 200, 300, 400]
        idx, cmp = binary_search(arr, 116)
        self.assertEqual(idx, 0)

    def test_binary_found_last(self):
        arr = [10, 20, 30, 116]
        idx, cmp = binary_search(arr, 116)
        self.assertEqual(idx, 3)

    def test_binary_not_found(self):
        arr = [1, 2, 3]
        idx, cmp = binary_search(arr, 116)
        self.assertEqual(idx, -1)

    def test_binary_single_element_found(self):
        arr = [116]
        idx, cmp = binary_search(arr, 116)
        self.assertEqual(idx, 0)

    def test_empty_array(self):
        arr = []
        idx, cmp = linear_search(arr, 116)
        self.assertEqual(idx, -1)
        idx, cmp = binary_search(arr, 116)
        self.assertEqual(idx, -1)


if __name__ == "__main__":
    unittest.main()
