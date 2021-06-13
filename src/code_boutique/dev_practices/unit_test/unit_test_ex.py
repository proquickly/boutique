
import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


# pytest only needs from here...
def test_string_pytest():
    a = 'some'
    b = 'some'
    assert a == b


def test_boolean(self):
    a = True
    b = True
    assert a is b
# to here


if __name__ == '__main__':
    unittest.main()
