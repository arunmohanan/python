import unittest

import OsPractice


class TestOsUtils(unittest.TestCase):

    def test_directory_with_file_list_only(self):
        os_utils = OsPractice.OsUtils()
        actual_directory_contents = os_utils.print_directory_contents("C:\\Users\\anu\\Documents\\GitHub\\python\\tests")
        self.assertEqual(actual_directory_contents,['TestOsUtils.py', 'test_NumberReader.py', '__init__.py'])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
