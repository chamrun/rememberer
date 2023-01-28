import unittest
import os

from src import save_obj


class TestSaveObj(unittest.TestCase):
    def test_save_obj(self):
        obj = {'name': 'John', 'age': 30}
        name = 'test_obj'
        path = './test_rem/'
        save_obj(obj, name, path)
        self.assertTrue(os.path.exists(path + name + '.pkl'))

    def test_save_obj_with_default_name(self):
        obj = {'name': 'John', 'age': 30}
        path = './test_rem/'
        save_path = save_obj(obj, path=path)
        self.assertTrue(os.path.exists(save_path))

    def test_save_obj_with_default_path(self):
        obj = {'name': 'John', 'age': 30}
        name = 'test_obj'
        save_path = save_obj(obj, name)
        self.assertTrue(os.path.exists('./rem/' + name + '.pkl'))


if __name__ == '__main__':
    unittest.main()
