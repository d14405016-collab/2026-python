import unittest
from search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_found(self):
        self.assertEqual(linear_search([1, 3, 5, 7, 9], 5), 2)

    def test_linear_not_found(self):
        self.assertEqual(linear_search([1, 3, 5, 7, 9], 4), -1)

    def test_linear_empty(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_linear_first_element(self):
        self.assertEqual(linear_search([1, 3, 5], 1), 0)

    def test_binary_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_binary_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)

    def test_binary_empty(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_binary_first_element(self):
        self.assertEqual(binary_search([1, 3, 5], 1), 0)

    def test_not_modify_input(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        linear_search(data, 3)
        self.assertEqual(data, original)
        binary_search(data, 3)
        self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
