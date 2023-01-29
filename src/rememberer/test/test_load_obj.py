import unittest
from rememberer import save_obj, load_obj


class TestLoadObj(unittest.TestCase):
    def test_load_obj(self):
        obj = {'name': 'John', 'age': 30}
        name = 'test_obj'
        path = './test_rem/'
        save_obj(obj, name, path)
        loaded_obj = load_obj(name, path)
        self.assertEqual(obj, loaded_obj)

    def test_load_obj_with_default_path(self):
        obj = {'name': 'John', 'age': 30}
        name = 'test_obj'
        save_obj(obj, name)
        loaded_obj = load_obj(name)
        self.assertEqual(obj, loaded_obj)

    def test_load_obj_with_non_existent_file(self):
        name = 'non_existent_file'
        loaded_obj = load_obj(name)
        self.assertIsNone(loaded_obj)


if __name__ == '__main__':
    unittest.main()
