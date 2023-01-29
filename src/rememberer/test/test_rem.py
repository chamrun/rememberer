import unittest
import time

from rememberer import rem


def test_func(a, b):
    time.sleep(2)
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

    def test_methods(self):
        class Test:
            def test_method(self, a, b):
                time.sleep(2)
                return a + b

        test = Test()
        result1 = rem(test.test_method, 1, 2)

        start = time.time()
        result2 = rem(test.test_method, 1, 2)
        end = time.time()

        self.assertLess(end - start, 1)
        self.assertEqual(result1, result2)

    def test_methods_with_kwargs(self):
        class Test:
            def test_method(self, a, b):
                time.sleep(2)
                return a + b

        test = Test()
        result1 = rem(test.test_method, 1, b=2)

        start = time.time()
        result2 = rem(test.test_method, 1, b=2)
        end = time.time()

        self.assertEqual(result2, 3)
        self.assertEqual(result2, result1)
        self.assertLess(end - start, 1)

    def test_dicts(self):
        def test_func2(a, b):
            time.sleep(2)
            return a['a'] + b['b']

        result1 = rem(test_func2, {'a': 1}, {'b': 2})

        start = time.time()
        result2 = rem(test_func2, {'a': 1}, {'b': 2})
        end = time.time()

        self.assertLess(end - start, 1)
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
