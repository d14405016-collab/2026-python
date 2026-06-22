import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_basic_shift(self):
        self.assertEqual(caesar_cipher("abc", 7), "hij")

    def test_wrap_around_uppercase(self):
        self.assertEqual(caesar_cipher("XYZ", 7), "EFG")

    def test_wrap_around_lowercase(self):
        self.assertEqual(caesar_cipher("xyz", 7), "efg")

    def test_mixed_case_with_symbols(self):
        self.assertEqual(caesar_cipher("Zz! 123", 7), "Gg! 123")

    def test_empty_string(self):
        self.assertEqual(caesar_cipher("", 7), "")

    def test_only_non_letters(self):
        self.assertEqual(caesar_cipher("123 !@#", 7), "123 !@#")

    def test_full_alphabet_cycle(self):
        plain = "abcdefghijklmnopqrstuvwxyz"
        expected = "hijklmnopqrstuvwxyzabcdefg"
        self.assertEqual(caesar_cipher(plain, 7), expected)

    def test_shift_zero(self):
        self.assertEqual(caesar_cipher("Hello", 0), "Hello")


if __name__ == "__main__":
    unittest.main()
