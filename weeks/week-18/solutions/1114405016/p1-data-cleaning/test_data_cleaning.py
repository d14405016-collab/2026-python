import unittest
from data_cleaning import data_cleaning


class TestDataCleaning(unittest.TestCase):

    def test_basic_case(self):
        nums = [4, -8, 7, 12, 4, 0, -8]
        expected = [-8, 0, 4, 12]
        self.assertEqual(data_cleaning(nums), expected)

    def test_all_removed(self):
        nums = [1, 3, 5, 7]
        expected = []
        self.assertEqual(data_cleaning(nums), expected)

    def test_edge_zeros_and_negatives(self):
        nums = [0, -4, 5, 4, 4]
        expected = [-4, 0, 4]
        self.assertEqual(data_cleaning(nums), expected)

    def test_all_identical_duplicates(self):
        nums = [4, 4, 4, 4]
        expected = [4]
        self.assertEqual(data_cleaning(nums), expected)

    def test_single_element_divisible(self):
        nums = [8]
        expected = [8]
        self.assertEqual(data_cleaning(nums), expected)

    def test_single_element_not_divisible(self):
        nums = [9]
        expected = []
        self.assertEqual(data_cleaning(nums), expected)

    def test_large_numbers(self):
        nums = [1000000000, -1000000000, 4]
        expected = [-1000000000, 4, 1000000000]
        self.assertEqual(data_cleaning(nums), expected)


if __name__ == "__main__":
    unittest.main()
