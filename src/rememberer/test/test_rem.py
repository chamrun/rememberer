import unittest
import time

from rememberer import rem


def test_func(a, b):
    time.sleep(3)
    return a + b


class TestRem(unittest.TestCase):
    def test_rem(self):
        result1 = rem(test_func, 1, 2)

        start = time.time()
        result2 = rem(test_func, 1, 2)
        end = time.time()

        self.assertLess(end - start, 1)
        self.assertEqual(result1, result2)

    def test_rem_with_kwargs(self):
        result = rem(test_func, 1, b=2)
        self.assertEqual(result, 3)

    def test_rem_with_cached_result(self):
        rem(test_func, 1, 2)
        result = rem(test_func, 1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
