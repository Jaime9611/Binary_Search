import unittest

from search import binary_search as bs


class TestBinarySearches(unittest.TestCase):

    def test_basic(self):
        sample = [2, 4, 6, 8, 9]

        self.assertEqual(bs(6, sample), 2)

    
    def test_medium(self):
        sample = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # lista de prueba

        self.assertEqual(bs(67, sample), 18)


if __name__ == "__main__":
    unittest.main()