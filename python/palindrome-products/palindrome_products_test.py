import unittest

from palindrome_products import (
    largest,
    smallest,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class PalindromeProductsTest(unittest.TestCase):

    def test_find_the_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest(min_factor=100, max_factor=999)
        self.assertEqual(value, 906609)
        self.assertFactorsEqual(factors, [[913, 993]])
