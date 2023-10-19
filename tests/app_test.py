import unittest

from api.app import process_query


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("Rob", process_query("what is your name?"))


if __name__ == '__main__':
    unittest.main()
