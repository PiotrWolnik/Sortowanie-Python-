# Pozostaw ten plik pusty, ew. wykorzystaj do własnych testów.
import unittest
from sort import quicksort, bubblesort, list_n_, check_list, random_list


class TestFunctions(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([i for i in range(1000)]), sorted(range(1000)))
        self.assertEqual(quicksort(list(reversed(check_list))), check_list)
        self.assertEqual(quicksort(list_n_), list_n_)
        self.assertEqual(quicksort(random_list), sorted(random_list))

    def test_bubblesort(self):
        self.assertEqual(bubblesort([i for i in range(1000)]), (sorted([i for i in range(1000)]), 0))
        # self.assertEqual(bubblesort(list(reversed(check_list))), (check_list, )
        self.assertEqual(bubblesort(list_n_), (list_n_, 0))
        # self.assertEqual(bubblesort(random_list), sorted(random_list))


if __name__ == '__main__':
    unittest.main()

# Piotr Wolnik, 403077