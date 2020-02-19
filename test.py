import unittest

from search import binary_search as bs
from errors import NotOrderedListError, NotSameTypeError


class TestBinarySearches(unittest.TestCase):

    def test_short_list(self):
        sample = [2, 4, 6, 8, 9]

        self.assertEqual(bs(6, sample), 2)

    def test_large_list(self):
        sample = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # lista de prueba

        self.assertEqual(bs(67, sample), 18)

    def test_strings_list(self):
        sample = ['Carlos', 'Daniela', 'George', 'Laura', 'Tom']

        self.assertEqual(bs('George', sample), 2)

    def test_not_orderered(self):
        sample = [3, 5, 7, 9, 8]

        self.assertRaisesRegex(NotOrderedListError, r".+", bs, 5, sample)

    def test_unequal_types_list(self):
        sample = [1, 'Carlos', 'Ana', 3, 5]

        with self.assertRaisesRegex(NotSameTypeError, r".+"):
            bs(3, sample)


if __name__ == "__main__":
    unittest.main()