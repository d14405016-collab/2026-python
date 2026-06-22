import unittest
from digital_root import digital_root


class TestDigitalRoot(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(digital_root(0, 9), 0)

    def test_single_digit_less_than_base(self):
        self.assertEqual(digital_root(8, 9), 8)

    def test_multi_step_root(self):
        self.assertEqual(digital_root(80, 9), 8)

    def test_large_number(self):
        self.assertEqual(digital_root(1000000000, 9), 1)

    def test_base_2_simple(self):
        self.assertEqual(digital_root(3, 2), 1)

    def test_base_2_large(self):
        self.assertEqual(digital_root(7, 2), 1)

    def test_base_16(self):
        self.assertEqual(digital_root(255, 16), 15)

    def test_base_16_zero(self):
        self.assertEqual(digital_root(0, 16), 0)


if __name__ == "__main__":
    unittest.main()
