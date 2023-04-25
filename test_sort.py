from sort import insertionsort, mergesort
import unittest


def InsertionSortCase(self, input, expected):
    output = insertionsort(input)
    self.assertEqual(output, expected)


def MergeSortCase(self, input, expected):
    output = mergesort(input, 0, len(input)-1)
    self.assertEqual(output, expected)


class sortTest(unittest.TestCase):
    def test_insertion_sort(self):
        InsertionSortCase(self, input=[5, 3, 6, 1, 4, 9, 0], expected=[
                          0, 1, 3, 4, 5, 6, 9])
        InsertionSortCase(self, input=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                          expected=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        InsertionSortCase(self, input=[9, 8, 7, 6, 5, 4, 3, 2, 1],
                          expected=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        InsertionSortCase(self, input=[2], expected=[2])
        InsertionSortCase(self, input=[1, 5, 7, 4, 15, 99, 420, 3, 99, 8, 77, 1, 20, 23, 1], expected=[
            1, 1, 1, 3, 4, 5, 7, 8, 15, 20, 23, 77, 99, 99, 420])

    def test_merge_sort(self):
        MergeSortCase(self, input=[5, 3, 6, 1, 4, 9, 0], expected=[
            0, 1, 3, 4, 5, 6, 9])
        MergeSortCase(self, input=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      expected=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        MergeSortCase(self, input=[9, 8, 7, 6, 5, 4, 3, 2, 1],
                      expected=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        MergeSortCase(self, input=[2], expected=[2])
        MergeSortCase(self, input=[1, 5, 7, 4, 15, 99, 420, 3, 99, 8, 77, 1, 20, 23, 1], expected=[
            1, 1, 1, 3, 4, 5, 7, 8, 15, 20, 23, 77, 99, 99, 420])


if __name__ == '__main__':
    unittest.main()
