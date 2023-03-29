import unittest


class TestDemo(unittest.TestCase):

    def test_case01(self):
        assert 1 == 1

    def test_case02(self):
        assert 1 == 'a'


if __name__ == "__main__":
    unittest.main()


